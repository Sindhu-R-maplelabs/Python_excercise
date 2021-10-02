def findFactZero(n):
    count = 0
    i = 5
    while (n/i>= 1):
        count += int(n / i)
        i *= 5
  
    return int(count)
def fact(n):
    if n==1:
        return n
    else :
        return n*fact(n-1)

num = int(input("enter the number "))
print(fact(num))
print("Count of 0's in",num,"factorial is", findFactZero(num))
  