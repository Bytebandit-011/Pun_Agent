# Pun Agent (Streamlit + Gemini)

A tiny Streamlit app that generates short, witty puns about any subject using an Agno Agent with Google Gemini.

## Quick Start

- Requirements: Python 3.10+ (recommended), pip
- Install:
  - Windows (PowerShell):
    - Create venv: `py -m venv .venv`
    - Activate: `.venv\Scripts\Activate`
    - Install deps: `pip install -r requirements.txt`
- Environment:
  - Create a `.env` file in the project root with:
    ```
    GEMINI_API_KEY="your_google_gemini_api_key"
    ```
    (You can also keep your existing `.env`; the app only needs GEMINI_API_KEY.)
- Run:
  - `streamlit run agent.py`

## Usage

1. Open the app URL from the terminal output.
2. Enter a subject (e.g., “space”, “pizza”, “Python”).
3. Click “Generate Pun” to get a short, humorous pun.

## Tech

- Streamlit UI
- Agno Agent (`agno==1.2.13`)
- Google Gemini via `google-genai==1.9.0`

## OutPut


<img width="1912" height="907" alt="image" src="https://github.com/user-attachments/assets/f51b59ef-8a60-425d-9d10-182d4f931e19" />
