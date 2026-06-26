# Question: Create a script that uses the attached countries_by_area.txt file as data sourceand prints out the top 5 most densely populated countries

import pandas as pd

file_path = "D:\Python developer\Python-exercises\Personal-exercises\Pandas\Data Filter\countries-by-area.txt"

data = pd.read_csv(file_path)
data["density"] = data["population_2013"] / data["area_sqkm"]
data = data.sort_values(by="density", ascending=False)

for index, row in data[:5].iterrows():
    print(row["country"])

# We're using pandas to load the data as a dataframe and then calculate a density column in line 4. Then we use sort_values  to sort the data by density in descending order. Lastly, in the last two lines, we access the first 5 rows of the dataframe and iterate using iterrows