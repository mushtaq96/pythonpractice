

def stockpicker(stock_prices):
    if len(stock_prices)<0:
        raise ValueError('require atleast 2 prices')

    min_price = stock_prices[0]
    max_profit = stock_prices[1] - stock_prices[0]
    
    for current_time in range(1, len(stock_prices)):

        current_price = stock_prices[current_time]

        potential_profit = current_price - min_price 
        
        max_profit = max(max_profit, potential_profit)

        min_price = min(min_price, current_price)

    print(max_profit)


list1 = [10,13,4,5,9]
#list2 = input('enter the list of elements separated by space')
#list2 = list2.split()

profit = stockpicker(list1)


