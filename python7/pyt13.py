#generate=(i**2 for i in range(6)) 
#print(*generate)    #*generage yaparsan listeyi disariya bosaltir


#print(next(generate))

##Armstrong Number?

while True:

    number=input("write positive integer: ")
    digits=len(number)
    summ=0
    if not number.isdigit():
        print(number,"is invalid.Retry")
    elif int(number)>=0:
        for i in range(digits):
            summ=int(number[i])**2+summ
        if summ==int(number):
            print(number,"is Armstrong Number")
            break
        else:
            print(number,"is not Armstrong") 
            break   

