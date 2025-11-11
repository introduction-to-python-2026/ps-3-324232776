def move(my_list, direction):

    if direction == 'right':
        if my_list.index(1) <=2 :
         my_list[my_list.index(1)] = 0
         my_list[my_list.index(1) + 1] = 1

    elif direction == 'left':
        if my_list.index(1) >0 :
         my_list[my_list.index(1)] = 0
         my_list[my_list.index(1) - 1] = 1

    
    return my_list
