import os
from openpyxl import load_workbook



module_dir = os.path.dirname(__file__)
excel_file = os.path.join(module_dir, 'resources/excel/practice.xlsx')

wb2 = load_workbook(excel_file, data_only=True)
ws = wb2["Page1"]
rows = ws.rows
next(rows)

stud = []

for row in rows:
    if row[1].value != None:
        print('a ', row[1].value)
        tmp = []
        for i in range(13):
            tmp.append(row[i].value)
        stud.append(tmp)
        for cell in row:
            a = cell.value
            print('b', a)

for i in range(len(stud)):
    print(stud[i])


