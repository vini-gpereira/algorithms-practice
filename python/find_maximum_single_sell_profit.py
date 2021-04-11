def find_buy_sell_stock_prices(array):
    buy = array[0]
    sell = array[1]
    maxProfit = sell - buy

    for i in range(1, len(array)):
        profit = array[i] - buy

        if profit > maxProfit:
            maxProfit = profit
            sell = array[i]

        if buy > array[i]:
            buy = array[i]
    
    return sell - maxProfit, sell

if __name__=="__main__":
    array = [8, 5, 12, 9, 19, 1]
    print(find_buy_sell_stock_prices(array))
    array = [21, 12, 11, 9, 6, 3]
    print(find_buy_sell_stock_prices(array))
    array = [21, 12, 11, 9, 6, 3]
    print(find_buy_sell_stock_prices(array))