lis = [6,4,1]
print(sorted(lis,reverse=True))
money = 8

def change(lis,money):
    lis.sort(reverse=True)
    val = 0
    result = []
    while money!=0:
        if lis[val]<=money:
            money-=lis[val]
            print(money)
            result.append(lis[val])
        else:
            val+=1

    return result

print(change(lis,money))
