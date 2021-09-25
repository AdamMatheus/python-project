meat=True
bread=True
lettuce=False
pepper=True
store=False

if (bread and (pepper or lettuce) and store and meat)==True:
    print("hamburger hazir")
else:
    print("eksik malzeme var")

a="TWELVE PLUS ONE"
b="ELEVEN PLUS TWO"

if set(a)==set(b):
    print('We are the same')


cevp=input("Yes or No:" ).title().strip()=="Yes" #girilen degerin buyuk kucuk harf ve bosluk yapma hatalarini silebiliriz
print("you entered",cevp)
# git huba eklendi
