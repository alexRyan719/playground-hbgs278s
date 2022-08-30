# Loops

Loops are very useful when needing to do the same action 
multiple time (iterations). For loops are usually better when 
the amount of iterations is known and while loops are usually
better when the number of iterations is not known. 
   
However, you can pretty much do any process (algorithm) with 
either style of loop. You can also use recursion.

Iterate through every char in a string

@[Try changing the string!]({"stubs": ["py_files/loops.py"], "command": "python3 py_files/loops.py"})

Indexes are used to keep track of what we're working with for
each iteration. With while loops, you have to manually change
the index. Be careful, infinite loops are created when a 
terminating condition is never met. IE the index never changes,
a count never changes, or whatever condition we decide for the 
loop. 
     
@[Try adjusting the index!]({"stubs": ["py_files/loops_2.py"], "command": "python3 py_files/loops.py"})

In other languages, there are do while loops. However,
Python doesn't use them without some extra effort. 

You can also use the range() function to set a start, stop, and step for your for loops. This is similar to the start, stop, and step of string slicing.

Start is the initial value that the loop range will start at.

Stop is the end limit that the loop value will reach in the range.

Step is the amount that the loop will count by. 

@[Try changing n!]({"stubs": ["py_files/loops_3.py"], "command": "python3 py_files/loops_3.py"})

Here is a nifty way to demonstrate Multiplication and Division as loops of Addition and Subtraction!

@[Try me!]({"stubs": ["py_files/loops_4.py"], "command": "python3 py_files/loops_4.py"})

   
