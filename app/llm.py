import os
import json
import time
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def classify_ticket(message: str):
    prompt = f"""
You are a support automation assistant.

Classify the ticket into one of:
Billing, Technical, Shipping, Other.

Return STRICT JSON:
{{
  "category": "...",
  "confidence": 0.0 to 1.0,
  "draft_reply": "..."
}}

Ticket:
{message}
"""

    for attempt in range(3):
        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.2
            )

            content = response.choices[0].message.content
            return json.loads(content)

        except Exception as e:
            if attempt == 2:
                raise e
            time.sleep(1)
