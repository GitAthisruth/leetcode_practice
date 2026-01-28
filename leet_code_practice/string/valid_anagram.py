s = "anagram"
t = "nagaram"


def vali_anagram(s,t):
    flag = False
    s = list(s)
    t = list(t)
    s.sort()
    t.sort()

    s = "".join(s)
    t = "".join(t)
    if s == t:
        flag = True

    return flag
   

print(vali_anagram(s,t))

    
    
     