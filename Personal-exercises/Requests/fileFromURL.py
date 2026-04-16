# Question: Print out the text of this file http://www.pythonhow.com/data/universe.txt. Please don't manually download the file. Let Python do all the work.

import requests

response = requests.get("http://www.pythonhow.com/data/universe.txt",headers={'user-agent': 'customUserAgent'}) #Header 'user-agent' ها اطلاعاتی هستند که به سرور می‌گویند درخواست از چه نوع کلاینتی آمده (مرورگر، ربات، اسکریپت و…).

print(response.text)