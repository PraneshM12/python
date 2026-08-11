def max_profit(prices):
    min_price = prices[0]
    max_profit = 0

    for price in prices:

        if price < min_price:
            min_price = price

        profit = price - min_price

        if profit > max_profit:
            max_profit = profit

    return max_profit


# Input
prices = list(map(int, input("Enter stock prices: ").split()))

# Find maximum profit
result = max_profit(prices)

# Output
print("Maximum Profit:", result)