# 目標: 使用 print 函數印出變數內容
# 變數名稱:名字、學校、科系、年齡
name = "Howard"
school = "國立彰化師範大學"
department = "資訊管理學系"
age = 24
# 單純印出變數內容
print(name)
print(school)
print(department)
print(age)
# 用逗號印出完整句子
print("我的名字是", name)
print("我就讀的學校是",school)
print("我就讀的科系是",department)
print("我的年齡是", age)
# 用 f-string 印出完整句子
print(f"我的名字是 {name}\n我的學校是{school}\n我的科系是{department}\n我今年 {age} 歲")
# 用 f-string 印出一段自我介紹
print(f"大家好，我是 {name}，目前就讀{school}{department}今年 {age} 歲。我正在學 Python，我會一步一步變強。")