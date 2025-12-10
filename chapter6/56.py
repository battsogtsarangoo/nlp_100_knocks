from gensim.models import KeyedVectors
import csv
from scipy.stats import spearmanr
import numpy as np

model = KeyedVectors.load_word2vec_format("GoogleNews-vectors-negative300.bin", binary = True)

csv_file = "./wordsim353/combined.csv"

word_pair = []
human_scores = []

with open(csv_file, 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        w1 = row["Word 1"]
        w2 = row["Word 2"]
        score = float(row["Human (mean)"])

        word_pair.append((w1, w2))
        human_scores.append(score)

model_scores = []

for w1, w2 in word_pair:
    model_scores.append(model.similarity(w1,w2))

human_scores = np.array(human_scores)
model_scores = np.array(model_scores)
rho, pval = spearmanr(human_scores, model_scores)

print("Spearman 相関係数 :", rho)
print("p-value:", pval)