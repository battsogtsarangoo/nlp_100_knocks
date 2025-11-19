import json
import re

# --- 1. ファイルからイギリスの本文を読み込む ---
UK_text = ""
filename = f'./jawiki-country.json'


with open(filename, 'r', encoding='utf-8') as f:
    for line in f:
        data = json.loads(line)
        if data['title'] == "イギリス":
            UK_text = data['text']
            break

# --- 2. 正規表現でカテゴリ行を抽出する ---
UK_text
pattern = r"\[\[Category:.*?\]\]"
result = re.findall(pattern, UK_text)
    
    # 結果を表示（pprintを使うと見やすいです）
from pprint import pprint
pprint(result)
