def recursive_fibo(n):
   if n <= 1:
       return n
   else:
       return(recursive_fibo(n-1) + recursive_fibo(n-2))

Num = int(input("enter a positive integer "))
if Num >= 0:
    print("Fibonacci sequence are:")
    for i in range(Num):
        print(recursive_fibo(i))
else :
    print("please enter a positive number")