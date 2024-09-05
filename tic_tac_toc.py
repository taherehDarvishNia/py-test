from random import choice
choices=[1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9]
ent=[1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9]
Turn=1


def choiceplayer () :
    choice_player=int(input(f" Choose from the options : {ent} : "))
    x=choices.index(choice_player)
    choices.insert(x,"O")
    del choices [x+1]
    del ent [ent.index(choice_player)]

def choicepc () :
    choice_pc=choice(ent)  
    x=choices.index(choice_pc)
    choices.insert(x,"X")
    del choices [x+1]
    del ent[ent.index(choice_pc)]

def show () :
    j=0
    print(" - - - - - - -")
    for i in  choices:
        j+=1  
        print(" |",i,end="")
        if(j%3==0) :
            print(" |")
            print(" - - - - - - -")

            
def Score_pcs  () :
    if choices[0]==choices[1]==choices[2]=="X":
        return 1
    elif choices[3]==choices[4]==choices[5]=="X":
        return 1
    elif choices[6]==choices[7]==choices[8]=="X":
        return 1        
    elif choices[0]==choices[3]==choices[6]=="X":
        return 1
    elif choices[1]==choices[4]==choices[7]=="X":
        return 1
    elif choices[2]==choices[5]==choices[8]=="X":
        return 1
    elif choices[0]==choices[4]==choices[8]=="X":
        return 1
    elif choices[2]==choices[4]==choices[6]=="X":
        return 1
    else :
         return 0      

def Score_players  () :
    if choices[0]==choices[1]==choices[2]=="O":
        return 1
    elif choices[3]==choices[4]==choices[5]=="O":
        return 1
    elif choices[6]==choices[7]==choices[8]=="O":
        return 1        
    elif choices[0]==choices[3]==choices[6]=="O":
        return 1
    elif choices[1]==choices[4]==choices[7]=="O":
        return 1
    elif choices[2]==choices[5]==choices[8]=="O":
        return 1
    elif choices[0]==choices[4]==choices[8]=="O":
        return 1
    elif choices[2]==choices[4]==choices[6]=="O":
        return 1
    else:
        return 0        


while  True :
    try :
        choiceplayer()
        if Turn!=5 :
             choicepc()
        show()
        if Score_pcs()==1:
            print("\n*** win pc ***\n" )
            break
        if Score_players()==1 :
            print("\n*** win player ***\n" )
            break
        Turn+=1
        if Turn>5:
           print("\n___ very equal ___\n")
           break
    except :
        print("\n\n" , "  << Please be careful and enter correctly >>  ","\n\n" )
