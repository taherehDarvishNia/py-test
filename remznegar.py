from random import *
a=["1","2","3","4","5","6","7","8","9","q","w","e","r","t","y"\
   "u","i","o","p","a","s","d","f","g","h","j"\
   "k","l","z","x","c","v","b","n","m",
   ]
r=input("ramz : ")

k=0

while True :
    c="".join(sample(a,4))
    if (r[0]==c[0]) and (r[1]==c[1]) and (r[2]==c[2]) and (r[3]==c[3]) :
        print(r ,"==", c)
        break
    k+=1
    print(f"ramz dorost nist : {k} ")
