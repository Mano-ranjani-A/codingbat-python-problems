'''

The web is built with HTML strings like "<i>Yay</i>" which draws Yay as italic text. In this example, the "i" tag makes <i> and </i> which surround the word "Yay". Given tag and word strings, create the HTML string with tags around the word, e.g. "<i>Yay</i>".

make_tags('i', 'Yay') → '<i>Yay</i>'
make_tags('i', 'Hello') → '<i>Hello</i>'
make_tags('cite', 'Yay') → '<cite>Yay</cite>'

'''

# Function for make_tags

def make_tags(tag, word):
    return("<" + tag + ">" + word + "<" + "/" + tag + ">")

# Calling make_tags function with use cases

usecase_1 = make_tags('i', 'Yay')
usecase_2 = make_tags('i', 'Hello')
usecase_3 = make_tags('cite', 'Yay')

# Printing all use-cases
print(usecase_1, usecase_2, usecase_3)