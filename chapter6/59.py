import numpy as np
import pandas as pd
from gensim.models import KeyedVectors
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

# 1. Word2Vecモデルのロード
model = KeyedVectors.load_word2vec_format(
    "GoogleNews-vectors-negative300.bin", binary=True
)

# 2. 国名リストのロード
with open("countries.txt", "r") as f:
    countries = f.read().split("\n")

# 3. Word2Vec に存在する国名だけ残す
countries = [c for c in countries if c in model.key_to_index]

# 4. 国名ベクトル取得
vectors = np.array([model[c] for c in countries])

# 5. t-SNE で 300次元 → 2次元に圧縮
tsne = TSNE(n_components=2, random_state=42, perplexity=30, learning_rate='auto')
tsne_results = tsne.fit_transform(vectors)

# 6. 散布図で可視化
plt.figure(figsize=(14, 10))
plt.scatter(tsne_results[:, 0], tsne_results[:, 1])

# 7. 各点に国名を表示
for i, country in enumerate(countries):
    plt.annotate(country, (tsne_results[i, 0], tsne_results[i, 1]))

plt.title("t-SNE Visualization of Country Word Vectors")
plt.xlabel("Dimension 1")
plt.ylabel("Dimension 2")
plt.grid(True)
plt.show()
