from random import *
array = [ "1" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9" , "q" , "w" , "e" , "r" , "t" , "y" \
   "u" , "i" , "o" , "p" , "a" , "s" , "d" , "f" , "g" , "h" , "j" \
   "k" , "l" , "z" , "x" , "c" , "v" , "b" , "n" , "m" ,
   ]
password = input ( " guess the password : " )

counter = 0

while True :
    guess = "" . join ( sample ( array , 4 ) )
    if ( guess [0] == password [0] ) and (guess [1] == password [1] ) and ( guess [2] == password [2] ) and ( guess [3] == password [3] ) :
        print ( guess , "==" , password )
        break
    counter += 1
    print ( f" The password entered is not correct for the {counter} th time . Please enter the correct password :" )
