#####  *args and **kwargs###################################

# def  name(*parameter)

#     name(multiple args)

# def name(**parameter)
#     name(multiple kwargs)

# def fruiterer(fruit1,fruit2):
#     print("I want to get", fruit1, "and", fruit2)
# fruiterer("orange","banana")

# def fruiterer(*fruit): ###sayisi belirsiz meyve ise...
#     print("i want to get:")
#     for i in fruit:
#         print("-",i)
# fruiterer("orange","banana","melon","ananas")

# def slicer(*numbers):
#     even=[]
#     odd=[]
   
#     for i in numbers:
#         if i%2 == 0:
#            even.append(i)
#         else:
#             odd.append(i)
#     print("even list:",even)
#     print("odd list:", odd)
# slicer(1,2,3,4,5,6,12,14,15,23,16)

# def animals(**kwargs):
#     for key ,value in kwargs.items():
#         print(value,"are",key)
# animals(Carnivores="lions",Omnivores="bears",Herbivores='deers',Nomnivores="human")

####    key value argumennts
def orginazer(**kwargs):
    names=[]
    ages=[]
   
   
    for key, value in kwargs.items():
           
            names.append(key)
            ages.append(value)
    print(names)
    print(ages)

orginazer(Beth=26,Oscar=42,Justin=18,Frank=32,Halil=39)


