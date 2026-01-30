s = "AABABBA"
k = 1
#window 
def character_replacement(s,k):
    left = 0
    max_fre = 0
    result = 0
    freq = {}
    #we will get the max same array by replacing by finding , window_size = (right-left+1),max_freq 
    # replacement_needed = window_size - max_frq
    for right in range(len(s)):
        freq[s[right]] = freq.get(s[right],0)+1
        max_fre = max(max_fre,freq[s[right]])

        while (right-left+1)-max_fre>k:
            freq[s[left]]-=1
            left+=1

        result = max(result,right-left+1)

    return result

print(character_replacement(s,k))

