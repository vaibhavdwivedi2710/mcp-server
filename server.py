import asyncio
import logging
from datetime import datetime
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP
from fastapi.responses import JSONResponse
from tools.google_search_tool import perform_google_search

# Load environment variables from .env file
load_dotenv()

# Configure standard Python logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

#Initialize FastMCP Server
mcp = FastMCP(
    host="0.0.0.0",
    port=8000,
    sse_path="/mcp-server/sse",
    message_path="/mcp-server/message",
)

@mcp.custom_route("/health", methods=["GET"])
async def health(request):
    return JSONResponse({"status": "MCP Server is Healthy"})


@mcp.tool()
async def get_lat_log(request):
    """Get the current time"""
    return JSONResponse({"time": datetime.now().isoformat()})

@mcp.tool()
async def fetch_weather(request):
    """Get the current weather"""
    return JSONResponse({"weather": "Sunny"})

@mcp.tool()
async def google_search(query: str):
    """Perform a Google search"""
    logger.info(f"Performing Google search for: {query}")
    result = await perform_google_search(query)
    logger.debug(f"Google search result: {result}")
    return result

@mcp.tool()
async def get_google_directions(request):
    """Get the Google directions"""
    return JSONResponse({"directions": "Google Directions"})


async def start_server():
    """Start the MCP Server"""
    print("Starting MCP Server on port 8000...")
    await mcp.run_sse_async()

if __name__ == "__main__":
    asyncio.run(start_server())