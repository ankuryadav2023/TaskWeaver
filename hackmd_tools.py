from browser_use_agent import browser_use
import asyncio
from typing import Optional

async def create_docs(title: str, markdown: str) -> str:
    """
    Create a new document in HackMD.
    
    Args:
        title (str): The title of the document
        markdown (str): The markdown content of the document
    
    Returns:
        str: The URL of the created document or error message
    """

    task = f"""1. Go to https://hackmd.io/new
    2. Paste the following markdown in the editor on the left side:
    {markdown}
    3. Click on the three dots(Menu icon) on the top right
    4. Click on "Note settings"
    5. In the opened modal, remove the current title and paste this new title: {title}
    6. Wait for the document to save automatically
    7. Get the current URL from the browser's address bar"""
    
    return await browser_use(task)

async def read_docs(url: str) -> str:
    """
    Read a document from HackMD.
    
    Args:
        url (str): The URL of the document to read
    
    Returns:
        str: The title and content of the document or error message
    """
    task = f"""1. Go to {url}
    2. Wait for the document to load
    3. Get the title from the top center of the page
    4. Get the content from the editor on the left side
    5. Return both title and content in this format:
    Title: [document title]
    Content: [document content]"""
    
    return await browser_use(task)

async def update_docs(url: str, new_title: str, new_markdown: str) -> str:
    """
    Update an existing document in HackMD.
    
    Args:
        url (str): The URL of the document to update
        new_title (str): The new title for the document
        new_markdown (str): The new markdown content
    
    Returns:
        str: Success message or error message
    """
    task = f"""1. Go to {url}
    2. Wait for the document to load
    3. Delete all content in the editor on left side
    4. Paste the following new markdown:
    {new_markdown}
    5. Click on the three dots(Menu icon) on the top right
    6. Click on "Note settings"
    7. In the opened modal, remove the current title and paste this new title: {title}"""
    
    return await browser_use(task)

async def delete_docs(url: str) -> str:
    """
    Delete a document from HackMD.
    
    Args:
        url (str): The URL of the document to delete
    
    Returns:
        str: Success message or error message
    """
    task = f"""1. Go to {url}
2. Wait for the document to load
3. Click on the three dots(Menu icon) on the top right
4. Click on "Delete this note"
5. Confirm the deletion in the popup dialog"""
    
    return await browser_use(task)

# Example usage
if __name__ == "__main__":
    async def main():
        # Create a new document
        create_result = await create_docs(
            "Test Document",
            "# Test Document\n\nThis is a test document created using browser automation."
        )
        print("Create Result:", create_result)
        
        # Read the document
        if "https://hackmd.io/" in create_result:
            read_result = await read_docs(create_result)
            print("Read Result:", read_result)
            
            # Update the document
            update_result = await update_docs(
                create_result,
                "Updated Test Document",
                "# Updated Test Document\n\nThis document has been updated using browser automation."
            )
            print("Update Result:", update_result)
            
            # Delete the document
            delete_result = await delete_docs(create_result)
            print("Delete Result:", delete_result)

    asyncio.run(main()) 