# Example Algorithms

 Here are some example algorithms to see these Python concepts in use.  
 
# ROT13

 ROT13 stands for rotation of 13 values. This means that every character / letter in the plain text will be changed / encrypted to a different character 13 values
 away. 13 is the classic beginning number for a rotation encryption algorithm due to the nature of being able to decrypt the cipher text simply by encrypting the
 cipher text again with the same ROT13 algorithm. This is also known as Symmetric Encryption.

<!-- @[Try it out!]({"stubs": ["py_files/rot13.py"], "command": "py_files/python3 rot13.py"}) -->

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
   

