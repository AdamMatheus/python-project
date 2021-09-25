#dictionary eslestirmeli durumlarda kullanilan bir fonksiyon
my_dict={
    'key1':'value1',
    'key2':'value2',
    'key3':'value3'}
print(my_dict)

grocer1={"fruit":"apple","drink":"water"}
grocer2=dict(fruit="apple", drink="water")
print(grocer1)
print(grocer2)

first_dic={1:"one","two":2, False:[1,2,3]}
print(first_dic)

second_dic={(1,2,3):"liste","clarusway":"the best"} #eger [1,2,3] kullanirsam kabul etmiyor
print(second_dic)

#!!!!dict icinde { },[] seklinde key yazilamiyor ancak {},[] value olarak yazilabilir

fifth_dic={"erkekler":{"ahmet":35,"mehmet":30, "cevat":17},\
    "bayanlar":{"ayse":23, "melek":10}}
print(fifth_dic)

# accessing and assigning an item

capitals={'Arkansas':"little Rock",
            "colorado":'denver',
            "california":"sacramento",
            "georgia":"Atlanta"}
print(capitals['colorado'])

# ADDING NEW ELEMENT
capitals1={'Arkansas':"little Rock",
            "colorado":'denver',
            "california":"sacramento",
            "georgia":"Atlanta"}
capitals1["virginia"]="richmond"
print(capitals1)

#keys and values can be of different types

mix_values={'animal':("dog","cat"), #tuple
            'planet':['neptun','saturn','jupiter'], #list type
            'number':40, #int type
            'pi':3.14, #float type
            'is_good':True} #bool type
print(mix_values)

mix_keys={22:"integer",
        1.2:"float",
        True:"boolean",
        "key":"string"}
print(mix_keys)


family={"name1":"Halil","name2":"Halime","name3":"Cemil"}
print(family)

family["name4"]="Asude"
print(family)

#dict fonksiyonuyla dictionary olusturma

sozluk=dict(animal="dog",planet="saturn",number="35",pi="3.14",is_good=True)
print(sozluk)


fam=dict(name1="halo",name2="maho",name3="cano")
print(fam)


n1,n2,n3=5,10,15
numbers={n1 :"bes", n2:"on" ,n3:"onbes"}
print(numbers)

sayilar={"tek":[],
        "cift":[]}
print(sayilar)
sayilar["tek"]="1,3,5,7,9" # sayilar["tek"].append(tek sayilari tek tek ekle) #
sayilar["cift"]="2,4,6,8,10" #sayilar['cift].append(cift sayilari tek tek ekle) yani value tipi neyse ona gore islemleri ayarla.yani listeyse listeye gore ,string ise stringe gore islemler yapilir
print(sayilar)   
print(sayilar["tek"])




