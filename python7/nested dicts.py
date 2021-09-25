school={
    "personelinfo":
        {"kid":{"tom":{"class":"intermadiate","age":10},
                "sue":{"class":"elementary","age":8}
            },
        "teen":{"joseph":{"class":"college","age":19},
                "marry":{"class":"high school","age":16}
                },
        },
                    
    "gradesinfo":
        {"kid":{"tom":{"math":88, "speech":69},
                "sue":{"math":90, "speech":81}
                },
        "teen":{"joseph":{"coding":80,"math":89},
                "marry":{"coding":70,"math":96}
                },
            },
}                

print(school)
#marry nin yasini kayitlardan suz
print(school["personelinfo"]["teen"]["marry"]["age"])


#josephin ders notlari
print(list(school["gradesinfo"]['teen']['joseph'].items()))
print(school["gradesinfo"]['teen']['joseph'])




#index bulma

samanlik=["yumurta","saman","inek","igne","yaba"]
print(f"igne {samanlik.index('igne')} numarali indextedir.")