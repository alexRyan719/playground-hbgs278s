# Recursion

   To demonstrate recursion, we need to define a function. The 
   concept is where we have a function that calls itself until
   a condition is met. It's also easy to write infinite loops
   with recursion

    def recurse_this(n):
      if n == -1:
        print(test_str[10 - n])
        print("This is the base case!")
      else:
        print(test_str[10 - n])
        #print("iteration: " + str(n))
        recurse_this(n-1)

    recurse_this(len(test_str))
