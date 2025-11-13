# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.


prices = [7,6,4,3,1,15]
profit = 0
for i in range(len(prices)-1):
    for j in range(i+1,len(prices)):
        # print(f"i:{i} and j:{j}")
        # print(f"profit:{profit}")
        if prices[i]<prices[j] and abs(prices[i] - prices[j]) > profit:
            # print(f"i:{prices[i]} and j:{prices[j]}")
            # print(profit)
            profit = abs(prices[i] - prices[j])

print(profit)


# print(7 - 1)


#Best solution

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = float('inf')   # Track lowest price seen so far
        max_profit = 0             # Track best profit
        
        for price in prices:
            # If current price is lower, update min_price
            if price < min_price:
                min_price = price
            # Otherwise, check if selling today is better
            elif price - min_price > max_profit:
                max_profit = price - min_price
                
        return max_profit



#Bad method 

prices = [7,1,5,3,6,4]

min_price = min(prices)
min_price_index = prices.index(min_price)

# print(min_price_index)
max_price = 0

for i in range(min_price_index+1,len(prices)):
    print(prices[i],i,i-prices[min_price_index])
    if prices[i]>prices[min_price_index] and (prices[i]-prices[min_price_index])>max_price:
        max_price = prices[i]-prices[min_price_index]

print(max_price)