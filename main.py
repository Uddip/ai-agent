import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

MODEL_NAME = "gemini-2.0-flash-001"

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py '<input text>'")
        sys.exit(1)

    load_dotenv()
    api_key = os.getenv('GEMINI_API_KEY')

    client = genai.Client(api_key=api_key)
    user_input = sys.argv[1]
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_input)])
    ]

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=messages,
    )

    print(response.text)

    if len(sys.argv) > 2 and sys.argv[2] == "--verbose":
        print(f"User prompt: {user_input}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count + 1}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

if __name__ == "__main__":
    main()
