X = "paraparaparadise"
Y = "paragraph"

bigram_x = {X[i:i+2] for i in range(len(X)-1)}
bigram_y = {Y[i:i+2] for i in range(len(Y)-1)}

union = bigram_x | bigram_y  # 和集合
intersection = bigram_x & bigram_y  # 積集合
difference = bigram_x - bigram_y  # 差集合

print("Xのbi-gram:", bigram_x)
print("Yのbi-gram:", bigram_y)
print("和集合:", union)
print("積集合:", intersection)
print("差集合:", difference)

# 'se' が含まれるか確認
print("'se' in X:", 'se' in bigram_x)
print("'se' in Y:", 'se' in bigram_y)
