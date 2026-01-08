# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5.

# method 1

prices = [7,1,5,3,6,4,2,10]

def bst(prices):
    val = 0
    l = 0
    for r in range(1,len(prices)):
        if prices[r]<prices[l]:
            l=r
        else:
            val = max(val,prices[r]-prices[l])
    return val

print(bst(prices))



