#text=["one","two","three"]
#numbers=[1,2,3]
#for x,y in zip(text,numbers):
#    print(x,":",y)

#########1-10 arasi sayilar tekleri ve ciftleri ayri kumele

sayilar=list(range(10))
cift=[]
tek=[]
for i in range(10):
    if i%2==0:
        cift.append(i)
    else:
        tek.append(i)
print("tek sayilar:{}\n ciftsayilar:{}".format(tek,cift))
