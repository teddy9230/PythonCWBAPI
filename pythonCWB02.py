import json

# 設定 JSON 檔案的相對路徑
file_path = "F-C0032-001.json"

# 讀取 JSON 檔案內容
with open(file_path, "r") as file:
    data_json = json.load(file)

location = data_json["cwbopendata"]["dataset"]["location"]  # 取出 location 的內容
for i in location:
    city = i["locationName"]  # 縣市名稱
    wx8 = i["weatherElement"][0]["time"][0]["parameter"]["parameterName"]  # 天氣現象
    maxt8 = i["weatherElement"][1]["time"][0]["parameter"]["parameterName"]  # 最高溫
    mint8 = i["weatherElement"][2]["time"][0]["parameter"]["parameterName"]  # 最低溫
    ci8 = i["weatherElement"][3]["time"][0]["parameter"]["parameterName"]  # 舒適度
    pop8 = i["weatherElement"][4]["time"][0]["parameter"]["parameterName"]  # 降雨機率
    print(f"{city}未來 8 小時{wx8}，最高溫 {maxt8} 度，最低溫 {mint8} 度，降雨機率 {pop8} %")
