# from typing import Generator


# dict_couple={"bride":["marry","bella","linda"],"groom":["jack","robert","eric"]}
# def muruvvet(bride,groom):
#     couple_list =[]
#     for x in zip(bride,groom):
#         couple_list.append(x)
#     return couple_list

# print(muruvvet(** dict_couple))

# def muruvvet_2(bride,groom):
#     generate=[(bride,groom) for x in zip(bride,groom)]

#     return generate

# friends={"Ahmet":34,"Mehmet":25,"Cemal":12}

# def meaner(Ahmet,Mehmet,Cemal):
#     ortalama=(Ahmet+Mehmet+Cemal)/3
#     return ortalama
# print(meaner(**friends))

friends={"Ahmet":34,"Mehmet":25,"Cemal":12}

def meaner(Ahmet,Mehmet,Cemal):
    ortalama=sum(Ahmet,Mehmet,Cemal)/3
    return ortalama
print(meaner(**friends))
