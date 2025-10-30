s = "I am an NLPer"
trigrams = [s[i:i+3] for i in range(len(s)-2)]
print(",".join(trigrams))
words = s.split()
bigrams = [[words[i],words[i+1]] for i in range(len(words)-1)]
print(bigrams)
