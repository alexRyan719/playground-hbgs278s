# Debugging

One of the most frustrating things about learning a new coding language is the debugging. Debugging is the removal of flaws (bugs) in your code. There are a 
couple ways to categorize bugs. 
    
# Syntax Errors

The more obvious bugs are known as Syntax Errors. These happen whenever you misspell something or leave something out. 

@[Try to fix the code!]({"stubs": ["py_files/debug.py"], "command": "python3 py_files/debug.py"})



# Logic Errors

Another type of bug is a Logic Error. These are harder to detect as they don't usually affect your code being able to run. These errors are more with your 
process for the task you're trying to do (aka algorithm). 

The first few lines show an index out of range error. This is pretty common in coding as the index usually starts at 0. 

@[Try to fix the code!]({"stubs": ["py_files/debug_2.py"], "command": "python3 py_files/debug_2.py"})
   
Notice that not only are you not finding the sum of all those numbers added together, you're also mulitplying by 0! 

Another thing to be aware of is PEMDAS (the order of operations in math).


# PEMDAS - Parenthesis Exponent Multiply Divide Add Subtract

If you think that your bug is due to math not being done in the correct order, you can separate out pieces of your equation with parenthesis. 
    
# Rubber Ducks

An important concept in Computer Science is the Rubber Duck. Now, this can really be any inanimate object (or pet even), as long as it doesn't respond. The 
idea is to explain what your code is doing. Also, try explaining it different ways from different angles / points of view. Eventually, the hope is that you 
will discover the flaws / bugs in your code this way. In college, we used to bring real rubber ducks to the CS lab. Nowadays, I use a red octopus, or Roctopus!
