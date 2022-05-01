


def fibo(num):
   a = int(input("Enter the First number: "))
   b = int(input("Enter the Second number: "))
   num = int(input("Enter the number of elements: "))
   print(a, b, end=" ")

   while num-2:
       c = a+b
       a = b
       b = c
       print(c, end=' ')
       num = num-1


fibo(5)