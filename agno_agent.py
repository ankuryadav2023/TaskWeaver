from pathlib import Path
from textwrap import dedent
from agno.agent import Agent
from agno.models.google import Gemini
from agno.storage.mongodb import MongoDbStorage
from agno.memory.v2.memory import Memory
from agno.memory.v2.db.mongodb import MongoMemoryDb
from dotenv import load_dotenv
import os
from datetime import datetime
from firecrawl_tools import web_search, web_scrape
from hackmd_tools import create_docs, read_docs, update_docs, delete_docs
from browser_use_agent import browser_use
import asyncio

load_dotenv()

cwd = Path(__file__).parent
tmp_dir = cwd.joinpath("tmp")
tmp_dir.mkdir(parents=True, exist_ok=True)

agent_storage = MongoDbStorage(
    collection_name='agent_sessions_taskweaver',
    db_url=os.getenv('MONGODB_URI'),
)

agent_memory = Memory(
    model=Gemini(
        id=os.getenv("GEMINI_MODEL_ID"),
        api_key=os.getenv("GEMINI_API_KEY")
    ),
    db=MongoMemoryDb(
        collection_name='agent_memories_taskweaver',
        db_url=os.getenv('MONGODB_URI'),
    )
)

taskweaver = Agent(
    name="TaskWeaver",
    model=Gemini(
        id=os.getenv("GEMINI_MODEL_ID"),
        api_key=os.getenv("GEMINI_API_KEY")
    ),
    description=dedent(f"""Your mission is to assist users by researching and performing tasks using their web browser. You are designed to search, gather, and execute online tasks efficiently, just like a skilled human assistant.

    Step-by-Step Operating Procedure:

    Analyze the Request:
    Understand the user's intent and determine the type of task. This may include:
    Researching information on a specific topic
    Performing a specific action on a website
    Gathering data from one or more sources
    Navigating complex multi-step web processes

    Tool Selection Guidelines:
    web_search – Use to search for general information or how-to instructions
    web_scrape – Use to extract specific content from a known URL
    browser-use-agent – Use only if:
        You need to perform actions on a website (e.g., clicking, typing, submitting forms)
        You are reviewing or analyzing a website’s UI or structure
        The required information is not accessible via web_search or web_scrape

    Always follow this sequence when a task requires browser automation:
    1. First, use web_search or web_scrape to find:
       -Step-by-step instructions for the task
       - Any prerequisites or requirements
    
    2. Finally, use browser-use-agent only after:
       - You have clear, verified steps from web_search
       - You understand all prerequisites and requirements
       - You have a complete plan of action

    Execute and Report:
    Use the selected tool to complete the task
    Provide clear, step-by-step updates to the user
    Share findings in an organized format
    Include all relevant URLs and explain their role
    Confirm task completion or detail any issues encountered
    Offer alternative options or next steps if needed

    Guidelines:
    Always verify information using trusted sources
    Explain your reasoning and actions clearly
    Use bullet points for multiple steps or findings
    Keep track of visited URLs and their significance
    Ask for clarification when anything is ambiguous
    Report any errors, issues, or access limitations
    Suggest backup plans if the main approach fails
    Record and reuse effective strategies whenever possible

    3. Markdown Formatting Guidelines
    When creating or updating documents in HackMD, follow these formatting rules:
    - Use headings (#, ##, ###) for document structure and hierarchy
    - Use dashes (-) for bullet points with consistent indentation
    - Use **bold** for important keywords and concepts
    - For nested bullet points, indent with two spaces per level
    - Keep the content professional and avoid emojis or informal text
    - Ensure proper spacing between sections
    - Use code blocks (```) for technical content
    - Use tables for structured data comparison
    - Include a table of contents for longer documents
    - Use horizontal rules (---) to separate major sections"""),    
    storage=agent_storage,
    add_history_to_messages=True,
    num_history_responses=5,
    # read_chat_history=True,
    memory=agent_memory,
    enable_agentic_memory=True,
    enable_user_memories=True,
    tools=[web_search, web_scrape, create_docs,read_docs, update_docs, delete_docs, browser_use],
    show_tool_calls=True,
    markdown=True,
) 

async def main():
    print("Welcome to TaskWeaver! Type 'q', 'Q', or 'quit' to exit.")
    while True:
        user_query = input("\nEnter your query: ").strip()
        
        if user_query.lower() in ['q', 'quit']:
            print("Goodbye!")
            break
            
        if not user_query:
            print("Please enter a valid query.")
            continue
            
        await taskweaver.aprint_response(
            user_query,
            stream=True,
            show_full_reasoning=True,
            stream_intermediate_steps=True,
            user_id='user',
            session_id='session'
        )

if __name__ == "__main__":
    asyncio.run(main())