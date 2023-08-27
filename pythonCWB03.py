import json

# 設定 JSON 檔案的相對路徑
file_path = "O-A0001-001.json"

# 讀取 JSON 檔案內容
with open(file_path, "r") as file:
    data_json = json.load(file)

location = data_json["cwbopendata"]["location"]
for i in location:
    name = i["locationName"]  # 測站地點
    city = i["parameter"][0]["parameterValue"]  # 城市
    area = i["parameter"][2]["parameterValue"]  # 行政區
    print(city, area, name)
