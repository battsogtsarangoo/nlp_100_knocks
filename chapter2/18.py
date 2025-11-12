import sys
from collections import Counter

filename = "/Users/sarangoobattsogt/nlp_100_knocks/chapter2/popular-names.txt"

def main():
    with open(filename, "r", encoding="utf-8") as f:
        # 各行の1列目を取得
        col1_list = [line.strip().split("\t")[0] for line in f]
         # 出現頻度をカウント
    counter = Counter(col1_list)

    # 出現頻度の多い順にソートして表示
    for name, freq in counter.most_common():
        print(freq, name)

if __name__ == "__main__":
    main()