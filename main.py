import requests

if __name__ == "__main__":
    url = "https://jzsz.uestc.edu.cn/wxvacation/./monitorRegisterForReturned"

    payload = "{\n  \"healthCondition\" : \"正常\",\n  \"todayMorningTemperature\" : \"36°C~36.5°C\",\n  \"yesterdayEveningTemperature\" : \"36°C~36.5°C\",\n  \"yesterdayMiddayTemperature\" : \"36°C~36.5°C\",\n  \"location\" : \"四川省成都市郫都区成灌高速公路\"\n}"

    headers = {
        'Cookie': 'JSESSIONID=89e4d4c5-7bbd-419a-bccb-100f017842b9; SESSION=e1c46237-5082-4276-a2b1-179ed3b6608a',
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload.encode("UTF-8"))
    print(response.text)