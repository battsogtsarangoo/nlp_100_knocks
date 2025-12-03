import os
import pandas as pd
from google import genai
from dotenv import load_dotenv
import time

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

df = pd.read_csv("anatomy.csv")

correct = 0
REQUEST_DELAY = 6

# ===== 2. LLM に解答させるループ =====
for i, row in df.iterrows():
    
    question = row.iloc[0]
    A= row.iloc[1]
    B = row.iloc[2]
    C = row.iloc[3]
    D = row.iloc[4]
    answer = row.iloc[5].strip().upper()
    prompt = (
        "次の選択肢から最も正解に近いものを一つ選んでください。\n\n"
        f"問題：{question}\n"
        f"A:{B}\n"
        f"B:{D}\n"
        f"C:{A}\n"
        f"D:{C}\n\n"
        "答えはA/B/C/Dの文字だけで答えてください。\n"
        "答え："
    )

    response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents= prompt
        )
    model_answer = response.text.strip().upper()
    
    if model_answer == answer:
        correct += 1
    time.sleep(REQUEST_DELAY)

accuracy = correct / len(df)
print(f"正解数：{correct}/{len(df)}")
print(f"正解率：{accuracy * 100:.2f}%")


