# def carp(a,b):
#     print(a*b)

# carp(3,7)
# carp(-1,5.4)
# carp('amazing',3)


# def rastgele():
#     print("kafama gore takiliyorum")

# rastgele()

# def add(x,y):
#     print(x+y)

# add(3,5)


# def calc(x,y,islem):
#     if islem=="+":
#         print(x+y)
#     elif islem=="-":
#         print(x-y)
#     elif islem=="*":
#         print(x*y)
#     else:
#         print("yanlis deger girdin")
# calc(6,2,"*")


################  execution function   #########  print<<<<>>>return

# def multip(a,b):
#     print(a*b)
# multip(10,4)


# def multipl(a,b):
#     return(a*b)
# print(multipl(10,4))


# print(type(multip(10,4)))
# print(type(multipl(10,4)))    
   

def calc2(x,y,islem):
    if islem=="+":
        return(x+y)
    elif islem=="-":
        return(x-y)
    elif islem=="*":
        return(x*y)
    else:
        return("yanlis deger girdin")
print(calc2(9,2,"*"))