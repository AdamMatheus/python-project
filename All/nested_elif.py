# girdigin sinav sonucunu harfli karsiligini bulma
x=float(input("enter your score: "))
if x>=95:
    print('A+')
elif x<95 and x>=90:
        print("A")
elif x>=85 and x<90:
        print("B+")
elif x>=80 and x<85:
        print("B")
else:
    print("B-")