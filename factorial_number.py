


def factorial(num, result=1):
    if(num<=1):
        return result
    else:
        return factorial(num-1, num * result)


if __name__ == '__main__':
    num = int(input("Enter a number :"))
    print(f"Calculating the factorial for {num}")
    res = factorial(num, 1)
    print(f"factorial of {num} is :{res}")