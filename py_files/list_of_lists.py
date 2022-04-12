my_list = []
my_list_of_lists = []

width = 7
height = 5

for num in range(height):
  for n in range(width):
    my_list.append(n)
  my_list_of_lists.append(my_list)
  my_list = []

for item in my_list_of_lists:  
    print(item)
    print()

x = 0
y = 0

# Try adjusting the coordinates by adjusting x and y. 
print(my_list_of_lists[y][x])

n = 3
n_2 = 2

# Or, you can change n or n_2 to change coordinates.
print(my_list_of_lists[y+n][x+n_2])
