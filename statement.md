# For a video of the creation of this playground, visit YouTube at: https://www.youtube.com/watch?v=X8Vu-nEtMVA

# For the second part video of this playground, visit YouTube here: https://www.youtube.com/watch?v=hCZ4EUrBJC4

@[Try out any of the snippets in this here window!]({"stubs": ["universe.py"], "command": "python3 universe.py"})

# Hello World


   This is the classic "Hello World" program in Python. This will 
   print whatever String (array of chars) you have between the single 
   quotes (' ') or double quotes (" ")
        
        print('Hello World!')

   Formatting is a major part of problem solving with code. String
   manipulation can be done a few ways in python
        
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
