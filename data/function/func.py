from data.parametrs.get_data import get_result, list_words_1, id_1, list_words_2, id_2


letters_1 = []
letters_2 = []


def get_start():
    get_result('data/parametrs/data.db')

    for i in range(len(id_1) // 3):
        letter = str(list_words_1[0][i]) + ")" + " " + list_words_1[1][i]
        letters_1.append(letter)

    for i in range(len(id_2) // 3):
        letter = str(list_words_2[0][i]) + ")" + " " + list_words_2[1][i]
        letters_2.append(letter)


def read_the_token():
    with open('data/key/key.txt', 'r') as f:
        lines = f.readlines()
        return lines[0].strip()


