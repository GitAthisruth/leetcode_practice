s = "aaa"

#Brute force method 

def  palindromic_substrings(s):
    val  = []
    for i in range(len(s)):
        for j in range(i,len(s)):
            sn = s[i:j+1]
            if sn == sn[::-1]:
                val.append(sn)
    return val



def pald(s):
    dd = 0
    n= len(s)
    def con(l,r):
        count = 0
        while l>=0 and r<n and s[l] == s[r]:
            count+=1
            l-=1
            r+=1
        return count


    for i in range(n):
        dd += con(i,i)
        dd += con(i,i+1)
    return dd

print(pald(s))