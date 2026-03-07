def advanced_word_counter(filepath):
    with open(filepath,"r") as file:
            text = file.read()
    text = text.replace(","," ")
    string_list = text.split(" ")
    return len(string_list)

print(advanced_word_counter("D:/Python developer/Python-exercises/Personal-exercises/advanced word counter/word.txt"))

# import re

# def count_words_re(filepath):
#     with open(filepath, 'r') as file:
#         text = file.read()
#     string_list = re.split(",| ", text)
#     return len(string_list)

# print(count_words_re("D:/Python developer/Python-exercises/Personal-exercises/advanced word counter/word.txt"))

# This alternative solution uses the built-in re  module, which provides regular expression matching operations. We're using the split method of that module, and the expression ",| " is meant to replace commas with spaces. Using methods from the re  module can be more appropriate than Python built-in methods when string operations are complicated. However, for this simple scenario, the re  module could be skipped.