import gzip
import json
import re
import spacy
from collections import Counter

nlp = spacy.load("ja_ginza")
noun_counter = Counter()

def chunks(text, size=3000):
    for i in range(0, len(text), size):
        yield text[i:i+size]

def clean_markup(text):
    # テンプレート除去
    text = re.sub(r'\{\{[^{}]*\}\}', ' ', text)
    # [[]]除去
    text = re.sub(r'\[\[[^\[\]]*\]\]', ' ', text)
    # 見出し除去
    text = re.sub(r'==+[^=]+==+', ' ', text)
    # <tag>除去
    text = re.sub(r'<[^>]+>', ' ', text)
    # 記号の連続除去
    text = re.sub(r'[|{}=%]', ' ', text)
    # 改行→スペース
    text = text.replace("\n", " ")
    return text

with gzip.open("jawiki-country.json.gz", "rt", encoding="utf-8") as f:
    for line in f:
        data = json.loads(line)
        text = clean_markup(data.get("text", ""))

        for part in chunks(text):
            doc = nlp(part)
            for token in doc:
                # 名詞かつ、意味のある語だけ
                if token.pos_ in ["NOUN", "PROPN"]:
                    lemma = token.lemma_.strip()

                    # 空・数字のみ・記号のみを除外
                    if not lemma:
                        continue
                    if re.fullmatch(r'[\d.]+', lemma):
                        continue
                    if re.fullmatch(r'[^\wぁ-んァ-ン一-龥]+', lemma):
                        continue

                    # 頻出だけど意味の薄い名詞（除外したい場合）
                    if lemma in ["こと", "ため", "よう"]:
                        continue

                    noun_counter[lemma] += 1

# Top20
for word, freq in noun_counter.most_common(20):
    print(word, freq)
