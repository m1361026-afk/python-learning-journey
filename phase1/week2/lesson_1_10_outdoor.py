# 任務 C：是否適合出門
# Ask the user whether is it sunny and whether he/she brings an umbrella
sunny = input("Please enter whether the day is sunny day (yes/no): ")
umbrella = input("Please enter whether you bring an umbrella (yes/no): ")
# Check whether the user can go out
if sunny == "yes" or umbrella == "yes":
    print("適合出門")
else:
    print("不適合出門")