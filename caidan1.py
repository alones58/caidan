#!/usr/bin/python
import sqlite3
import random
import xlwt
conn = sqlite3.connect('caidan.db')

def qucai():
    cur = conn.cursor()
    cur.execute('select * from caidan')
    res = cur.fetchall()
    return (res)
    cur.close()

def hejijine():#定义合计金额
    a = qucai()
    b = random.randint(8, 28)  #  取得一个随机数
    slice = random.sample(a, b)  # 从list中随机获取b个元素，作为一个片断返回
    print("取到", slice)
    heji = 0
    for i in slice:
        jine = i[1]
        heji = heji + jine
    return (heji,slice,b)


jine = int(input())
while True:
    hj = hejijine()
    print("金额为：", hj[0])
    print("菜单为：", hj[1])
    if hj[0] > jine - 30 and hj[0] < jine:
        print(jine)
        break
book = xlwt.Workbook(encoding='utf-8', style_compression=0)
sheet = book.add_sheet('test', cell_overwrite_ok=True)

print("222", hj[1])
print("333", hj[1][1])
print("金额", hj[1][1][1])
print("菜名", hj[1][1][0])
i = 1

for i in range(hj[2]):
    print(i)
    print("5555", hj[1][i][0])
    sheet.write(i, 0, hj[1][i][0])
    sheet.write(i, 1, hj[1][i][1])
    i += 1



book.save(r'd:\菜单\菜单' + str(jine) + '.xls')
'''

'''