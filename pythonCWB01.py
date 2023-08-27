import json

# 設定 JSON 檔案的相對路徑
file_path = "F-C0032-001.json"

# 讀取 JSON 檔案內容
with open(file_path, "r") as file:
    data_json = json.load(file)

location = data_json["cwbopendata"]["dataset"]["location"]  # 取出 location 的內容
for i in location:
    print(f"{i}")
