from firecrawl import FirecrawlApp, ScrapeOptions
import os
from dotenv import load_dotenv
from typing import List, Dict, Any, Optional

load_dotenv()

app = FirecrawlApp(api_key=os.getenv("FIRECRAWL_API_KEY"))

def web_search(query: str, limit: int = 5) -> List[Dict[str, Any]]:
    """
    Perform a web search using Firecrawl.
    
    Args:
        query (str): The search query
        limit (int): Maximum number of results to return (default: 5)
    
    Returns:
        List[Dict[str, Any]]: List of search results with markdown content
    """
    try:
        search_result = app.search(
            query,
            limit=limit,
            scrape_options=ScrapeOptions(formats=["markdown"])
        )
        
        results = []
        for result in search_result.data:
            results.append({
                'title': result.get('title', ''),
                'url': result.get('url', ''),
                'description': result.get('description', ''),
                'markdown': result.get('markdown', '')
            })
        
        return results
    except Exception as e:
        print(f"Error performing web search: {e}")
        return []

def web_scrape(url: str) -> Dict[str, str]:
    """
    Scrape content from a specific URL using Firecrawl.
    
    Args:
        url (str): The URL to scrape
    
    Returns:
        Dict[str, str]: Dictionary containing URL and markdown content
    """
    try:
        scrape_result = app.scrape_url(url, formats=['markdown'])
        
        return {
            'url': url,
            'markdown': scrape_result.get('markdown', '')
        }
    except Exception as e:
        print(f"Error scraping URL: {e}")
        return None


