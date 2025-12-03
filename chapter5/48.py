import os
import re
from google import genai
from dotenv import load_dotenv
import statistics
import time

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

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

def evaluate_senryu(senryu_list):
    prompt = "以下の川柳の面白さを10段階で評価してください。10が最も面白いです。\n\n"
    for i, senryu in enumerate(senryu_list, 1):
        prompt += f"{i}. {senryu}\n"
    prompt += "\n出力は各川柳ごとに「点数」の形式でお願いします（例: 1: 7）"

    chat = client.chats.create(model="gemini-2.0-flash")
    response = chat.send_message(prompt)
    
    # 点数だけ抽出
    scores = [int(x) for x in re.findall(r'\b\d+\b', response.text)]
    # 川柳の数と合わない場合は None で埋める
    if len(scores) != len(senryu_list):
        scores += [None] * (len(senryu_list) - len(scores))
    return scores

num_trials = 5  # 繰り返す回数
all_scores = []

for trial in range(num_trials):
    scores = evaluate_senryu(senryu_list)
    all_scores.append(scores)
    print(f"試行 {trial+1}: {scores}")
    time.sleep(6)  # 連続リクエストで制限に引っかからないよう少し待つ

# 平均と標準偏差を計算して表示
print("\n=== 平均と標準偏差 ===")
for i in range(len(senryu_list)):
    ith_scores = [trial[i] for trial in all_scores]
    mean = statistics.mean(ith_scores)
    stdev = statistics.stdev(ith_scores)
    print(f"{i+1}. {senryu_list[i]} 平均: {mean:.2f}, 標準偏差: {stdev:.2f}")
