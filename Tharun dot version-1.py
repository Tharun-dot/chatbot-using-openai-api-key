import os
from groq import Groq

api_key = os.getenv("GROQ_API_KEY")
if api_key is None:
    raise ValueError("API key is not set in environment variables")

client = Groq(api_key=api_key)

user_input=input("THARUN-DOT:")
chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": user_input,
        }
    ],
    model="llama3-8b-8192",
)

print(chat_completion.choices[0].message.content)
