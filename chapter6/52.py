from gensim.models import KeyedVectors

model_path = "GoogleNews-vectors-negative300.bin"
model = KeyedVectors.load_word2vec_format(model_path, binary=True)

results = model.most_similar("United_States", topn=10)

for word, score in results:
    print(word, score)
