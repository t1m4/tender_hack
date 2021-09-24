import os
import time

from pandas import read_excel
def read(filename):
    start_time = time.time()
    result = read_excel(filename)
    t = 0
    for row in result.iterrows():
        print(row[1].values)
        # print("fir/st", i)
        # t += 1
        # time.sleep(1)
    print("End time",t,  time.time() - start_time)
    return

class CSVReader():
    MAX_PAGE_SIZE = 10

    def _file_read(self, filename):
        exist = os.path.exists(filename)
        if not exist:
            raise ValueError('File does not exist')

        with open(filename, 'rb') as f:
            result = f.readlines()
            for line in result:
                print(line.decode('cp1252'))
                yield line
                return

        # index = 0
        # print(file)
        # for line in file:
        #     print(line)
        #     yield index, line
        #     index += 1

    def read_file(self, filename: str, max_page_size: int, start_from_line: int = 1):
        """
        Read curtain line from file
        """
        result_lines = []
        for index, line in self.__file_read(filename):
            if index < start_from_line:
                continue
            elif index >= start_from_line + max_page_size:
                break
            else:
                line = line.strip().split(';')
                result_lines.append(line)
        return result_lines

if __name__ == '__main__':
    print(read("test.xlsx"))
    # csv_reader = CSVReader()
    # for i in csv_reader._file_read("test.xlsx"):
    #     print(i)