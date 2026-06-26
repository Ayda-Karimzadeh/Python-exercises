# Add the missing items to the file

checklist = ["Portual", "Germany", "Spain"]

file_path = "D:\Python developer\Python-exercises\Personal-exercises\Add missing data\countries-missing.txt"
file_path2 = "D:\Python developer\Python-exercises\Personal-exercises\Add missing data\countries-missing-fixed.txt"

with open(file_path, "r") as file:
    content = file.readlines()

for item in checklist:
    content.append(item + "\n")

content = sorted(content)

with open(file_path2, "w") as file:
    file.writelines(content)
    

# checklist = [i + "\n" for i in checklist]

# with open(file_path, "r") as file:
#     content = file.readlines()

# updated_list = sorted(checklist + content)

# with open(file_path2, "w") as file:
#     for i in updated_list:
#         file.write(i)