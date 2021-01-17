import requests

if __name__ == "__main__":
    url = "https://xgaffairs.uestc.edu.cn/wxvacation/./monitorRegisterForReturned"

    payload = "{\n    \"healthCondition\":\"正常\",\n    \"todayMorningTemperature\":\"36°C~36.5°C\"," \
              "\n    \"yesterdayEveningTemperature\":\"36°C~36.5°C\"," \
              "\n    \"yesterdayMiddayTemperature\":\"36°C~36.5°C\"\n} "
    headers = {
        'Cookie': 'JSESSIONID=140ad9c7-db8c-4ea5-81ad-e24f1e9f3c80; SESSION=8d990cb9-9e47-4565-bda0-7db239f3284c',
        'Content-Type': 'application/json;charset=UTF-8'
    }

    response = requests.request("POST", url, headers=headers, data=payload.encode("UTF-8"))
    print(response.text)




