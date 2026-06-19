# Question: Please download the attached countries-raw.txt file. The file contains the list of country names, but it also contains some unnecessary text among the countries. 

# Please clean the list with Python by generating a new text file that contains a flawless list of country names without any other text or brake lines in it. The new file content should look like in the expected output.
file_path = 'D:/Python developer/Python-exercises/Personal-exercises/Data Cleaner/countries-raw.txt'
# cleaned_countries = []
# with open(file_path, 'r') as file:
#     for line in file:
#         line = line.strip()

#         if line == "":
#             continue

#         if line == "Top of Page":
#             continue

#         if len(line) == 1 and line.isalpha():
#             continue

#         cleaned_countries.append(line)

# with open('D:/Python developer/Python-exercises/Personal-exercises/Data Cleaner/countries-cleaned.txt', 'w') as file:
#     for country in cleaned_countries:
#         file.write(country + '\n')

with open(file_path, 'r') as file:
    content = file.readlines()

content = [i.strip("\n") for i in content if "\n " in i]
content = [i for i in content if i != ""]
content = [i for i in content if i != "Top of Page"]
content = [i for i in content if len(i) != 1]

with open (file_path, "w") as file:
    for i in content:
        file.write(i + "\n")