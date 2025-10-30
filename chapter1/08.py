def cipher(s):
    result = ""
    for i in range(len(s)):
        if s[i].isalpha() and s[i].islower():
            result += chr(219 - ord(s[i]))
        else:
            result +=s[i]
    return result
        

s = "Battsogt SARANGoo"
print(cipher(s))
