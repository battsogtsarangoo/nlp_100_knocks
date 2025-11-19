import re
import ast
from pprint import pprint

# 1. 保存したファイル「27.txt」を読み込む
filename = "./27.txt"


with open(filename, "r", encoding="utf-8") as f:
    content = f.read()
        # 文字列を辞書に復元
    inf_dic3 = ast.literal_eval(content)

    # --- ここから問題28 (マークアップ除去) ---
    inf_dic4 = {}

for key, text in inf_dic3.items():
        # 1. <ref>タグとその中身を消す（脚注）
        text = re.sub(r'<ref(\s.*?)?>.*?</ref>', '', text, flags=re.DOTALL)

        # 2. その他のHTMLタグ (<br>, <ref/> 等) を消す
        text = re.sub(r'<[^>]+>', '', text)

        # 3. 外部リンクを除去
        text = re.sub(r'\[https?://(?:[^\s]*?\s)?([^]]*?)\]', r'\1', text)

        # 4. テンプレート {{...}} の除去
        pattern_template = r'\{\{(?:[^|]*?\|)*?([^|]*?)\}\}'
        text = re.sub(pattern_template, r'\1', text)

        # 5. それでも残った空のテンプレートや {{0}} などを消す
        text = re.sub(r'\{\{.*?\}\}', '', text)

        # 辞書に格納
        inf_dic4[key] = text

    # 結果を表示
  
pprint(inf_dic4)


