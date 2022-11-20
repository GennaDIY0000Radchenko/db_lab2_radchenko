import psycopg2
from python_coding._course_3.base.ac import *


def print_query(current_query):
    table = []
    for row in current_query:
        a = str(row).split(",")
        b = [c.replace("'", "")[1:].replace("Decimal(", "").replace(")", "").strip() for c in a]
        table.append(b)
    rows = len(table)
    cols = len(table[0])
    max_len = [max(len(table[q][w]) for q in range(rows)) for w in range(cols)]
    for i in range(rows):
        for j in range(cols):
            print(" " * (max_len[j] - len(table[i][j])) + f"{table[i][j].strip()}" + " | ", end="")
        print("")


def find_query_in_file_sql(dir, find="-- select"):
    f = open(dir)
    query_s = []
    add = False
    s = ""
    for r in f:
        if r.find(find) == 0:
            add = True
        if len(r) <= 2 and len(s) != 0 and add:
            add = False
            query_s.append(s.replace("-- ", ""))
            s = ""
        if add:
            s += r
    return query_s


# database = 'radchenko_DB'
database = "lab_2"
conn = psycopg2.connect(user=username, password=password, dbname=database)

with conn:
    cur = conn.cursor()
    print("Database opened successfully\n")

    # query_s = find_query_in_file_sql(
    #     "C:/Users/админ/OneDrive/Рабочий стол/КПІ/3 курс 1 семестр/База/lab_practice_04(25_10_2022).sql")
    query_s = find_query_in_file_sql(
        "C:/Users/админ/OneDrive/Рабочий стол/query.sql")

    i = 1
    for query in query_s:
        print(f"--- {i} ---", query, sep="\n", end="\n\n")
        cur.execute(query)
        print_query(cur)
        print("\n" + "-----"*35 + "\n")
        i += 1
