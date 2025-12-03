import os
from google import genai
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

topic = "月"
prompt = f"""
お題「{topic}」に沿って、ユーモアや風情を感じる川柳を10個作ってください。
各川柳は簡潔でリズムよく、1行ずつ表示してください。
"""

# 修正：chats.create() + send_message() を使用
chat = client.chats.create(model="gemini-2.5-flash")
response = chat.send_message(prompt)

# 結果の取得
print(response.text)
