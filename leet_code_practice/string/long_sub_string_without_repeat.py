s = "abcddya"


def lcs(s):
    sub = ""
    if not s:
        return 0
    if s.isspace() and len(s) == 1:
            return 1
    val = []
    for i in s:
        if i not in sub:
             sub+=i
        else:
             val.append(sub)
             idx = sub.index(i)
             sub = sub[idx+1:]+i

    val.append(sub)   
  
    return len(max(val,key = len))
    



# print(lcs(s))



def lcs_pointer(s):
    seen = set()
    left = 0
    max_len = 0

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1

        seen.add(s[right])
        max_len = max(max_len, right - left + 1)

    return max_len
print(lcs_pointer(s))

