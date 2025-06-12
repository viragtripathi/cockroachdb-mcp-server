from fastapi.testclient import TestClient
from cockroachdb_mcp_server.main import app

client = TestClient(app)

def test_debug_info():
    response = client.get("/debug/info")
    assert response.status_code == 200
    assert "database" in response.json()

def test_debug_tables():
    response = client.get("/debug/tables")
    assert response.status_code == 200
    assert "tables" in response.json()

def test_debug_sql_valid():
    response = client.post("/debug/sql", json={"query": "SELECT 1"})
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_debug_sql_invalid():
    response = client.post("/debug/sql", json={"query": "DROP TABLE mcp_contexts"})
    assert "error" in response.json()