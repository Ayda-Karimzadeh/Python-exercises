import random

charecters = "0123456789qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM@#$%&*!?()^"

password = "".join(random.sample(charecters, 6))
print(password)
