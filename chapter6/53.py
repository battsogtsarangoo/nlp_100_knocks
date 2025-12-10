from gensim.models import KeyedVectors

path_model = "GoogleNews-vectors-negative300.bin"
model = KeyedVectors.load_word2vec_format(path_model, binary = True)

result = model.most_similar(positive = ['Spain', 'Athens'], negative = ['Madrid'], topn = 10)

for word, score in result:
    print(word, score)