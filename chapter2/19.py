filename = "/Users/sarangoobattsogt/nlp_100_knocks/chapter2/popular-names.txt"
output_file = "sorted_by_third_column.txt"

# ファイルを読み込み、各行をリストに格納
with open(filename, "r") as f:
    lines = [line.strip() for line in f]

# 3列目の数値で降順にソート
# タブ区切りで 3列目は index 2
lines_sorted = sorted(lines, key=lambda x: int(x.split("\t")[2]), reverse=True)

# 結果を別ファイルに書き出す
with open(output_file, "w") as f:
    for line in lines_sorted:
        f.write(line + "\n")

print(output_file)

