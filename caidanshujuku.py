#!/usr/bin/python
import random
import sqlite3
conn = sqlite3.connect('caidan.db')

def qucai():
    cur = conn.cursor()
    cur.execute('select * from caidan')
    res = cur.fetchall()
    return (res)
    cur.close()

def hejijine():
    a = qucai()
    heji = 0
    for i in a:
        jine = i[1]
        heji = heji + jine
    return (heji)
a = qucai()
hj = hejijine()
while hj > 154:
    b = random.randint(0, 1)
    print("duole")
    print("将要删除：", a[b])
    d = a[b]
    hj = hj - d[1]
    del a[b]
    print("现在的金额是：", hj,"现在菜单里有：",a)

print("shaole")


