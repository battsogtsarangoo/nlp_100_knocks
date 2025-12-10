import numpy as np
import pandas as pd
from gensim.models import KeyedVectors
from sklearn.cluster import KMeans

# 1. Word2Vecモデルのロード
model = KeyedVectors.load_word2vec_format(
    "GoogleNews-vectors-negative300.bin", binary=True
)
# 2. questions-words.txt から国名抽出
with open("countries.txt", "r") as f:
    # countries.txtの国名が入っているので取り出す
    countries = f.read().split("\n")



# Word2Vec に存在する国名だけを残す
countries = [c for c in countries if c in model.key_to_index]

# 3. 国名のベクトルを取得

country_vectors = [model[c] for c in countries]

# numpy 形式へ
X = np.array(country_vectors)


# 4. k-means クラスタリング(k=5)
kmeans = KMeans(n_clusters=5, random_state=0)
labels = kmeans.fit_predict(X)

# 5. クラスタごとに表示
result = {i: [] for i in range(5)}

for country, label in zip(countries, labels):
    result[label].append(country)

for k, v in result.items():
    print(f"=== Cluster {k+1} ===")
    for country in v:
        print("  ", country)
    print(f"Total: {len(v)}\n")
