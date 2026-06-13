# 目標:資料輸入與型態轉換
# 任務1:輸入名字並打招呼
name = input("請輸入你的名字: ")
print(f"你好，{name}")
# 任務2:輸入學校並印出完整句子
school = input("請輸入你的學校: ")
print(f"你就讀的學校是 {school}")
# 任務3:輸入年齡並轉成整數後加1
age = int(input("請輸入你的年齡: "))
print(f"明年你會是 {age + 1} 歲")
# 任務4:輸入身高與體重
height = float(input("請輸入你的身高 (公尺): "))
weight = float(input("請輸入你的體重 (公斤): "))
print(f"你的身高是: {height} 公尺")
print(f"你的體重是: {weight} 公斤")