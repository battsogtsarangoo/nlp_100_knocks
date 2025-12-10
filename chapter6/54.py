from gensim.models import KeyedVectors

# GoogleNews Word2Vec の読み込み
model = KeyedVectors.load_word2vec_format(
    "GoogleNews-vectors-negative300.bin",
    binary=True
)

# アナロジー評価データ
file_path = "questions-words.txt"

results = []

section = ""   # ← これが必要！

with open(file_path, "r") as f:
    for line in f:
        line = line.strip()

        # セクション開始
        if line.startswith(":"):
            section = line[2:].strip()
            continue

        # capital-common-countries 以外は無視
        if section != "capital-common-countries":
            continue

        # 行を分割（A B C D）
        A, B, C, D = line.split()
        
        # vec(B) - vec(A) + vec(C)
        vec = model[B] - model[A] + model[C]

        # 最も類似する単語を取得
        predicted_word, similarity = model.similar_by_vector(vec, topn=1)[0]

        # 記録
        results.append({
            "A": A,
            "B": B,
            "C": C,
            "Correct(D)": D,
            "Predicted": predicted_word,
            "Similarity": similarity
        })

# 結果表示
for r in results:
    print(f"{r['A']} {r['B']} {r['C']} {r['Correct(D)']}  ->  {r['Predicted']}  ({r['Similarity']:.4f})")
