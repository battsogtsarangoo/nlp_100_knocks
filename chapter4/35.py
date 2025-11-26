import spacy
from spacy import displacy

nlp = spacy.load("ja_ginza")

text = "メロスは激怒した。"

doc = nlp(text)

displacy.serve(doc, style="dep", auto_select_port=True)  # ブラウザで表示されます
