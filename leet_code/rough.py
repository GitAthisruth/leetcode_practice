price = [7,1,5,3,6,4,10]
val = price[0]
profit = 0
for i in range(1,len(price)):
    if val>price[i]:
        val = price[i]
    elif price[i]-val>profit:
        profit = price[i]-val

print(profit)