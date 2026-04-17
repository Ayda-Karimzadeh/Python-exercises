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
# data1 = pandas.read_csv(io.StringIO(c.decode('utf-8')))
# data2 = pandas.read_csv("sampledata_x_2.txt")
# data12 = pandas.concat([data1, data2])
# data12.to_csv("sampledata12.txt", index=None)