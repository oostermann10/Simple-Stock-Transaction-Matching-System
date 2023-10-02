def match_stock(buy_orders, sell_orders):

    transactions = []  # the list for storing if we find a match

    # we should have for efficiency:
    # the buys should be in descending order by price
    # the sells should be in ascending order by price

    buy_orders.sort(key=lambda x: x['price'], reverse=True)
    sell_orders.sort(key=lambda x: x['price'])
    
    if len(buy_orders) == 0 or len(sell_orders) == 0: 
        return "NO TRANSACTIONS CAN BE MADE"

    for i in range(len(buy_orders)):
        for j in range(len(sell_orders)):
            ticker_buy = buy_orders[i]['ticker']
            ticker_sell = sell_orders[j]['ticker']
            quantity_buy = buy_orders[i]['quantity']
            quantity_sell = sell_orders[j]['quantity']
            price_buy = buy_orders[i]['price']
            price_sell = sell_orders[j]['price']

            if quantity_buy != 0 and quantity_sell != 0:
                # if the its equal to zero then we skip either the buy or the sell
                # we can't make a transaction here
                if ticker_buy == ticker_sell and price_buy >= price_sell:
                    # then we have a match
                    matched_units = min(quantity_buy, quantity_sell)
                    buy_orders[i]['quantity'] -= matched_units
                    sell_orders[j]['quantity'] -= matched_units

                    # if there is a match then we create a dictionary
                    a_transaction = {
                        'ticker': ticker_buy,
                        'buy': price_buy,
                        'sell': price_sell,
                        'quantity': matched_units
                    }

                    transactions.append(a_transaction)
    return transactions


buy_orders = [
    {'ticker': 'AAPL', 'price': 150, 'quantity': 10},
    {'ticker': 'AAPL', 'price': 160, 'quantity': 5},
]

sell_orders = [
    {'ticker': 'AAPL', 'price': 155, 'quantity': 7},
    {'ticker': 'AAPL', 'price': 165, 'quantity': 5},
]

transactions = match_stock(buy_orders, sell_orders)
print(transactions)


