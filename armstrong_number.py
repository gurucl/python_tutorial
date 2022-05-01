


def is_armstrong_number(num):
    temp = num
    length = len(str(temp))
    res = 0

    while temp > 0:
        digit = temp % 10
        temp = temp // 10
        res += digit ** length

    if res == num:
        print(f"Yes, {res} == {num} is a Armstrong Number")
    else:
        print(f"No, {res} != {num} is not a Armstrong Number")

    


def is_neon_number(num):
    val = num * num
    res = 0
    while val > 0:
        digit = val % 10
        res += digit
        val = val // 10

    if res == num:
        print(f"Yes, {num} == {res} is a Neon Number")
    else:
        print(f"No, {num} != {res} is not a Neon Number")



if __name__=='__main__':
    num = int(input("Enter a Number: "))
    # is_neon_number(9)
    is_armstrong_number(num)




