count=3
while count>0:
    try :
        fruits=["banana","mango","pear","apple","kiwi","grape"]
        i=int(input("lutfen index no girin:"))
        print("my favorite fruit is:",fruits[i])
        break
    except (TypeError,IndexError):
        count-=1
        print(f"hatali giris yaptiniz,{count} hakkkin kaldi,lutfen tekrar deneyin",(IndexError,TypeError))
    except ValueError:
        count-=1
        print(f"tam sayi girmen gerekiyor,{count} hakkkin kaldi")
    else:
        print("afiyet olsun")
