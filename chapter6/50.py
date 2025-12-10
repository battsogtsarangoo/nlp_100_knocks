from gensim.models import KeyedVectors

# Google News の学習済みモデルを読み込む
model_path = "GoogleNews-vectors-negative300.bin"
model = KeyedVectors.load_word2vec_format(model_path, binary=True)

# “United States” は "United_States" という表記
word = "United_States"

# ベクトルの取得
vector = model[word]

print(f"Vector for '{word}':")
print(vector)
print("次元数:", len(vector))
