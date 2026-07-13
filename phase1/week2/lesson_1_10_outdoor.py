# 任務 C：是否適合出門
# Ask whether it is sunny and whether the user has an umbrella
is_sunny = input("Please enter whether the day is sunny day (yes/no): ")
has_umbrella = input("Please enter whether you bring an umbrella (yes/no): ")
# Check whether it is suitable to go outside
if is_sunny == "yes" or has_umbrella == "yes":
    print("適合出門")
else:
    print("不適合出門")