# create a script that let user type in a search term and opens and search on the browser for that term on Google

import webbrowser

query = input("Enter your Google query : ")
webbrowser.open_new("https://google.com/search?q=%s" %query)

# You need to first do a manual search on Google and observe how Google will construct the URL.
# Depending on where you are in the world the URL may be different, but the above URL should work everywhere.

# You will see that the URLcontains your search term at the end.
# Therefore, we concatenate the first part of the URLwith the search term we get from input.

