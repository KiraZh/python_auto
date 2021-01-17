import requests

url = "https://xgaffairs.uestc.edu.cn/wxvacation/./monitorRegister"

payload = "{\n\t\"currentAddress\": \"山西省太原市万柏林区清泽东路\",\n\t\"remark\": \"\",\n\t\"healthInfo\": \"正常\"," \
          "\n\t\"isContactWuhan\": 0,\n\t\"isFever\": 0,\n\t\"isInSchool\": 0,\n\t\"isLeaveChengdu\": 1," \
          "\n\t\"isSymptom\": 0,\n\t\"temperature\": \"36°C~36.5°C\",\n\t\"province\": \"山西省\",\n\t\"city\": \"太原市\"," \
          "\n\t\"county\": \"万柏林区\"\n} "
headers = {
    'Cookie': 'JSESSIONID=003cdaa3-434a-4391-b317-636b2ed8c1cc; SESSION=659f7e25-bc3a-4b58-84ae-09b519899f11',
    'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload.encode("UTF-8"))

print(response.text)
