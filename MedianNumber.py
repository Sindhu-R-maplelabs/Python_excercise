try:
    Numbers = []
     
    while True:
        Numbers.append(int(input()))
         
except:
    print(Numbers)
Numbers.sort()  
length = len(Numbers)
#print (length)
if (length % 2 == 0): 
    median = (Numbers[(length)//2] + Numbers[(length)//2-1])/2 
else: 
    median = Numbers[(length-1)//2] 
 

print(median) 