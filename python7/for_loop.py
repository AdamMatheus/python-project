#adlar="ahmed aisha adam joseph gabriel"
#names=adlar.split()

#i=0

#for i in range(len(names)):

#    print('Hello!',names[i])

###########
#print(list(range(1,6)))  yada
#numbers=[]
#for i in range(1,6):
#    numbers.append(i)
#print(numbers)

a=input("kelimeyi yaz:")
count=0
for i in a:
    count+=1
    if count<len(a):
        i=i+"-"
    print(i,end="")