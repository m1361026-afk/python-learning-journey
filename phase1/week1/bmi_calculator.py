# 先讓使用者輸入自己的身高、體重
height = float(input("請輸入您的身高(公尺): "))
weight = float(input("請輸入您的體重(公斤): "))

# 計算 BMI
bmi = weight / (height ** 2)

# 印出 BMI 結果，並保留兩位小數
print(f"您的 BMI 是: {bmi:.2f}")