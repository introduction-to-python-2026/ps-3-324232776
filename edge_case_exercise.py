def move(my_list, direction = None):
   index_of_one=my_list.index(1) # Store the index of 1 once
   if direction == 'right' and index_of_one != len(my_list) - 1:
     my_list[index_of_one] = 0 # Use the stored index
     my_list[index_of_one + 1] = 1 # Use the stored index

   elif direction == 'left' and index_of_one != 0:
      my_list[index_of_one] = 0 # Use the stored index
      my_list[index_of_one - 1] = 1 # Use the stored index

   return my_list
