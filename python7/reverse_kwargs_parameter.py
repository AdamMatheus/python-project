########reverse kwarg and parameter############

# def brothers(bro1,bro2,bro3):
#     print("here are the names of brothers:")
#     print(bro1,bro2,bro3, sep="\n")
# bros=["tom","sue","tim"]

# brothers(*bros)

#####filter fonksiyonu kullanma
#"bazen odun olmayi istemisimdir"  ###sesli harfleri filtrele

# cumle="bazen ODUN olmayi istemisimdir"

# def voweler(letter):
#     vowels=["a",'e',"i","u","o"]

#     if letter.lower() in vowels:
#         return True

#     else:
#         return False

# filtered_vowels=filter(voweler,cumle)
# list(filtered_vowels)

# ############
# def gene(x,y):  #defined by positional args
#     print(x,"belongs to Generation X")
#     print(y,"belongs to Generation Y")

# dict_gene={"y": "Mary","x":"Fred"}
# gene(**dict_gene) #we call the functuion by single argument(variable)

dict_couple={"bride":["marry","bella",'linda','emma'],"groom":['jack','robert','eric','adam']}
def muruvvet(bride,groom):
    couple_list =[]
    for x in zip(bride,groom):
        couple_list.append(x)
    return couple_list

muruvvet(** dict_couple)

    
    
     




