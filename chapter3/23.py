import re
import collections

filename = "./20.txt"
with open(filename, "r", encoding="utf-8") as f:
    pattern = "(={2,4}.*?={2,4})"
    result = re.findall(pattern, f.read())
    section = {}
    for text in result:
        c1 = collections.Counter(text)
        c2 = int(c1["="] / 2 - 1 )
        text = text.replace("=", "")
        section[text] = c2

# 結果を表示
from pprint import pprint
pprint(section)