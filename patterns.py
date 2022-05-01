


def pattern(num):
    temp = num
    while temp > 0:
        print("*" * (num - temp))
        temp -=1


pattern(5)