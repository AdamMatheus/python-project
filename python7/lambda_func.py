# def square(x):
#     return x**2
# print(square(3))
# lambda x:x**2

# print((lambda x:x**2)(2))

# print((lambda x,y:(x+y)/2)(3,5))

# avg=(lambda x,y:(x+y)/2)(3,7)
# print(avg)

# print((lambda x:x[::-1])("1234"))

##########
# sayi=[1,2,3,4] 
# for x in sayi:
print(x, ":",(lambda x: "odd"  if  x%2!=0 else "even")(x))





########lambda with map() function#######################

#iterable=[1,2,3,4,5]
# map(lambda x:x**2,iterable)
# result=map(lambda x:x**2,iterable)
# print(type(result))  #its map type
# print(list(result))  #its list type of print
# print(list(map(lambda x:x**2, iterable)))  ##direct print

# def square(n):
#     return n**2
# result=map(square,iterable)

# for i in result:
#     print(i)
#     print(*result)

