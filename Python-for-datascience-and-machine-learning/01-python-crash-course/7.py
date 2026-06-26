# ** Create a function that grabs the email website domain from a string in the form: **

# user@domain.com
# So for example, passing "user@domain.com" would return: domain.com

# import re
# def domainGet(email):
#     a = re.search(r"@(.+)$",email)
#     if a:
#         print(a.group(1))

def domainGet(email):
    return email.split('@')[-1]

domainGet('user@domain.com')