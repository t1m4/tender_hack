import json
import time

from django.db import connection
from openpyxl import load_workbook
from core.models import CTE, CTE_product, Contract, ContractCTE


def save_contract(filename):
    start_time = time.time()
    wb2 = load_workbook(filename)
    ws = wb2.active

    rows = ws.rows
    next(rows)
    k = 1
    contract_objects = []
    cte_objects = []
    contract_cte_objects = []
    contract_sql = """INSERT INTO core_contract (public_date, close_date, price, сustomer_inn, сustomer_kpp, customer_name, supplier_inn, supplier_kpp, supplier_name) VALUES\n"""
    # contract_sql = """INSERT INTO core_contract (public_date, close_date) VALUES\n"""
    for row in rows:
        if k % 10000 == 0:
            print(k)
            contract_sql = contract_sql.rstrip(",")
            contract_sql += ";"
            with connection.cursor() as cursor:
                cursor.execute(contract_sql)
            contract_sql = """INSERT INTO core_contract (public_date, close_date, price, сustomer_inn, сustomer_kpp, customer_name, supplier_inn, supplier_kpp, supplier_name) VALUES\n"""

        try:
            row_result = [i.value for i in row]
            row_result[-1] = json.loads(row_result[-1])
            contract_sql += """(TIMESTAMP '{}', TIMESTAMP '{}', '{}', {}, {}, '{}', {}, {}, '{}'),""".format(
                row_result[1].strftime("%Y-%m-%d %H:%M:%S"),
                row_result[2].strftime("%Y-%m-%d %H:%M:%S"),
                row_result[3] or 'null',
                row_result[4] or 'null',
                row_result[5] or 'null',
                row_result[6].replace("'", "") or 'null',
                row_result[7] or 'null',
                row_result[8] or 'null',
                row_result[9].replace("'", "") or 'null',
            )

        except Exception:
            print('error')
        k += 1
    contract_sql = contract_sql.rstrip(",")
    contract_sql += ";"
    with connection.cursor() as cursor:
        cursor.execute(contract_sql)

    print(time.time() - start_time)
