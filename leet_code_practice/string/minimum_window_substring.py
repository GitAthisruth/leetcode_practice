from collections import Counter


s = "ABAC"
t = "ABC"


def minWindow(s,t):
    if not t or not s:
        return ""
    
    t_count =Counter(t)
    val = []
    for i in range(len(s)):
        for j in range(i,len(s)):
            sub = s[i:j+1]
            print(sub)
            s_count= Counter(sub)
            if all(s_count[i]>=t_count[i] for i in t_count):
                val.append(sub)

    if not val:
        return "" 

    return min(val,key=len)


# print(minWindow(s,t))


#Learn the code .

def minWindow(s, t):
    if not s or not t:
        return ""

    t_count = Counter(t)
    window = {}

    need = len(t_count)
    have = 0

    res = [-1, -1]
    res_len = float("inf")

    left = 0
    for right in range(len(s)):
        c = s[right]
        window[c] = window.get(c, 0) + 1
        print(f"right={right}, left={left}, c={c}, window={window} , t_count={t_count}")

        if c in t_count and window[c] == t_count[c]:
            have += 1
            

        # try to shrink
        while have == need:
            if (right - left + 1) < res_len:
                res = [left, right]
                res_len = right - left + 1

            window[s[left]] -= 1
            print("window",window)
            if s[left] in t_count and window[s[left]] < t_count[s[left]]:
                have -= 1
            left += 1

    l, r = res
    return s[l:r+1] if res_len != float("inf") else ""

print(minWindow(s,t))





