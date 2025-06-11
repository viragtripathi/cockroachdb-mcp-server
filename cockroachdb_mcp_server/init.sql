CREATE TABLE IF NOT EXISTS mcp_contexts (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  context_name STRING NOT NULL,
  context_version STRING NOT NULL,
  body JSONB NOT NULL,
  created_at TIMESTAMP DEFAULT now()
);
