


def is_palindrome(input):
    input_str = input.lower()
    if input_str == input_str[::-1]:
        return True
    else:
        return False

def factorial(num):
    if num <= 0:
        return 0
    elif num == 1:
        return 1;
    else: 
        return num * factorial(num-1)


def factorial(num, res=1):
    if num <= 0:
        return 0
    elif num == 1:
        return res
    else:
        return factorial(num-1, num*res)


if __name__=='__main__':
    # input = input("\nInput a string to check - Whether it is a Palindrome Or Not: ")
    # print(input)
    # result = is_palindrome(input)
    # if result:
    #     print(f"{input} - is a palindrome")
    # else:
    #     print(f"{input} - is Not a Palindrome")

    input = float(input("\nEnter a Number to calculate Factorial: "))
    import sys
    sys.setrecursionlimit(1500)
    print(sys.getrecursionlimit())
    print(factorial(input))
