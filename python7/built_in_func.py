names=["susan",'tom','False']
mood=["happy",'sad',0]
empty={}

print(all(names),all(mood),all(empty),sep="\n") #"all" hepsi True ise True yazar.aksi halde Fasle

listA=["susan","tom",False]
listB=[None,(),0]
empty={}

print(any(listA),any(listB),any(empty),sep="\n")# "any" enaz bir dogru varsa True yazar

liste=["susan","tom",False,0,"0"]
filtered_list=filter(None,liste) #listedeki truthyleri alir

print("The filtered elements are: ")
for i in filtered_list:
    print(i)