#Dictwords = {
 #   "hello": 56,
  #  "at" : 23 ,
   # "test" : 43,
    #"this" : 43
    #}
n=5
Dictwords=dict(input().split() for x in range(n))
print(Dictwords)
print("Sorting keys in Ascending order ")
for key in sorted(Dictwords.keys()) :
   print(key , " :: " , Dictwords[key])

print("Sorting Values in Ascending order")
for elem in sorted(Dictwords.items() ,  key=lambda x: len (x[1])):
    print(elem[0] , " ::" , elem[1] )  


#print("for reverse order")
#print(sorted(Dictwords, reverse=True))