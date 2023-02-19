# クラス

# データ = アトリビュート
# 　クラス内で定義された変数

# 処理 = メソッド
# 　クラス内で定義された関数


class Student_a:
    # メソッドを定義する
    def average(self):
        # 渡したい引数が無くても、必ず一つ必要
        print((80 + 70) / 2)


# インスタンス化 ※クラスは、インスタンスを変数に入れて初めて使えるようになる
a001 = Student_a()
# メソッドの実行
a001.average()

#######


class Student_b:
    def average(self, math, english):
        print((math + english) / 2)


b001 = Student_b()
b001.average(80, 70)

######


class Student_c:
    def average(self, math, english):
        print((math + english) / 2)


c001 = Student_c()
c001.average(30, 40)

# アトリビュートを作る
c001.name = "sato"
print(c001.name)
# > sato

c002 = Student_c()
print(c002.name)
# > error
# アトリビュートは、インスタンスごとに定義されるから

######
# 初期化メソッド（コンストラクタ）を作る


class Student_d:
    # 初期化メソッド↓
    def __init__(self):
        self.name = ""
        # selfはインスタンス名が入るイメージ

    def average(self, math, english):
        print((math + english) / 2)


d001 = Student_d()
d001.name = "sato"
print(d001.name)
# > sato

d002 = Student_d()
print(d002.name)
# > エラーは起きず、何も表示されない

######


class Student_e:
    def __init__(self, name):
        self.name = name
        # インスタンス化と同時に値を代入することもできる

    def average(self, math, english):
        print((math + english) / 2)


e001 = Student_e("sato")
print(e001.name)
# > sato

e002 = Student_e()
print(e002.name)
# > error
# name引数が必須項目になっているから
