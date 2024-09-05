from random import *
entekhab = ["sang","kaghaz","gheychi"]
emp,emk=0,0
n=int(input("emtias bord ra vared konid : "))
while emp<n and emk<n :
    print("---------------------------------------------------------------------")    
    entp=input(f"entekhab konid {entekhab} :")
    entk=choice(entekhab)
    if ( entk == "sang" and entp == "gheychi" ) or ( entk == "kaghaz" and entp == "sang" ) or ( entk == "gheychi" and entp == "kaghaz" ) :
        emk=+1
    elif ( entp == "sang" and entk == "gheychi" ) or ( entp == "kaghaz" and entk == "sang" ) or ( entp == "gheychi" and entk == "kaghaz" ) : 
        emp+=1
    else :
        print("emp" ,"==","emk")   
    print(f"emp== {emp}   entp=={entp} , emk=={emk} entk=={entk}") 
    print("---------------------------------------------------------------------")    
if emp==n:
    print("***********************win player*****************")
else :
    print("****************win pc ****************")        