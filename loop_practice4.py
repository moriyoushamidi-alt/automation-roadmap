daily_sales = [340, 890, 120, 560, 780, 230, 950, 410]

highest = 0
for sale in daily_sales:
    if sale>highest:
        highest = sale

print(highest)        