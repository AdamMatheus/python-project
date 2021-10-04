sentence=input("cumleyi yaz:")
words=sentence.split()
i=0
longest=0
while i<len(words):
    if len(words[i])>longest:
        longest=len(words[i])
    i+=1    
print("length of the longest word is:",longest)
