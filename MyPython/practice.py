# 実践


class Student:
    def __init__(self, name):
        self.name = name

    def calculate_avg(self, data):
        sum = 0

        for score in data:
            sum += score

        avg = sum / len(data)
        # len は、dataの要素数を取得する
        return avg

    def judge(self, avg):
        if avg >= 60:
            result = "passed"
        else:
            result = "failed"
        return result


a001 = Student("sato")
data = [70, 65, 50, 90, 30]
avg = a001.calculate_avg(data)
result = a001.judge(avg)

print(avg, a001.name + " " + result)


a002 = Student("goto")
data = [50, 70, 60, 85, 30]
avg = a002.calculate_avg(data)
result = a002.judge(avg)

print(avg, a002.name + " " + result)
