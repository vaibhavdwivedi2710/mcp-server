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

1. Create a `.env` file in the root directory of the project
2. Add your Google API key to the `.env` file:
```env
GOOGLE_API_KEY=your-google-api-key-here
```

**Note**: Make sure to add `.env` to your `.gitignore` file to keep your API key secure and never commit it to version control.

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
├── .env                      # Environment variables (create this file)
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
