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

print("係り元|係り先|依存関係")

for token in doc:
     head = token.head # 係り先の単語
     print(f"{token.text}|{head.text}|{token.dep_}")