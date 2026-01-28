s = "0P"
def isp(s):
    a = []
    for i in s.lower():
        if i.isalnum():
            a.append(i)
    a = "".join(a)
    if a == a[::-1]:
        return True
    return False
print(isp(s))

