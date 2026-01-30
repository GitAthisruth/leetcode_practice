mm = ["eat","tea","tan","ate","nat","bat"]


def group_anagrams(mm):
    val = {}
    for word in mm:
        mmc = list(word)
        mmc.sort()
        mmc = "".join(mmc)
        if mmc not in val:
            val[mmc] = []
        val[mmc].append(word)
    return list(val.values())

print(group_anagrams(mm))


# from collections import defaultdict

# val = defaultdict(list)

# print(val)