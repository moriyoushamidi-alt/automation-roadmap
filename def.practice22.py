def finance (payment):
    if payment >= 0:
        return "posetive"
    else:
        return "negetive"
result = finance(500)
print(result)

result2 = finance(-200)
print(result2)
