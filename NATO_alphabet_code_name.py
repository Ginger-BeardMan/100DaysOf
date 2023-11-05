import pandas

alphabet = pandas.read_csv('nato_phonetic_alphabet.csv')

nato_data_frame = pandas.DataFrame(alphabet)

# Create a dictionary of code names:
# {"A": "Alfa", "B": "Bravo"}

alpha_dict = {row.letter: row.code for (index, row) in nato_data_frame.iterrows()}

# Create a list of the phonetic code words from a word that the user inputs.

def generate_phonetic():
    code_word = input('What is your code word: ').upper()

    try:
        nato_code = [alpha_dict[w] for w in code_word]
    except KeyError:
        print('Sorry, only letters in the alphabet please')
        generate_phonetic()
    else:
        print(nato_code)


generate_phonetic()
