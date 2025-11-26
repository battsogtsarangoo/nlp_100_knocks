import gzip
import json
import re
import spacy
import math
from collections import Counter, defaultdict

# GiNZA 日本語モデル
nlp = spacy.load("ja_ginza")

# TF（日本の記事の名詞）
tf_counter = Counter()

# DF（文書頻度）
df_counter = defaultdict(int)

# 記事数
doc_count = 0

def chunks(text, size=3000):
    """SudachiPy の長文エラー対策"""
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

# ======= 全記事を読む =======
with gzip.open("jawiki-country.json.gz", "rt", encoding="utf-8") as f:
    for line in f:
        data = json.loads(line)
        title = data.get("title", "")
        text = clean(data.get("text", ""))

        doc_count += 1  # 記事数をカウント

        # DF のための一時セット（同じ記事で同じ名詞は1回だけ）
        appeared_words = set()

        # 長文を分割して解析
        for part in chunks(text):
            doc = nlp(part)
            for token in doc:
                if token.pos_ in ["NOUN", "PROPN"]:
                    appeared_words.add(token.lemma_)

        # DF（文書頻度）更新
        for word in appeared_words:
            df_counter[word] += 1

        # 日本の記事なら TF を作る
        if title == "日本":
            for part in chunks(text):
                doc = nlp(part)
                for token in doc:
                    if token.pos_ in ["NOUN", "PROPN"]:
                        tf_counter[token.lemma_] += 1

# ======= TF-IDF 計算 =======
results = []

for word, tf in tf_counter.items():
    df = df_counter[word]
    idf = math.log(doc_count / df)
    tfidf = tf * idf
    results.append((word, tf, df, idf, tfidf))

# TF-IDF 上位20語
results.sort(key=lambda x: x[4], reverse=True)

for word, tf, df, idf, tfidf in results[:20]:
    print(f"{word}\tTF={tf}\tDF={df}\tIDF={idf:.4f}\tTF-IDF={tfidf:.4f}")
