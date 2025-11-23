import os
import sys
from dotenv import load_dotenv
from google import genai

MODEL_NAME = "gemini-2.0-flash-001"

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py '<input text>'")
        sys.exit(1)
        
    load_dotenv()
    api_key = os.getenv('GEMINI_API_KEY')

    client = genai.Client(api_key=api_key)
    input = sys.argv[1]

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=input
    )

    print(response.text)
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

if __name__ == "__main__":
    main()