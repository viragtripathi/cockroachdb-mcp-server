import pytest
from fastapi.testclient import TestClient
from cockroachdb_mcp_server.main import app

client = TestClient(app)

@pytest.fixture(autouse=True)
def mock_db_engine(mocker):
    mock_engine = mocker.MagicMock()
    mock_conn = mocker.MagicMock()
    mock_engine.connect.return_value.__enter__.return_value = mock_conn

    # Patch get_sqlalchemy_engine to return mock
    mocker.patch("cockroachdb_mcp_server.routes.debug.get_sqlalchemy_engine", return_value=mock_engine)

    # Setup mock responses
    mock_conn.execute.side_effect = lambda query: {
        "SELECT version();": [("CockroachDB 25.2.0",)],
        "SELECT current_database();": [("defaultdb",)],
        "SELECT table_name FROM information_schema.tables ...": [("mcp_contexts",)],
        "SELECT 1": [(1,)],
    }.get(str(query).strip(), [])

def test_debug_info():
    res = client.get("/debug/info")
    assert res.status_code == 200
    assert "database" in res.json()
    assert "version" in res.json()

def test_debug_tables():
    res = client.get("/debug/tables")
    assert res.status_code == 200
    assert "tables" in res.json()

def test_debug_sql_valid():
    res = client.post("/debug/sql", json={"query": "SELECT 1"})
    assert res.status_code == 200
    assert isinstance(res.json(), list)

def test_debug_sql_invalid():
    res = client.post("/debug/sql", json={"query": "DROP TABLE mcp_contexts"})
    assert res.status_code == 200
    assert "error" in res.json()
