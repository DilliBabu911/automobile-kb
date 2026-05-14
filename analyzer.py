import os
from groq import Groq
from dotenv import load_dotenv
from database import save_complaint

load_dotenv()

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def analyze_and_save(complaint: str) -> str:
    prompt = f"""
    You are an expert automobile mechanic with 20+ years of experience.
    A customer describes their car problem: "{complaint}"

    Analyze and respond in this exact format:
    - Issue: <what the problem is>
    - Severity: <Low / Medium / High>
    - Possible Cause: <reason behind the problem>
    - Estimated Repair Cost: <cost range in USD>
    - Suggested Action: <what the customer should do next>
    - Time to Fix: <how urgent is the repair>
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=500
    )
    answer = response.choices[0].message.content

    # Save Q&A to database — this is the key difference from Project 1
    save_complaint(complaint, answer)

    return answer
