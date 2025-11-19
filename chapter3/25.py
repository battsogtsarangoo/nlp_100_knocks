import re
from pprint import pprint

filename = "./20.txt"

with open(filename, "r", encoding="utf-8") as f:
    # --- ステップ1: 基礎情報ブロックの抽出 ---
    pattern = r"\{\{基礎情報.*?\n\}\}"
    result = re.findall(pattern, f.read(), re.DOTALL)

    if result:
        result[0] += "\n"

        # --- ステップ2: 辞書への抽出 ---
        pattern2 = r'(?:^|\n)\|(.+?)\s*=\s*(.+?)(?=\n|$)'
        result2 = re.findall(pattern2, result[0])

        info_dict = {}
        for i, j in result2:
            info_dict[i] = j

        pprint(info_dict)
