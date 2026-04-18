import pandas as pd

df1 = pd.read_csv("https://pythonhow.com/data/sampledata.txt")
df2 = pd.read_csv("http://pythonhow.com/data/sampledata_x_2.txt")

df3 = pd.concat([df1, df2])

print(df3.to_csv("sampledata3.txt",index=None))


# import io
# import pandas
# import requests

# r = requests.get("http://www.pythonhow.com/data/sampledata.txt")
# c = r.content
# بایت خام با رمزگزاری utf-8 رمز گشایی میکنیم
#io.StringIO(...): رشته متنی را می‌گیرد و آن را مانند یک فایل متنی رفتار می‌کند
# data1 = pandas.read_csv(io.StringIO(c.decode('utf-8')))
# data2 = pandas.read_csv("sampledata_x_2.txt")
#ه طور پیش‌فرض، pandas.concat DataFrame ها را به صورت عمودی (ردیف به ردیف) به هم اضافه می‌کند.
# این بدان معناست که ردیف‌های data2 به انتهای ردیف‌های data1 اضافه می‌شوند.
# data12 = pandas.concat([data1, data2])
# index=None: این پارامتر مهم است. به Pandas می‌گوید که ایندکس DataFrame
# (اعداد ردیف پیش‌فرض که 0، 1، 2 و غیره هستند)را در فایل CSV به عنوان یک ستون جداگانه ننویسد.
# اگر این پارامتر وجود نداشت،
# یک ستون اضافی با ایندکس‌ها در فایل CSV شما ایجاد می‌شد.
# data12.to_csv("sampledata12.txt", index=None)