import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")  # または直接文字列に置き換え
url = f"https://generativelanguage.googleapis.com/v1beta/models?key={API_KEY}"

resp = requests.get(url)
print(resp.json())
