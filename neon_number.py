

def is_neon_number(num):
    sqr = num * num
    res = 0
    while(sqr>0):
        digit = sqr%10
        sqr = int(sqr/10)
        res = res + digit

    if(res==num):
        print(f"Number {num} is a Neon Number")
    else:
        print(f"Number {num} is NOT a Neon Number")


if __name__=='__main__':
    num = int(input("Enter a Number: "))
    is_neon_number(num)
