import requests
import ast

# ファイル読み込み
filename = "28.txt"

with open(filename, "r", encoding="utf-8") as f:
        info_dict = ast.literal_eval(f.read())


flag = info_dict.get("国旗画像")

if flag:
    url = "https://ja.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "titles": f"File:{flag}",
        "prop": "imageinfo",
        "iiprop": "url"
    }
    
    # 【重要】ボット判定を避けるためのヘッダー（名刺のようなもの）
    headers = {"User-Agent": "NLP100Knocks-Student/1.0"}

    # headersを追加してリクエスト
    response = requests.get(url, params=params, headers=headers)
    data = response.json()

    pages = data["query"]["pages"]
    for page_id, page in pages.items():
        imageinfo = page.get("imageinfo")
        if imageinfo:
            print("国旗画像URL:", imageinfo[0]["url"])
else:
    print("国旗画像のデータが辞書にありません。")