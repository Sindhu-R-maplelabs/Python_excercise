def swapPositions(list, pos1, pos2):     
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list

List=[]    
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input())
    List.append(ele)
print(List)
#List = ["aa","bb","cc","dd","ff"] 
#List= [10,20,30,40,50]
pos1=int(input("enter the position 1 to swap:"))
pos2=int(input("enter the position 2 to swap:"))
print(swapPositions(List, pos1-1, pos2-1))