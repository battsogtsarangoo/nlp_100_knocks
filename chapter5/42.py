import os
import time
import pandas as pd
from google import genai
from dotenv import load_dotenv

# ===== 1. APIキーとCSV読み込み =====
load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

df = pd.read_csv("anatomy.csv")

correct = 0
REQUEST_DELAY = 6

# ===== 2. LLM に解答させるループ =====
for idx, row in df.iterrows():

    question = row.iloc[0]   # 最初の列：質問文
    A = row.iloc[1]
    B = row.iloc[2]
    C = row.iloc[3]
    D = row.iloc[4]
    answer = row.iloc[5].strip().upper()

    prompt = (
        "次の選択肢から最も正しいものを一つ選んでください。\n\n"
        f"問題: {question}\n"
        f"A: {A}\n"
        f"B: {B}\n"
        f"C: {C}\n"
        f"D: {D}\n\n"
        "答えは A/B/C/D の文字だけで答えてください。\n"
        "答え:"
    )

    # ===== 3. Gemini API 呼び出し =====
    response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt 
   )
    model_answer = response.text.strip().upper()


 

    # ===== 4. 正解判定 =====
    if model_answer == answer:
        correct += 1
    time.sleep(REQUEST_DELAY)

# ===== 5. 正解率 =====
accuracy = correct / len(df)
print(f"正解数: {correct}/{len(df)}")
print(f"正解率: {accuracy * 100:.2f}%")
