import spacy

# GiNZA 日本語モデルをロード
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
predicates = []

for token in doc:
    # 主語が「メロス」のとき
    if token.dep_ == "nsubj" and token.text == "メロス":
        predicate = token.head.text  # 述語を取得
        if predicate not in predicates:
            predicates.append(predicate)

print(predicates)
