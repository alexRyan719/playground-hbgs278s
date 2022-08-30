# Example Algorithms

 Here are some example algorithms to see these Python concepts in use.  
 
# BUG BOUNTY ------------------------------------------------------------------------------------------
 There isn't any monetary reward, BUT I will cite you for the fix here in the playground! 
 
# ROT13

 ROT13 stands for rotation of 13 values. This means that every character / letter in the plain text will be changed / encrypted to a different character 13 values
 away. 13 is the classic beginning number for a rotation encryption algorithm due to the nature of being able to decrypt the cipher text simply by encrypting the
 cipher text again with the same ROT13 algorithm. This is also known as Symmetric Encryption.

# Bug In Progress
  6-16-22 Apologies, but it seems this code stub has a bug. I am looking into it, but there is a workaround! Copy and paste the code from this one into the other 
  code stub and it functions as expected. You will need to completely overwrite the second code stub's code with this first one. Also, apologies for the messy
  spacing and this has since been fixed. 

# Click "Reset Code" to get the original code example back.

# END OF BUG BOUNTY ------------------------------------------------------------------------------

@[Try it out!]({"stubs": ["py_files/rot13.py"], "command": "py_files/python3 rot13.py"})

  The concept of a circular array is demonstrated with these lines:
  
    if new_index > 26:
        new_index -= 26
        
   So, even if the new index is too large to find the corresponding cipher text character, the index is adjusted to create the illusion of a circular array.
   A better (and more scalable) way to do this would be to use the modulo operator (%) to ensure any number, no matter how large, would be able to yield a 
   corresponding cipher text character.
   
    if new_index > 26:
        new_index %= 26

# Rot N

   13 is the most common value, as it allows for Symmetric Encryption. However, it's fairly simple to change this algorithm to accept any value for the rotation. To
   account for larger values, we need to change the index modification to the modulo style. 
   
@[Try it out!]({"stubs": ["py_files/rotn.py"], "command": "python3 py_files/rotn.py"})
   
# Generate Character Messages via a Message Dictionary && Calculating a Message Code

    Say you want to cut down on the time taken with repetitive messages you want your game characters to say to the player. You could do this by using a dictionary to return a message based on an input value.

@[Try it out!]({"stubs": ["py_files/msg_dict.py"], "command": "python3 py_files/msg_dict.py"})

    You can also add the complexity of Holiday Based messages, Region Based messages, and many more!

@[Try it out!]({"stubs": ["py_files/msg_sel.py"], "command": "python3 py_files/msg_sel.py"})


