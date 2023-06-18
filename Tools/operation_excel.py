import xlrd, openpyxl
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
root_path = os.path.dirname(current_dir)


class OperationExcel:
    def __init__(self, sheet_id=None, file_name=None):
        if file_name:
            self.file_name = file_name
            self.sheet_id = sheet_id
        else:
            self.file_name = root_path + '/Datapools/interface.xlsx'
            self.sheet_id = sheet_id
        self.data = self.get_data()

    # 获取哪张sheet的内容
    def get_data(self):
        # data = xlrd.open_workbook(self.file_name)
        # return data.sheets()[self.sheet_id]
        # return data.sheet_by_index(self.sheet_id)
        # return data.sheet_by_name('Sheet1')
        data = openpyxl.load_workbook(self.file_name)
        # openpyxl库 操作 .xlsx表
        return data.worksheets[self.sheet_id]
        # return data['Sheet1']

    # 获取单元格的行数
    def get_lines(self):
        tables = self.data
        # return tables.nrows
        return tables.max_row

    # 获取某个单元格内容
    def get_cell_value(self, row, col):
        tables = self.data
        # return tables.cell_value(row, col)
        return tables.cell(row, col).value


if __name__ == '__main__':
    opers = OperationExcel(0)
    print(opers.get_data())
    print(opers.get_lines())
    # print(opers.get_cell_value(2, 3))
    print(opers.get_cell_value(3, 4))
