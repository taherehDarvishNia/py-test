n1=int(input("n : "))
n2=n1-1
for i in range(1,n1):
    print(" "*(n1-i),"*"*(2*i-(1)),sep="")
for i in range(1,n2):
    print(" "*(1+i),"*"*((n2)-i),"*"*((n2-1)-i),sep="") 