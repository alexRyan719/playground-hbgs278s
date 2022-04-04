my_list = []
my_list_of_lists = []

width = 10
height = 10

for num in range(width):
  for n in range(height):
    my_list.append(n)
  my_list_of_lists.append(my_list)
  my_list = []
  
print(my_list_of_lists)
