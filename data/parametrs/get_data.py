import sqlite3

list_1 = []
global list_2, word
list_2 = []
list_3 = []



def get_result(name):
    con = sqlite3.connect(name)

    cur = con.cursor()

    result_2 = []
    result_1 = cur.execute("""SELECT id FROM main
 """).fetchall()
    result_2.append(cur.execute("""SELECT topic FROM main
    """).fetchall())
    result_3 = (cur.execute("""SELECT year FROM main
 """).fetchall())

    for elem in result_1:
        for i in range(len(elem)):
            list_1.append(elem[0])
            # print(list_1)

    for elem in result_2:
        for i in range(len(elem)):
            a = ','.join(elem[i])
            list_2.append(a)
            # print(list_2)

    for elem in result_3:
        for i in range(len(elem)):
            list_3.append(str(elem[0]))
            # print(list_3)

    con.close()
