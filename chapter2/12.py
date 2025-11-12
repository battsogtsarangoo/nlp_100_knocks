import sys

def show_last_n_lines(filename, N):
   
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()  # ファイル全体をリストで読み込む
    for line in lines[-N:]:    # 末尾 N 行をスライス
        print(line, end='')

if __name__ == "__main__":
    filename = "/Users/sarangoobattsogt/nlp_100_knocks/chapter2/popular-names.txt"
    N = 10  
    show_last_n_lines(filename, N)
