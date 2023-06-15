import json
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
root_path = os.path.dirname(current_dir)


class OperationJson:

    def __init__(self):
        self.data = self.read_data()

    # 获取json文件
    def read_data(self):
        with open(root_path + '/Datapools/user.json', 'r') as f:
            self.data = json.load(f)
            return self.data

    # 根据关键字获取数据
    def get_data(self, name):
        return self.data[name]


if __name__ == '__main__':
    opjson = OperationJson()
    print(opjson.get_data("login"))
