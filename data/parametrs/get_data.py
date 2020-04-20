import sqlite3

id = []
list_words = [[], [], []]

topics_1 = []
url_1 = []


def get_result(name):
    con = sqlite3.connect(name)

    cur = con.cursor()

    result_1 = cur.execute("""SELECT id,topic,url FROM year_1
 """).fetchall()
    for elem in result_1:
        for i in elem:
            id.append(str(i))

    for i in id:
        if i.isdigit():
            list_words[0].append(i)
        elif 'https' in i:
            list_words[2].append(i)
        else:
            list_words[1].append(i)

    con.close()
