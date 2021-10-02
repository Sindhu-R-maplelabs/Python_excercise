def rev_number(n):
  s=0 
  if n in range (100,1000):
    for i in range(n):
      k = str(n)
      if k == k[::-1]:
        break
      else:
        m = int(k[::-1])
        n += m
        s += 1
    return n 
  else:
    print ("give the value within the range between 100-1000")

print((rev_number(int(input("enter the digit ")))))
