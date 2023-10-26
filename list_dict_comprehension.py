import pandas

alphabet = pandas.read_csv('nato_phonetic_alphabet.csv')

nato_data_frame = pandas.DataFrame(alphabet)

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

alpha_dict = {row.letter: row.code for (index, row) in nato_data_frame.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

code_word = input('What is your code word: ').upper()

code_word_letters = [w for w in code_word]

nato_code = [alpha_dict[w] for w in code_word_letters if w in alpha_dict]

print(nato_code)
