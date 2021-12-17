array = [ 1 , 2 , 3 , 4 , 5 , 6 , 7 ]

swap_index = int ( len ( array ) / 2)
if len ( array ) % 2 == 1 : swap_index += 1

for index in range ( 0 , int ( len ( array ) / 2 ) + 1 , 2 ) :

    if ( swap_index + index >= len ( array ) or swap_index - index < 0 ) : break

    temp = array [ swap_index + index ]
    array [ swap_index + index ] = array [ swap_index - index - 1 ]
    array [ swap_index - index - 1 ] = temp
    
print ( array )