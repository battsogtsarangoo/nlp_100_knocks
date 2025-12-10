import pandas as pd
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram, linkage
import matplotlib.pyplot as plt
import numpy as np
from gensim.models import KeyedVectors


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


#  Ward法で階層クラスタリング用のリンクageを作成 
Z = linkage(X, method='ward')

#  デンドログラムを描画 
plt.figure(figsize=(12, 6))
dendrogram(Z, labels=countries, leaf_rotation=90)
plt.title("Hierarchical Clustering (Ward method)")
plt.xlabel("Country")
plt.ylabel("Distance")
plt.tight_layout()
plt.show()
