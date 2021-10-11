#empty=[]
#max(empty,default=True) #verilen kume bos ise default ne ise onu verir

#seq=[1,1,1,1,2,2,2,3,3,4]
#print(max(seq)) #en buyuk sayiyi verir

#seq=[1,1,1,1,1,2,2,2,2,3,3,4,4] #hangi elemandan kac tane var
#print(seq.count(4))

#print(seq.count(max(seq))) #en buyuk eleman kac kez tekrar edeer

#aw=max(seq,key=seq.count)#en fazla tekrarlayan elemani bulma key=seq.count elemanlarini saydiriyor

#bw=seq.count(max(seq,key=seq.count)) #en fazla tekrarlayan kac kere tekrarladi

#print(("En cok tekrarlayan sayi {} sayisidir ve {} defa tekrar etmistir.".format(aw,bw)))

# verilen bir kelimenin comfortable word olup olmadigini bulma
kullanilacak metod (word\left) ve (word\right) bos kume olmamasi gerek

left={'q', 'w', 'e', 'r', 't', 'a', 's', 'd', 'f', 'g', 'z', 'x', 'c', 'v', 'b'}
right={'y', 'u', 'i', 'o', 'p', 'h', 'j', 'k', 'l', 'n', 'm'}
word="afyonkarahisar"  
set_word=set(word)
left_bool=bool(set_word-left)
print(left_bool)
right_bool=bool(set_word-right)
print(right_bool)
if right_bool and left_bool:
   print("comfortable_word" ,word)