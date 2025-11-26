import spacy

nlp = spacy.load("ja_ginza")

text = """
メロスは激怒した。
必ず、かの邪智暴虐の王を除かなければならぬと決意した。
メロスには政治がわからぬ。
メロスは、村の牧人である。
笛を吹き、羊と遊んで暮して来た。
けれども邪悪に対しては、人一倍に敏感であった。
"""
doc = nlp(text)
noun_phrases = []

for token in doc:
    # token が名詞で、かつ head（支配語）が名詞で、依存関係が 'nmod'（名詞修飾）の場合
    if token.pos_ == "NOUN" and token.dep_ == "nmod" and token.head.pos_ == "NOUN":
        phrase = token.text + "の" + token.head.text
        noun_phrases.append(phrase)

print(noun_phrases)