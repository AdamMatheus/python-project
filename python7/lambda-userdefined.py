# def repeater(n):
#     return lambda x:x*n
# repeat5=repeater(5)
# print(repeat5("sizi ozledim"))
# repeat2=repeater(2)
# print(repeat2("gule gule "))


# def functioner(n):
#     return lambda x:x +  n
# myprint_smile=functioner(":)")
# print(myprint_smile("hello "))
# myprint_sad=functioner(":(")
# print(myprint_sad("hello  "))
# myprint_neutral=functioner(":| ")
# print(myprint_neutral("hello  "))

# def funct(emoji):
#     return lambda message:print(message,emoji)

# smile=funct(" :)")
# print(smile(1))

# sad=funct(":(")
# print(sad([1,"1",False] ))

# def x():
#     return 1,2,3,4
# print(type(x()))
# a,b,c,d=x()
# print(a)

from typing import Counter


# num=[1,5,4,4,1,1,1]
# max(num,key=num.count) #listedeki en  fazla tekrar eden eleman

# def tekrar():
#     return 
# maxsayi=max(num,key=num.count)


# print(num.count(maxsayi))

 #listedeki en  fazla tekrar eden eleman

# def tekrar():
#     num=[1,4,4]
# equallambda=lambda x,y,z:[x,y,z].count(max([x,y,z],key=[x,y,z].count)) if [x,y,z].count(max([x,y,z],key=[x,y,z].count))>1 else 0
# print(equallambda(1,4,4))

def functgener(function):
    return lambda x:function(x)
print(print("sen"))
print(max([2,3,5]))
print(bool("hey"))





