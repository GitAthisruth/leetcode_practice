s = "rat"
t = "cart"


def valid_anagram(s,t):
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
   

# print(valid_anagram(s,t))



def val_ana(s,t):
    if len(s)!=len(t):
        return False

    s_d = {}
    t_d = {}
    for i in s:
        s_d[i] = s_d.get(i,0)+1
    for j in t:
        t_d[j] = t_d.get(j,0)+1

    return s_d==t_d




print(val_ana(s,t))






def isAnagram(s, t):
       
        flag = False
        if len(s)!=len(t):
            return flag
        s_d = {}
        t_d = {}
        for i in s:
            s_d[i] = s_d.get(i,0)+1
        for j in t:
            t_d[j] = t_d.get(j,0)+1

        count = 0
        for key in s_d:
            if key in t_d:
                if s_d[key] == t_d[key]:
                    count+=1
                    if count==len(s_d):
                        flag = True


        return flag
    

print(isAnagram(s,t))
    
     