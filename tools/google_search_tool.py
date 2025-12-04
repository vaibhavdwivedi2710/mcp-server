import asyncio
import os
import time
import logging
from google import genai
from google.genai.types import Tool, GoogleSearch, GenerateContentConfig

# Configure logger for this module
logger = logging.getLogger(__name__)

# Get API key from environment variable
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

client = genai.Client(api_key=GOOGLE_API_KEY)
model = "gemini-2.5-flash"
google_search_tool = Tool(google_search=GoogleSearch())

async def perform_google_search(query: str):
    search_result = list()
    retries = 0
    delay_ms = 500
    max_retries = 3

    while retries < max_retries:
        try:
            start_time = time.time()
            response = await client.aio.models.generate_content(
                model=model,
                content=query,
                config=GenerateContentConfig(
                    tools=[google_search_tool],
                    response_modalities=["text"],
                    automatic_function_calling={
                        "ignore_call_history": True,
                    },
                ),
            )
            elapsed_time = time.time() - start_time
            logger.info(f"Google search completed in {elapsed_time:.2f} seconds")
            logger.info(f"Search result: {response.text}")
            return {"result": response.text, "query": query}
        except Exception as e:
            logger.error(f"Error performing Google search: {e}")
            retries += 1
            if retries >= max_retries:
                logger.error(f"Failed to perform Google search after {max_retries} retries")
                return {"error": "Failed to perform Google search"}
            logger.warning(f"Retrying Google search... ({retries}/{max_retries})")
            await asyncio.sleep(delay_ms / 1000)
    return {"error": "Failed to perform Google search"}