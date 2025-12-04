# MCP Server

A Model Context Protocol (MCP) server built with FastMCP that provides Google search functionality using Google Gemini API.

## Features

- 🔍 **Google Search**: Perform Google searches using Google Gemini API
- 🏥 **Health Check**: Monitor server health status

## Installation

1. Clone the repository:
```bash
git clone https://github.com/vaibhavdwivedi2710/mcp-server.git
cd mcp-server
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Configuration

Before running the server, you need to configure your Google API key:

1. Open `tools/google_search_tool.py`
2. Replace `YOUR_GOOGLE_API_KEY_HERE` with your actual Google API key:
```python
GOOGLE_API_KEY = "your-actual-api-key-here"
```

Alternatively, you can use environment variables with `python-dotenv` for better security.

## Usage

Start the MCP server:

```bash
python server.py
```

The server will start on `http://0.0.0.0:8000` with the following endpoints:

- **SSE Endpoint**: `/mcp-server/sse`
- **Message Endpoint**: `/mcp-server/message`
- **Health Check**: `/health`

## Available Tools

### Google Search
Perform a Google search query using Gemini API.

**Tool**: `google_search(query: str)`

This tool uses the Google Gemini API to perform web searches and returns relevant search results based on your query.

## Project Structure

```
mcp-server/
├── server.py                 # Main MCP server file
├── requirements.txt          # Python dependencies
├── tools/
│   ├── __init__.py
│   └── google_search_tool.py # Google search implementation
└── README.md
```

## Dependencies

- `mcp>=1.6.0` - Model Context Protocol framework
- `fastapi` - Web framework
- `uvicorn` - ASGI server
- `google-genai` - Google Gemini API client
- `python-dotenv` - Environment variable management

## API Endpoints

### Health Check
```bash
GET /health
```

Returns:
```json
{
  "status": "MCP Server is Healthy"
}
```

## Development

The server uses FastMCP for building MCP-compatible tools and endpoints. All tools are defined using the `@mcp.tool()` decorator, and custom routes can be added using `@mcp.custom_route()`.

## License

See [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
