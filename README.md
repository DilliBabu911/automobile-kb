# Car Complaint Analyzer — Knowledge Base

An AI-powered web app that analyzes automobile complaints and saves them to a local knowledge base for future reference.

## Features

- Describe your car problem and get an instant AI diagnosis
- Structured report with issue, severity, possible cause, repair cost, and suggested action
- All complaints and answers saved to a local SQLite database
- View and delete past complaint history
- Quick-select example complaints for fast testing

## Tech Stack

- **Frontend:** Streamlit
- **AI Model:** Llama 3.3 70B via Groq API
- **Database:** SQLite (local file `complaints.db`)
- **Language:** Python 3

## Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/automobile-kb.git
   cd automobile-kb
   ```

2. **Install dependencies**
   ```bash
   pip install streamlit groq python-dotenv
   ```

3. **Create a `.env` file** in the project root:
   ```
   GROQ_API_KEY=your_groq_api_key_here
   ```

4. **Run the app**
   ```bash
   streamlit run app.py
   ```

## Project Structure

```
automobile-kb/
├── app.py          # Streamlit UI
├── analyzer.py     # Groq AI integration and analysis logic
├── database.py     # SQLite database setup and queries
├── .env            # API keys (not committed)
└── complaints.db   # Local database (not committed)
```

## Usage

1. Open the app in your browser (default: `http://localhost:8501`)
2. Go to the **Ask a Complaint** tab and describe your car problem
3. Click **Analyze My Car Problem** to get an AI diagnosis
4. View all past complaints in the **View History** tab

## Disclaimer

For reference only. Always consult a certified mechanic for actual repairs.
