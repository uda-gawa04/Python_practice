# 関数

# 引数のない関数
def say_hello1():
    print("hey world")


say_hello1()

# 引数がある関数
def say_hello2(greeting):
    print(greeting)


say_hello2("hello world")

# 関数を変数に入れる
hello = say_hello2
hello("good morning")


def add(num1, num2):
    return num1 + num2


add(6, 2)
# > 何も表示されない = ただただreturnしてるだけだから


# 練習問題
def average(num1, num2, num3):
    return (num1 + num2 + num3) / 3


print(average(9, 4, 2))
# > 5.0
