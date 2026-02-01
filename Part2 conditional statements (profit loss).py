org_price = int(input("enter a number:"))
sell_price = int(input("enter a number:"))

loss = org_price > sell_price
if sell_price >org_price:
    profit = sell_price - org_price 
    print("The seller has made a profit of", profit)

else:
    print("The seller has made a loss")