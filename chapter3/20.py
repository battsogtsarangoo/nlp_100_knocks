import json


filename = f'./jawiki-country.json'

UK_text = ""

# ファイルを開く
with open(filename, 'r', encoding='utf-8') as f:
    # 1行ずつ読み込んで処理する
    for line in f:
        data = json.loads(line)
        
        if data['title'] == "イギリス":
            # 【重要】辞書全体ではなく、'text'の中身だけを取り出す
            UK_text = data['text']
            break

# 結果の確認
print(UK_text)