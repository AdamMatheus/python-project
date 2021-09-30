bool_value=False

if bool_value:
    print("Yes")
else:
    print('no')

#klavyeden girilien 3 sayidan en buyugunu yazdir

x=float(input("ilk sayi: "))
y=float(input("ikinci sayi : "))
z=float(input('ucuncu sayi: '))

if x>y and x>z:
   largest=x
elif y>x and y>z:
   largest=y
else:
    print("largest=",z)
