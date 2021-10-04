#number=0
#while number<6:
    #print(number)
    #number+=1
#print("now, number is bigger or greater than 6")

#my_list=['a','b','c','d','e']
#a=0
#while a<len(my_list):
    #print("square of {} is :{}".format(a,a**2))
    #a+=1

#girilen yasin formati dogrumu
#yas=input("lutfen yasini gir: ")

#while  not yas.isdigit() :
   # print("yanlis format,tekrar gir")
    #yas=input("lutfen yasini gir: ")
#print("yasin",yas)

#x=int(input("aklimdaki sayiyi tahmin et:"))
#y=77

#while True:
#    if x<y:
#       print('little higher')
#       x=int(input("aklimdaki sayiyi tahmin et:"))
#    elif  x>y:
#        print("little lower")
#        x=int(input("aklimdaki sayiyi tahmin et:"))
#    else:
#        print("tebrikler buldun")    
#        x=int(input("aklimdaki sayiyi tahmin et:"))
 #       break

texta=input("write a short sentence1: ")
textb=input("write a short sentence2: ")

while True:
    if len(texta)>len(textb):
        print("longest word is {} with length {}".format(texta,int(len(texta))))
    else:
        print("longest word is {} with length {}".format(textb,int(len(textb))))
    break