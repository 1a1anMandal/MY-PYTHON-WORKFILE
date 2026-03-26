import re #Regular Expresson

email_condition=r"^[a-z]+[\]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
user_email=input(' Enter your Email : ')

if re.search(email_condition, user_email):
    print("Right Email")
else:
    print("Wrong Email")