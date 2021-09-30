mytuple=('solar')
print(mytuple,type(mytuple),sep="\n")

a=tuple()
print(type(a))

star=("solar",1,[22,"22"])
print(type(star))

x=1,2,3
print(type(x))

y=1,
print(type(y))

city=["losangles","beyrut",'tokyo']
city[0]=True
print(city)
print(type(city))

city[1:]='istanbul','moskova' #tuple formatindaki listeyi ekledim
print(city)

city[1:]=["1","2","3",4,False]  #list formatindaki liste ekledim
print(city)

city[1:]="banglades"  #string formatindaki liste ekledim
print(city)

#tuple, iterabli alir ,herbir elemaninin arasina virgul koyar

mountain=tuple("Alps")
print(mountain)

tuple1='h','a','p','p','y'
tuple3=("happy",)
tuple2=1,3,5
print(tuple1)
print(type(tuple1))
print(tuple2,type(tuple2))
print(tuple3)

liste=tuple(range(1,11))
print(type(tuple(liste)),liste,sep="\n")


mix_tup=("11",11,[2,"two",("six",6)],(5,"fair"))  #"six elemenini listeden cek"
print(mix_tup[2][2][0])


mix_tup1=("11",11,[2,"two",("six",6)],(5,"fair"))  #"six elemenini listeden cek"

print(mix_tup1[-4],type(mix_tup1[-4]), sep="\n")