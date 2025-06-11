#!/bin/bash
set -e

# Start the app
echo "🚀 Starting MCP server..."
exec uvicorn app.main:app --host 0.0.0.0 --port 8080
