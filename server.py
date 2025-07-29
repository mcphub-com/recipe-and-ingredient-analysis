import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/zestfuldata/api/recipe-and-ingredient-analysis'

mcp = FastMCP('recipe-and-ingredient-analysis')

@mcp.tool()
def parse_ingredients(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''Parse recipe ingredients into structured data'''
    url = 'https://zestful.p.rapidapi.com/parseIngredients'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'zestful.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
