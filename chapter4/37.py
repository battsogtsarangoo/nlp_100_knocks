import gzip
import json
import re
import spacy
from collections import Counter

nlp = spacy.load("ja_ginza")
noun_counter = Counter()

def clean_text(text):
    # Wikipedia 特有の記法を削除
    text = re.sub(r"\{\{.*?\}\}", " ", text, flags=re.DOTALL)
    text = re.sub(r"\[\[.*?\]\]", " ", text)
    text = re.sub(r"<.*?>", " ", text)
    text = re.sub(r"==.*?==", " ", text)

    # テンプレートの残り「|」「}}」を削除
    text = re.sub(r'[|}%"]', " ", text)
    return text

def chunks(text, size=3000):
    for i in range(0, len(text), size):
        yield text[i:i+size]

with gzip.open("jawiki-country.json.gz", "rt", encoding="utf-8") as f:
    for line in f:
        data = json.loads(line)
        text = clean_text(data.get("text", ""))

        for part in chunks(text):
            doc = nlp(part)
            for token in doc:
                if token.pos_ in ["NOUN", "PROPN"]:
                    noun_counter[token.lemma_] += 1

# 上位20語
for w, c in noun_counter.most_common(20):
    print(w, c)
