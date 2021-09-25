#ELEMANLARINI TEKER TEKER YAZDIRMA
sozluk=dict(animal="dog",planet="saturn",number="35",pi="3.14",is_good=True)
print(sozluk.items(),'\n')
print(sozluk.keys(),'\n')
print(sozluk.values())
print(type(sozluk.values()))
print(list(sozluk.values()))

#ELEMANLARINI TEK TEK LISTELEME METODU
family={"name1":"Halil","name2":"Halime","name3":"Cemil"}
print(list(family.items()),"\n")
print(list(family.keys()),"\n")
print(list(family.values()),"\n")

#UPDATE YAPMA

sozluk=dict(animal="dog",planet="saturn",number="35",pi="3.14",is_good=True)
sozluk.update({"is_bad":False,3:"uc"})

print(sozluk)

#DEL

sozluk=dict(animal="dog",planet="saturn",number="35",pi="3.14",is_good=True)

del sozluk["animal"]
print(sozluk)

fifth_dic={"erkekler":{"ahmet":35,"mehmet":30, "cevat":17},\
    "bayanlar":{"ayse":23, "melek":10}}
del fifth_dic["bayanlar"]
print(fifth_dic)

#in  ve not in  operatoru True False sonuc verir ..listede varmi yokmu
# ...key lerin arasinda arar

clarusway=['ali','veli','deli']
print('zeki' in clarusway)

print("deli" in clarusway)

# value icinde aramak icin sozluk.value
sozluk=dict(animal="dog",planet="saturn",number="35",pi="3.14",is_good=True)
print("dog" in sozluk.values() )

print('dog' not in sozluk)