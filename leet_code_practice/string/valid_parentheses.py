s = "([])()"

mapping = {')': '(', ']': '[', '}': '{','>':'<'}




def isvalid(s):
    if len(s)%2!=0:
        return False

    stack = []

    for c in s:
        if c in mapping.values():
            stack.append(c)
        elif c in mapping:
            if not stack or stack[-1]!=mapping[c]:
                return False
            stack.pop()
        else:
            return False
        
    return len(stack)==0


print(isvalid(s))

