# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.




# strs = ["f", "e", "fl", "flower", "flow", "flight"]

# if not strs:
#     print("")
# else:
#     min_word = min(strs, key=len) 
#     prefix = ""

#     for i in range(len(min_word)):
#         char = min_word[i]
#         if all(word[i] == char for word in strs):
#             prefix += char
#         else:
#             break

#     print(prefix)



# strs = ["flower","flow","flight"]
# if not strs:
#     print("")
# else:    
#     min_word = min(strs,key=len)
#     for i in range(len(min_word)+1):
#             if all(word[:i]==min_word[:i] for word in strs):
#                 output = "".join([min_word[:i]])
#             else:
#                 break
                
#     print(output)



strs = ["flower","flow","flight"]

min_word =  min(strs,key=len)

# print(min_word)

if not strs:
    print("")
else:
    for i in range(len(min_word)):
        if all(word[:i]==min_word[:i] for word in strs):
            # output = "".join([min_word[:i]])
            output = min_word[:i]
        else:
            break

print(output)


