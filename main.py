import requests


class RunMethod:
    def post_main(self, url, data, header=None):
        res = None
        if header != None:
            # verify=False 关闭证书验证
            res = requests.post(url=url, json=data, headers=header, verify=False)
            # print(res.status_code)
        else:
            res = requests.post(url=url, json=data, verify=False)
            # print(res.status_code)
        return res.json()

    def get_main(self, url, data=None, header=None):
        res = None
        if header != None:
            res = requests.get(url=url, params=data, headers=header, verify=False)
        else:
            res = requests.get(url=url, params=data, verify=False)
        return res.json()

    def run_main(self, method, url, data=None, header=None):
        res = None
        if method == 'POST':
            res = self.post_main(url, data, header)
        else:
            res = self.get_main(url, data, header)
        return res


if __name__ == '__main__':
    url = 'https://api.17track.net/track/v1/register'

    data = [{
        "number": "SYRM134693899",
        "carrier": 190072}]

    header = {"Content-Type": "application/json;charset=utf-8", "17token": "AC3BEC6BB65183D40A68B22AF178FFA3"}

    run = RunMethod()
    print(run.run_main('POST', url, data, header))
