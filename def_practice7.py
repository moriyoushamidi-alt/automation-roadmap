def is_long_password(password):
    if len(password) >8:
        return "strong"
    else:
        return "Too Short"

result= is_long_password("mypassword123")
print(result)
result2= is_long_password("abc")
print(result2)    