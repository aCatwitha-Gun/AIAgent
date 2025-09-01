import os
import sys
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

def main():

    arguments = sys.argv
    prompt = arguments[1]

    print(prompt)

    if len(arguments) < 1:
        print("ERROR: Please include command line argument to use as prompt")
        sys.exit(1)

    response = client.models.generate_content(
        model="gemini-2.0-flash-001", contents=prompt
    )
    print(response.text)
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

if __name__ == "__main__":
    main()
