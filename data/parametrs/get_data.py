import sqlite3

id_1 = []
list_words_1 = [[], [], []]

id_2 = []
list_words_2 = [[], [], []]


def get_result(name):
    con = sqlite3.connect(name)

    cur = con.cursor()

    result_1 = cur.execute("""SELECT id,topic,url FROM year_1
 """).fetchall()
    result_2 = cur.execute("""SELECT id,topic,url FROM year_2""").fetchall()
    for elem in result_1:
        for i in elem:
            id_1.append(str(i))

    for i in id_1:
        if i.isdigit():
            list_words_1[0].append(i)
        elif 'https' in i:
            list_words_1[2].append(i)
        else:
            list_words_1[1].append(i)

    for elem in result_2:
        for i in elem:
            id_2.append(str(i))

    for i in id_2:
        if i.isdigit():
            list_words_2[0].append(i)
        elif 'https' in i:
            list_words_2[2].append(i)
        else:
            list_words_2[1].append(i)

    con.close()
