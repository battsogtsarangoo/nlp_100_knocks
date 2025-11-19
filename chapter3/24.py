import re

filename = "./20.txt"
with open(filename, "r", encoding = "utf-8") as f:
    pattern = '\[\[ファイル:(.*?)(?:\||\])'
    result = re.findall(pattern, f.read())

  # 結果を表示
from pprint import pprint
pprint(result)



