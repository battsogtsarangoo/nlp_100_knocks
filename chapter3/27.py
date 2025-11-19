import re
import ast 
from pprint import pprint

# 1. 保存したファイル「26.txt」を読み込む
filename = "./26.txt"


with open(filename, "r", encoding="utf-8") as f:
        
        inf_dic2 = ast.literal_eval(f.read())

inf_dic3 = {}

for key, text in inf_dic2.items():
        # 内部リンク [[記事名|表示名]] または [[記事名]] を除去する正規表現
        pattern = r'\[\[(?:[^|]*?\|)*?([^|]*?)\]\]'
        
        # \1 は「正規表現で見つけた 表示名 の部分」に置き換える
        clean_text = re.sub(pattern, r'\1', text)
        
        inf_dic3[key] = clean_text

    # 結果を表示
   
pprint(inf_dic3)