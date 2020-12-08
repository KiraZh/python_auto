import requests

if __name__ == "__main__":
    header = {'Cookie': 'JSESSIONID=a098a56d-29da-48e1-b773-b3a3d0ceda6d'}
    r = requests.get("https://xgaffairs.uestc.edu.cn/wxvacation/./checkRegisterNew", headers=header)
    print(r.text)

