sales_w1 = [7,3,42,19,15,35,9]
sales_w2 = [12,4,26,10,7,28]
new_day = input('Enter sales for new day in week 2: ')
sales_w2.append(int(new_day))
sales = sales_w1 + sales_w2
best_day_sales_w1 = max(sales_w1) * 1.5
best_day_sales_w2 = max(sales_w2) * 1.5
best_day_sales = max(sales) * 1.5
worst_day_sales_w1 = min(sales_w1) * 1.5
worst_day_sales_w2 = min(sales_w2) * 1.5
worst_day_sales = min(sales) * 1.5
print('best sales week 1: $', best_day_sales_w1)
print('best sales week 2: $', best_day_sales_w2)
print('best sales overall: $', best_day_sales)
print('worst sales week 1: $', worst_day_sales_w1)
print('worst sales week 2: $', worst_day_sales_w2)
print('worst sales overall: $', worst_day_sales)



