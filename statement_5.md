# Loops

   Loops are very useful when needing to do the same action 
   multiple time (iterations). For loops are usually better when 
   the amount of iterations is known and while loops are usually
   better when the number of iterations is not known. 
   
   However, you can pretty much do any process (algorithm) with 
   either style of loop. You can also use recursion.

   Iterate through every char in a string
        
    test_str = "Hello World!"
    for char in test_str:
        print(char)

   Indexes are used to keep track of what we're working with for
   each iteration. With while loops, you have to manually change
   the index. Be careful, infinite loops are created when a 
   terminating condition is never met. IE the index never changes,
   a count never changes, or whatever condition we decide for the 
   loop. 
     
    index = 0
    while index < len(test_str):
      print(test_str[index])
      index += 1

   In other languages, there are do while loops. However,
   Python doesn't use them without some extra effort. 

@[Try em out here!]({"stubs": ["loops.py"], "command": "python3 loops.py"})

   
