#who=["i am", "you are"]
#mood=[' happy',' confident']
#for i in who:
  #  for ii in mood:
     #   print(i+ii)


#listekerdeki elemanlari birbiriyle birlestirip yazdir

#names=["susan","tom","edward"]
#mood=['happy','sad']

#for a in names:
    #for b in mood:
       # print(a+" is "+b)

#########LIST COMPREHENSION############
print([item for item in range(5)])

print([i**2 for i in range(5)])

#########Ternary IF Statements

#condition=True
#if condition:
 #   a=1
#else:
  #  a=0
#print(a)

listem=[1,2,3,4,5,6]

print([i**2 for i in listem if i%2])