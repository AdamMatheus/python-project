#############passsword generator program

# import random
# random.randint(65,90)
# print(chr(random.randint(65,90)))

# uppers=[chr(random.randint(65,90)) for i in range(3)]
# print(uppers)

# print("".join(uppers))  ###sonuctaki bosluklari kaldirip elemanlari birlestir

# lowers=[chr(random.randint(97,122)) for i in range(3)]###kucuk harf ekleme
# numbers=[chr(random.randint(48,57)) for i in range(3)]#sayi ekleme
# chars=[chr(random.randint(33,47)) + chr(random.randint(58,64))]#isaret ekleme

# password=''.join(uppers)+''.join(lowers)+''.join(numbers)+''.join(chars)
# print(password)

# def shuffleit(string):
#     tempList=list(string)
#     random.shuffle(tempList)
#     return ''.join(tempList)

# passw=shuffleit(password)
# print(passw)


#################################################### for loop ile sifre olusturma


from timeit import timeit
###########asagidaki iki yontemden hangisi hizli kiyaslayalim

# def for_loop():     ######1.yontem olusturulan fonksiyon
#     result=[]

#     for i in range(1000):
#         result.append(i)
#     return result


# def list_compherension():       ##########2.yontem
#     return [i for i in range(1000)]


# print(timeit(for_loop,number=1000))
# print(timeit(list_compherension,number=1000))

# time1=timeit(for_loop,number=1000)
# time2=timeit(list_compherension,number=1000)

# print(f"List Compherension is {round(time1/time2,2)} times faster than For Loop")

###############python uzerinde mail gonderme##############!!!!!!!!!!!!!!

import smtplib          ####### Simple Mail Trasfer Port

server=smtplib.SMTP("smtp.gmail.com",587)
print(server.starttls())
sifre="Afyon2364"
server.login("mathvirus03",sifre)

message="\n This is my test mail .\n havegood day"
adres="halimelihalimeli@gmail.com"

server.sendmail("mathvirus03",adres,message)
server.quit();

