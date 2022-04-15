


# Hello World


   This is the classic "Hello World" program in Python. This will 
   print whatever String (array of chars / group of letters) you have between the single (' ') or double quotes (" ")
        
@[Hello World!]({"stubs": ["py_files/hello_world.py"], "command": "python3 py_files/hello_world.py"})

   Being able to print output is very important in coding. You can use print statements to see the values of variables, if sections of code are being executed,
   or the results of your algorithm.

   Formatting is a major part of problem solving with code. String
   manipulation can be done a few ways in Python
        
        print("Hello! " * 3)
        
   For the rest of the examples, let's declare a String variable to use

        test_string = "Hello World, but now our new string!"

   Slicing is where you target or work with only parts of a string.
   To do this, use square brackets ([]). Within the square 
   brackets you can set the start, stop, and step. Or in other 
   words, the starting point, ending point, and how much to count by
        
        print(test_string[1:6])

   Print every other letter
        
        print(test_string[::2])

   Reverse the string
        
        print(test_string[::-1])

   Print single char at a certain index 
        
        print(test_string[0])

   This also works backwards with a negative index
        
        print(test_string[-1])
        print(test_string[-5])

   Set the start point as the fifth character from the end
        
        print(test_string[-5:])
        print(test_string[-10:-3])
        

@[Try them!]({"stubs": ["py_files/hello_other_world.py"], "command": "python3 py_files/hello_other_world.py"})


