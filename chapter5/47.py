import os
from google import genai
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# 46で作った川柳リスト
senryu_list = [
    "窓開けて　光のシャワー　月見酒",
"餅はない　月を肴に　一杯だ",
"茶を啜り　無言で月と　語り合う",
"うさぎさん　杵を振り上げ　筋トレか",
"遠い君　同じ月見て　今を思う",
"スマホ消し　月へと向けろ　心の目",
"歴史知り　未来を照らす　古の月",
"満月は　ダイエット中の　敵か味方か",
"雲隠れ　想像させる　粋な月",
"月光に　ひっそり伸びる　影ぼうし"
]

# 評価用プロンプト
prompt = "以下の川柳の面白さを10段階で評価してください。10が最も面白いです。\n\n"
for i, senryu in enumerate(senryu_list, 1):
    prompt += f"{i}. {senryu}\n"

prompt += "\n出力は各川柳ごとに「点数」の形式でお願いします。"

# chats.create + send_message で評価
chat = client.chats.create(model="gemini-2.5-flash")
response = chat.send_message(prompt)

# 結果表示
print(response.text)
