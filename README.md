# TaskWeaver

TaskWeaver is an AI-powered web automation and research assistant that helps users perform tasks using web browsers, search engines, and document management tools.

## Features

- Web search and scraping capabilities
- Browser automation for complex web tasks
- Document management with HackMD integration
- Memory and storage using MongoDB
- Powered by Google's Gemini AI model

## Prerequisites

- Python 3.8+
- MongoDB database
- Google Gemini API key
- HackMD API token
- Google Chrome browser installed

## Setup

1. Clone the repository:
```bash
git clone <your-repo-url>
cd TaskWeaver
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root directory with the following environment variables:
```env
# Google Gemini API Configuration
GEMINI_API_KEY=your_gemini_api_key
GEMINI_MODEL_ID=your_model_id

# MongoDB Configuration
MONGODB_URI=your_mongodb_uri

# Firecrawl API Configuration
FIRECRAWL_API_KEY=your_firecrawl_api_key
```

4. Set up Chrome for browser automation (Windows PowerShell):
```powershell
# Stop any running Chrome processes
Stop-Process -Name chrome -Force -ErrorAction SilentlyContinue

# Create Chrome debug profile directory
mkdir "C:\Temp\ChromeDebugProfile"

# Launch Chrome with remote debugging enabled
& "C:\Program Files\Google\Chrome\Application\chrome.exe" `
  --remote-debugging-port=9223 `
  --user-data-dir="C:\Temp\ChromeDebugProfile"
```

5. Run the application:
```bash
python agno_agent.py
```

## Usage

1. Start the application
2. Enter your query when prompted
3. The agent will analyze your request and use appropriate tools to complete the task
4. Type 'q' or 'quit' to exit

## Tools

- `web_search`: Search for information online
- `web_scrape`: Extract content from specific URLs
- `browser_use`: Perform browser automation tasks
- `create_docs`: Create new HackMD documents
- `read_docs`: Read existing HackMD documents
- `update_docs`: Update HackMD documents
- `delete_docs`: Delete HackMD documents

## License

MIT License 