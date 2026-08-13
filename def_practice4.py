def check_age(age):
    if age > 18:
        return "Adult"
    else:
        return "Minor"

result= check_age (19)
print(result)

result2= check_age (17)
print(result2)
