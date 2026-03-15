import json
with open("company1.json", "r+") as file:
    d = json.loads(file.read())
    d["employees"].append(dict(firstName = "Ayda", lastName = "Karimzadeh"))
    file.seek(0)
    json.dump(d, file, indent=4, sort_keys=True)
    file.truncate()

    # r+ means in both read and write mode 
    # the string of file.read() is converted to dict by json.loads()
    # #file.seek(0) is put the cursor to the top of the file.
    #  when you read a file the cursor goes to the end of it.
    # sort_keys=True means that the string that will be written in the json file,
    #  will have the same order as the dictionary.
    # file.truncate() will delete everything under the cursor