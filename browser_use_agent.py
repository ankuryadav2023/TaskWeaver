from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import Agent, Browser, BrowserConfig
from browser_use.browser.context import BrowserContext
import asyncio
import os
from dotenv import load_dotenv
load_dotenv()

browser_config = BrowserConfig(
    cdp_url="http://localhost:9223"
)

browser = Browser(config=browser_config)

async def browser_use(task: str) -> str:
    """
    Perform browser automation tasks using the browser_use agent.
    
    Args:
        task (str): A step-by-step description of the task to perform, for example:
                   '''
                   1. Go to https://example.com
                   2. Click the "Sign In" button
                   3. Enter "username" in the email field
                   4. Enter "password" in the password field
                   5. Click the "Login" button
                   '''
    
    Returns:
        str: The final result of the browser automation task or error message
    """
    try:
        agent = Agent(
            task=task,
            llm=ChatGoogleGenerativeAI(
                api_key=os.getenv("GEMINI_API_KEY"),
                model="gemini-2.5-flash-preview-04-17"
            ),
            browser=browser
        )
        
        response = await agent.run()
        
        return response.final_result()
        
    except Exception as e:
        return f'Error during browser automation: {str(e)}'

if __name__ == "__main__":
    # Example task
    task = """1. Go to https://docs.google.com/document/u/0/
        2. Click the Blank button (the one with the colorful '+' icon) to open a new, empty document.
        3. Paste the text in the page."""
    
    # Run the async function
    result = asyncio.run(browser_use(task))
    print("Result:", result)