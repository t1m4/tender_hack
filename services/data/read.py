import json
import os
import time

from openpyxl import load_workbook
from pandas import read_excel, read_csv

from core.models import CTE


def read(filename):
    start_time = time.time()
    # result = read_excel(filename, engine='xlrd')
    result = read_excel(filename, engine='xlrd')
    # result = read_csv(filename)
    t = 0
    print(result)
    for row in result.iterrows():
        row_values = row[1].values
        print(row_values)
        # t += 1
        # time.sleep(1)
    print("End time",t,  time.time() - start_time)
    return



def read_cte(filename):
    start_time = time.time()
    wb2 = load_workbook(filename)
    ws = wb2.active

    rows = ws.rows
    next(rows)
    k = 1
    objects = []
    for row in rows:
        if k % 10000 == 0:
            print(k)
        try:
            row_result = [i.value for i in row]
            objects.append(CTE(cte_id=row_result[0], name=row_result[1], category=row_result[2], code_kphz=row_result[3]))
            if row_result[-1]:
                row_result[-1] = json.loads(row_result[-1])
        except:
            row_result = [i.value for i in row]

            print('something wrong with {}'.format(row), row_result)
        k += 1
    print(len(objects))

    print('2', time.time() - start_time)



if __name__ == '__main__':
    # print(read("Contract.xlsx"))
    # print(read_xsxl("Contract.xlsx"))
    # print(read_cte("CTE.xlsx"))
    print(read_cte("cte_test.xlsx"))
    # print(read_xsxl("cte_hard_test.xlsx"))
