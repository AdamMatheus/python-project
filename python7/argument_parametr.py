#####   positional
# a="i"
# b="love"
# c="you"

# def texter(c=a,a=b,b=c):
    
#     print(a,b,c)
    

# texter(c,a,b)
    
 #############  keywordargument=kwarg
# def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
#     print("-- This parrot wouldn't", action, end=' ')
#     print("if you put", voltage, "volts through it.")
#     print("-- Lovely plumage, the", type)
#     print("-- It's", state, "!")
# parrot(1000)
# parrot(voltage=100000,action="voooom") 
# parrot(action="voooom",voltage=100000)
# parrot("million ","bereft of life", "jump")
# parrot("a thousand", state="pushing up the daisies")

# def argu(a,b="dunya",c,d="saturn"): #tum positionallar yazildiktan sonra digerleri yazilmali..burada yanlis yazdik
#     print(a,b,c,d,sep="\n")

def argu(a,c,b="dunya",d="saturn"):
    print(a,b,c,d,sep="\n")
argu("uranus","jubiter")
argu(a="uranus",c="jubiter")
argu("pluto","venus",d="mars")