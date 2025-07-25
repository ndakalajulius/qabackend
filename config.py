from dotenv import load_dotenv
import os

load_dotenv()  

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if OPENAI_API_KEY is None:
    raise ValueError("OPENAI_API_KEY not found in environment variables")
