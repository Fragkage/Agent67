import argparse
import os 
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")

client = OpenAI(
    base_url = "https://openrouter.ai/api/v1",
    api_key = api_key,
)

if api_key is None:
    raise RuntimeError("OPEN_ROUTER_API_KEY not found")

parser = argparse.ArgumentParser(description="chatbot")
parser.add_argument("user_prompt", type=str, help = "User Prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()

messages = [
    {"role": "user", "content": args.user_prompt,}
    ]

response = client.chat.completions.create(
    model = "openrouter/free",
    messages = messages,
)

if args.verbose:
    if response.usage is None:
        raise RuntimeError("Response has no usage data. The API request may have failed.")
    
    print(f"Propmt tokens: {response.usage.prompt_tokens}")
    print(f"Response tokens: {response.usage.completion_tokens}")

print("Response: ")
print(response.choices[0].message.content)


