def partition(N, before_file):
    # ファイルを開いて行をすべて読み込む
    with open(before_file, "r") as f1:
        lines = f1.readlines()

    # 1ファイルあたりの行数（余りがあれば最後のファイルに入る）
    total = len(lines) // N + (1 if len(lines) % N != 0 else 0)

    for i in range(N):
        start = i * total
        end = start + total
        extract = lines[start:end]

        if not extract:
            break  # 残りの行がなければ終了

        output_file = f"popular_names_{i+1}.txt"
        with open(output_file, "w") as f2:
            f2.writelines(extract)
        print(f"{output_file} を作成 ({len(extract)} 行)")

# 10分割
partition(10, "/Users/sarangoobattsogt/nlp_100_knocks/chapter2/popular-names.txt")
