import os, sys

root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root_path)

from Data.get_data import GetData
from Base.runmethod import RunMethod


class RunTest:

    def __init__(self):
        self.data = GetData()
        self.run_method = RunMethod()

    # 程序执行的
    def go_on_run(self):
        res = None
        # 获取excel行数,也就是case条数
        rows_count = self.data.get_case_lines()
        for i in range(2, rows_count):
            # caseId = self.data.get_caseId(i)
            url = self.data.get_request_url(i)
            method = self.data.get_request_method(i)
            is_run = self.data.get_is_run(i)
            data = self.data.get_data_for_json(i)
            header = self.data.is_header(i)
            if is_run:
                res = self.run_method.run_main(method, url, data, header)
            return res


if __name__ == '__main__':
    run = RunTest()
    print(run.go_on_run())
