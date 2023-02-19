# if文
age = 18

if age >= 20:
    print("adult")
elif age == 0:
    print("baby")
else:
    print("child")


# 繰り返し
for i in range(5):
    print(i)

# i カウンタ変数
# range(5) 繰り返す回数

# break
for i in range(5):
    if i == 3:
        break  # for文を抜ける
    print(i)

# continue
for i in range(5):
    if i == 3:
        continue  # 以下の処理を飛ばす
    print(i)

# ネスト
for i in range(3):
    for j in range(3):
        print(i, j, sep="-")

# リストとfor文
arr = [2, 4, 6, 8, 10]

for i in arr:
    print(i)
    # print(arr[i]) > error

sum = 0
for i in arr:
    sum += i  # 足し上げることもできる

print(sum)
# > 30
