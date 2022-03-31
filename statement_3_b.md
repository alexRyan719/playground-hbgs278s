# Functions

  Functions are sections of code that are meant to accomplish one (or few) action(s). Functions are used to organize code, as well as allow for modularity. Modularity
  means that code can be reused with little to no adjustments. 
  
  When defining a function, you start with the keyword "def", followed by the name of the function and attached parameters / arguments for the function, and finally a 
  colon (:). Any code that is meant to be contained in the function needs to be indented one indent further than the function declaration line. 
  
  @[Try changing the values for each of the functions!]({"stubs": ["functions.py"], "command": "python3 functions.py"})


    def multply(a, b):
      return a*b

  In this example, the declaration line is "def multiply(a, b):". This means that we have a function named "multiply" that takes two arguments, "a" and "b". The next
  line returns the value of the two input arguments when they are multiplied together (or the product of the two inputs). 
  
  To call a function, we would do something like this:
  
    multiply(2, 5)
    
  Notice that you don't actually see anything in your terminal / output. This is because the nature of this function simply multiplies the arguments and returns
  the product. If we want to see what value is returned from this function, we would need to either print our call to that function, or add print functionality
  within the function. 
  
    print(multiply(2, 5)
    
  Or
  
    def multply(a, b):
      print(a*b)
      return 0
      
  Either way, we need to define our function BEFORE we try to call it / envoke it / run it. The compiler / interpreter / computer reads our code top down, left to right.
  This means that if we try to call our function before we define it, we will get an error. The computer doesn't know what we're talking about and will ask us to 
  clarify. 
