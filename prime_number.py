



def is_prime(num):
    flag = True
    for i in range(2, int(num/2)):
        if num % i == 0:
            flag = False
            break
    
    if flag:
        print(f"{num} - is a Prime Number")
    else:
        print(f"{num} - is Not a Prime Number")

if __name__=='__main__':
    # num = int(input("Enter a number: "))
    # is_prime(num)
    l2 = list(range(1,11))
    l = list((1,2,3,4,5,"Guru",7,8,9))
    print(l)
    l.reverse()
    print(l)
    x = l[::-1]
    print(x)
  


    

