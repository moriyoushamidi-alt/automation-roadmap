def get_discount(price, percent):
    return f"{price-(price*percent/100)}"
result= get_discount(200, 25)
print(result)