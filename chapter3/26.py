import re
from pprint import pprint

filename = "./20.txt"


with open(filename, "r", encoding="utf-8") as f:
        # --- ステップ1: 基礎情報ブロックの抽出 ---
        pattern = r'基礎情報(.*?\<references/\>)'
        result = re.findall(pattern, f.read(), re.DOTALL)
        
        if result:
          
            result[0] += "\n"
     
            pattern2 = r'(?:^|\n|\\n)\|(.+?)\s*=\s*(.+?)(?=\n|\\n|$)'
            
            result2 = re.findall(pattern2, result[0])
            
            info_dict = {}
            for i, j in result2:
                info_dict[i] = j

            inf_dic2 = {}
            for key, text in info_dict.items():
                clean_text = re.sub(r"'{2,5}", "", text)
    
                inf_dic2[key] = clean_text
            pprint(inf_dic2)