# ai_code_reviewer

A project for AI-powered code review and analysis.

## Features
- Fetches changed code from GitHub pull requests
- Runs static analysis and LLM-based review
- Summarizes results and can send to Slack

## Setup
1. Clone the repo
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up your `.env` file with required tokens (e.g., `GITHUB_TOKEN`)

## Usage
Run the main pipeline on a PR URL:
```bash
python main.py <github_pull_request_url>
```

## Project Structure
- `main.py` — Entry point for code review pipeline
- `reviewer/` — Modules for GitHub, static analysis, LLM review, summarization, notifications
- `test_token.py`, `test_send_slack.py` — Example/test scripts

---
Feel free to contribute or open issues!
