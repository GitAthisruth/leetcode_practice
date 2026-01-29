strs = ["flower","flow","flight"]

def lcp(strs):
    min_w = min(strs,key=len)
    prefix = ""
    for i in range(len(min_w)):
        char = min_w[i]
        if all(word[i]== char for word in strs):
            prefix+=char
        else:
            break
    return prefix

print(lcp(strs))
