# AirTrack

A Model Context Protocol (MCP) server for Apache Airflow that enables standardized access to DAG metadata, run status, and task insights, allowing seamless integration with MCP clients for monitoring and automation.

## About
This project implements a Model Context Protocol server that wraps Apache Airflow's REST API, allowing MCP clients to interact with Airflow in a standardized way. It uses the official Apache Airflow client library to ensure compatibility and maintainability.

## Project Structure

```
combined_project/
├── airflow/           # Airflow project files
│   ├── dags/         # Airflow DAG definitions
│   ├── logs/         # Airflow logs
│   ├── plugins/      # Airflow plugins
│   └── Docker-compose.yaml  # Docker compose file for Airflow
│
└── mpc/              # MPC application files
    ├── utils/        # Utility functions
    ├── server.py     # Main server file
    └── main.py       # Entry point
```

## Running the Projects

## Requirements

- Docker and Docker Compose for Airflow
- Python 3.8+ for MPC application
- Virtual environment for MPC application 

### Airflow

1. Navigate to the airflow directory:
   ```bash
   cd airflow
   ```

2. Start Airflow using Docker Compose:
   ```bash
   docker-compose up 
   ```

3. Access the Airflow web interface at http://localhost:8181

      **Username:** `admin` **Password:** `airflow`

### MPC Application

1. Navigate to the mpc directory:
   ```bash
   cd mpc
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # On Windows
   source .venv/bin/activate  # On Unix/MacOS
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the MPC server:
   ```bash
   python server.py
   ```
## Usage with Claude Desktop
   ```bash
   {
     "mcpServers": {
       "FlowPredictor": {
      "command": "D:\\Apps\\conda\\Scripts\\uv.EXE",
      "args": [
        "run",
        "--with",
        "mcp[cli]",
        "mcp",
        "run",
        "<---PATH OF YOUR SERVER FILE eg(C:\\Users\\..\\..\\..\\server.py) --->"
      ]
    }
      }
   }
   ```

## Integration

The Airflow DAGs can interact with the MPC application through API calls. Make sure both services are running when executing workflows that require MPC functionality.


![Logo](mcp\Airtrack.png)

## Future Development
-  **🔄 Live Updates – Stream DAG/task status via WebSocket or SSE.**
-  **🔐 Security – Add OAuth2, API keys, and role-based access.**  
-  **⚡ Event Triggers – Auto-trigger agents on DAG events.**  
-  **A📊 Analytics – Dashboard for DAG performance and trends.**  
- **🤖 AI Troubleshooting – Use LLMs for issue analysis and fixes.**  
