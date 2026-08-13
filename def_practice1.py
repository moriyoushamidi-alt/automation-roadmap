def check_status (code):

   if code==200:
      return "success"
   else:
      return f"failed with code {code}"
result=check_status(200)
print(result)

result2=check_status(404)
print(result2)