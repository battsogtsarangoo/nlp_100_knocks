sentence = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
sentence = sentence.replace(".", "")
words = sentence.split()
index1 = [1,5,6,7,8,9,15,16,19]
result = {}
for i in range(len(words)):
    if i+1 in index1:
        key = words[i][0]
    else:
        key = words[i][0:2]
    result[key]= i+1

print(result)    

