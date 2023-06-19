import requests


class RunMethod:
    def post_main(self, url, data, header=None):
        res = None
        if header != None:
            res = requests.post(url=url, json=data, headers=header)
            # 接口返回状态
            # print(res.status_code)
        else:
            res = requests.post(url=url, json=data)
            # print(res.status_code)
        return res.json()

    def get_main(self, url, data=None, header=None):
        res = None
        if header != None:
            res = requests.get(url=url, params=data, headers=header)
        else:
            res = requests.get(url=url, params=data)
        return res.json()

    def run_main(self, method, url, data=None, header=None):
        res = None
        if method == 'POST':
            res = self.post_main(url, data, header)
        else:
            res = self.get_main(url, data, header)
        return res
