number_1 = int ( input ( "number : " ) )
number_2 = number_1 - 1
for i in range ( 1 , number_1 ) :
    print( " " * ( number_1 - i ) , "*" * ( 2 * i - ( 1 ) ) , sep = "" )
for i in range ( 1 , number_2 ) :
    print( " " * ( 1 + i ) , "*" * ( ( number_2 ) - i ) , "*" * ( ( number_2 - 1 ) - i ) , sep = "" ) 
