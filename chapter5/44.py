import os
from google import genai
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

chat = client.chats.create(model="gemini-2.5-flash")

# プロンプトを input に入れる
response = chat.send_message(
   "つばめちゃんは渋谷駅から東急東横線に乗り、自由が丘駅で乗り換えました。東急大井町線の大井町方面の電車に乗り換えたとき、各駅停車に乗るべきところ、間違えて急行に乗ってしまいました。自由が丘の次の急行停車駅で降り、反対方向の電車で一駅戻った駅がつばめちゃんの目的地です。目的地の駅の名前を答えてください。"
)

print(response.text)
