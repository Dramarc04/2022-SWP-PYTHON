# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random


def Lotto_Ziehung():
    result = []
    for i in range(1,7):
        e = random.randint(1,45)
        print(e)
        while result.__contains__(e):
            e = random.randint(1,45)
            print(e)
        result.append(e)
    return result

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    dict = {}
    for i in range(45):
        dict[i+1] = 0
    for i in range(1000):
        data = Lotto_Ziehung()
        for e in data:
            dict[e] += 1
    print(dict)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
