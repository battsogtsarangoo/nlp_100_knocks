import gzip
import json
import re
import spacy
from collections import Counter
import matplotlib.pyplot as plt

# GiNZA 日本語モデル
nlp = spacy.load("ja_ginza")

word_counter = Counter()

def chunks(text, size=3000):
    """Sudachi の tokenization エラー回避"""
    for i in range(0, len(text), size):
        yield text[i:i+size]

def clean(text):
    # Wikipedia 特有の記法を削除
    text = re.sub(r"\{\{.*?\}\}", " ", text, flags=re.DOTALL)
    text = re.sub(r"\[\[.*?\]\]", " ", text)
    text = re.sub(r"<.*?>", " ", text)
    text = re.sub(r"==.*?==", " ", text)

    # テンプレートの残り「|」「}}」を削除
    text = re.sub(r'[|}%"]', " ", text)
    return text

# ====== 全記事から名詞カウント ======
with gzip.open("jawiki-country.json.gz", "rt", encoding="utf-8") as f:
    for line in f:
        data = json.loads(line)
        text = clean(data.get("text", ""))

        for part in chunks(text):
            doc = nlp(part)
            for token in doc:
                if token.pos_ in ["NOUN", "PROPN"]:
                    word_counter[token.lemma_] += 1

# 頻度順にソート
freqs = [freq for word, freq in word_counter.most_common()]

# ====== 両対数グラフ ======
plt.figure(figsize=(8, 6))
plt.loglog(range(1, len(freqs) + 1), freqs)
plt.xlabel("Rank (順位)")
plt.ylabel("Frequency (出現頻度)")
plt.title("Zipf's Law (Wikipedia)")
plt.grid(True)
plt.show()
