s = "babad"
#brute force method .
def lps(s):
    val = []
    n =""
    len_ = 0
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            pal = s[i:j+1]
            val.append(pal)

    for i in val:
        if i==i[::-1] and len(i)>len_:
            len_=len(i)
            n = i
    return n

# print(lps(s))


def lps1(s):
    res = ""
    def expand(l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]   # last valid palindrome
    
    for i in range(len(s)):
        # odd length palindrome
        p1 = expand(i, i)
        # even length palindrome
        p2 = expand(i, i+1)
        
        if len(p1) > len(res):
            res = p1
        if len(p2) > len(res):
            res = p2
    
    return res


print(lps1(s))

