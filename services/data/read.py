import json
import time

from openpyxl import load_workbook

from core.models import CTE, CTE_product


def read_cte(filename):
    start_time = time.time()
    wb2 = load_workbook(filename)
    ws = wb2.active

    rows = ws.rows
    next(rows)
    k = 1
    cte_objects = []
    cte_product_objects = []
    for row in rows:
        cte_product_objects = []
        if k % 10000 == 0:
            print(k)
        try:
            row_result = [i.value for i in row]
            if row_result[0] and row_result[2]:
                cte_instance = CTE.objects.create(cte_id=row_result[0], name=row_result[1], category=row_result[2],
                                                  code_kphz=row_result[3])
            else:
                continue
            # cte_objects.append(cte_instance)
            # add products if they are exists
            if row_result[-1]:
                row_result[-1] = json.loads(row_result[-1])
                for product in row_result[-1]:
                    cte_product_instance = CTE_product(name=product.get('name'), cte_product_id=product.get('Id'),
                                                       value=product.get('Value'),
                                                       cte=cte_instance)
                    cte_product_objects.append(cte_product_instance)
                CTE_product.objects.bulk_create(cte_product_objects)
        except:
            row_result = [i.value for i in row]

            print('something wrong with {}'.format(row), row_result)
        k += 1
    # CTE.objects.bulk_create(cte_objects)
    # CTE_product.objects.bulk_create(cte_product_objects)

    print('2', time.time() - start_time)


def read_contract(filename):
    start_time = time.time()
    wb2 = load_workbook(filename)
    ws = wb2.active

    rows = ws.rows
    next(rows)
    k = 1
    cte_objects = []
    cte_product_objects = []
    for row in rows:
        if k % 10000 == 0:
            print(k)
        try:
            row_result = [i.value for i in row]
            cte_instance = CTE(cte_id=row_result[0], name=row_result[1], category=row_result[2],
                               code_kphz=row_result[3])
            cte_objects.append(cte_instance)
            # add products if they are exists
            if row_result[-1]:
                row_result[-1] = json.loads(row_result[-1])
                for product in row_result[-1]:
                    cte_product_instance = CTE_product(name=product.get('name'), cte_product_id=product.get('Id'),
                                                       value=product.get('Value'),
                                                       cte=cte_instance)
                    cte_product_objects.append(cte_product_instance)
        except:
            row_result = [i.value for i in row]

            print('something wrong with {}'.format(row), row_result)
        k += 1
    CTE.objects.bulk_create(cte_objects)
    CTE_product.objects.bulk_create(cte_product_objects)

    print('2', time.time() - start_time)


if __name__ == '__main__':
    # print(read("Contract.xlsx"))
    # print(read_xsxl("Contract.xlsx"))
    # print(read_cte("CTE.xlsx"))
    print(read_cte("cte_test.xlsx"))
    # print(read_xsxl("cte_hard_test.xlsx"))
