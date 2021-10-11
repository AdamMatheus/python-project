# first_ten=[0,1,2,3,4,5,6,7,8,9]
# even=filter(lambda x:x%2==0,first_ten)
# print(type(even)) #its filter type
#                     #in order to print result
#                     #we`d better convert it in to th list type
# print('even numbers are:',list(even))

# words=['apple','swim','clock','me','kiwi','banana']

# print(list(filter(lambda x: len(x)<5,words)))

# first_ten=["a",'b','c','d','e','f','g','h','i','j','u']
# vowels=["a","e","i","o","u"]
 print(list(filter(lambda x:x in vowels,first_ten)))


com=["rihgt 20","right 30","left 50","up 10","down 20"]
x=y=0
for i in range(len(com)):
    if com[i].startswith("r"):x=x+int(com[i].split()[1])
    elif com[i].startswith("l"):x=x-int(com[i].split()[1])
    elif com[i].startswith("u"):y=y+int(com[i].split()[1])
    elif com[i].startswith("d"):y=y-int(com[i].split()[1])
print([x,y]);
