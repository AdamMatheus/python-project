#sayi=int(input("lutfen sayi gir : "))

#a=[sayi%i for i in range(2,sayi)] #if not all(a):
#    print("Asal Degil")
#else:
#    print("asal")

#############e   enumerate(iterable,start=0)

#grocery=["bread","water",'olive']
#enum_grocery=enumerate(grocery)

# print(type(enum_grocery))
# print(list(enum_grocery))
# enum_grocery=enumerate(grocery,10)
# print(list(enum_grocery))

###################  max(iterable),min(iterable).

# number=[-222,0,16,5,10,6]
# largestnum=max(number)
# smallestnum=min(number)

# print("the largest number is:",largestnum)
# print("the smallest num is:",smallestnum)


############ sum(iterable,start)

# num=[2.5,30,4,-15]

# numsum=sum(num)
# print(numsum)

# numsum=sum(num,20)
# print(numsum)


######################  round(numbers,ndigits)

# print(round(12))
# print(round(10.8))
# print(round(3.665,2))
# print(round(3.676,2))

# def absltvalue(a):
#     return(abs(a))
    
# print(absltvalue(3.3))
# print(absltvalue(-4))


def absval(num):

    """ This func gives absolute value"""

    if num>=0:
        return num
    else:
        return -num
print(absval(-22))

print(absval.__doc__)
print(abs.__doc__)