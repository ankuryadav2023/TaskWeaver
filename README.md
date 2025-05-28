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

3. Create a `.env` file with your credentials:
```
GEMINI_API_KEY=your_gemini_api_key
GEMINI_MODEL_ID=your_model_id
MONGODB_URI=your_mongodb_uri
HACKMD_API_TOKEN=your_hackmd_token
```

4. Run the application:
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