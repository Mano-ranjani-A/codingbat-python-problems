'''

Given an "out" string length 4, such as "<<>>", and a word, return a new string where the word is in the middle of the out string, e.g. "<<word>>".

make_out_word('<<>>', 'Yay') → '<<Yay>>'
make_out_word('<<>>', 'WooHoo') → '<<WooHoo>>'
make_out_word('[[]]', 'word') → '[[word]]'

'''

# Function for make_out_word

def make_out_word(out, word):
    return(out[:2] + word + out[-2:])


# Calling make_out_word function with use cases

usecase_1 = make_out_word('<<>>', 'WooHoo')
usecase_2 = make_out_word('<<>>', 'Yay')
usecase_3 = make_out_word('[[]]', 'word')

# Printing all use-cases
print(usecase_1, usecase_2, usecase_3)