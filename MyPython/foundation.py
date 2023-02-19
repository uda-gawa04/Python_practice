# ターミナルに表示してみる
print("Good morning")
print("Good afternoon")
print("Good evening")

# 変数の宣言
num = 1
msg = "abc"
boo = 2 > 10

# データ型の確認
print(type(num))
# >> <class 'int'>
print(type(msg))
# >> <class 'str'>
print(type(boo))
# >> <class 'bool'>

# リスト
menber_a = []  # 要素のないリスト
menber_b = ["sato", "suzuki", "takahasi"]

print(menber_b[0])
print(menber_b[1])
print(menber_b[2])
# sato
# suzuki
# takahasi

menber_b[1] = "goto"  # 上書き可能
print(menber_b[1])
# goto

menber_c = [["aoki", "iida"], ["kato", "kimura"]]  # ネストすることも可能
print(menber_c[1][0])
# kato

# 演算子
x = 10
y = 2

print(x + y)
print(x - y)

# 論理演算子　かつ・または
z = 8
w = 3

print(z >= 5 and w == 4)  # false
print(z >= 5 or w == 4)  # true


# 代入演算子
xx = 8
xx += 10
print(xx)
# > 18
