def for_loop(n):
  test_str = "Hello World!"
  for char in test_str:
    print(char)

def while_loop(n):
  index = 0
  test_str = "Hello Other World!"
  while index < len(test_str):
    print(test_str[index])
    index += 1
    
def range_for_loop(n):
  for num in range(1,n+1,2):
    print(num)
    
for_loop(10)
while_loop(10)
range_for_loop(20)
