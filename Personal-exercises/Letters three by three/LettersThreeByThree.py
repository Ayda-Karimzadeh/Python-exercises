# import string

# with open("mynewfile.txt","w") as f:
#     for i,j,k in zip(string.ascii_lowercase[0::3],string.ascii_lowercase[1::3],string.ascii_lowercase[2::3]):
#         f.write(i+j+k+"\n")

import string

letters = string.ascii_lowercase + " "

slice1 = letters[0::3]
slice2 = letters[1::3]
slice3 = letters[2::3]

with open("letters.txt", "w") as file:
    for s1, s2, s3 in zip(slice1, slice2, slice3):
        file.write(s1 + s2 + s3 + "\n")

# we are adding one white space to ascii_lowercase  so that we get a string of 27 items instead of 26 that ascii_lowercase  provides. By slicingascii_lowercase we would get two slices with a length of 9 and one slice with a length of 8. 
# That means the iteration would stop at the shortest slice, so letters y and z wouldn't be written in the file. That's why we add a white space, so we get three slices, each with a length of 9. That means we get 9 iterations and not 8 as we would get with the original ascii_lowercase  string. The 9th iteration would write letters y and z in the file.
