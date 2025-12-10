from gensim.models import KeyedVectors

model_path = "GoogleNews-vectors-negative300.bin"
model = KeyedVectors.load_word2vec_format(model_path, binary=True)

similarity = model.similarity("United_States", "U.S.")
print("類似度:", similarity)
