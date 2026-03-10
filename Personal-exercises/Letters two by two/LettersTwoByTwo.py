import string

with open("newfile.txt","w") as f:
    for i,j in zip(string.ascii_lowercase[0::2],string.ascii_lowercase[1::2]):
        f.write(f"{i}{j}\n")
        # f.write(i+j+"\n")
    f.close()