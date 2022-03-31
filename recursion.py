test_str = "Hello World!"

def recurse_this(n):
  if n == -1:
    print(test_str[10 - n])
    print("This is the base case!")
  else:
    print(test_str[10 - n])
    #print("iteration: " + str(n))
    recurse_this(n-1)

recurse_this(len(test_str))
