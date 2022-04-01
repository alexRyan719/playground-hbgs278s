example_dict = {}
#to_add = 


letter_dict = {}
alphabet = "abcdefghijklmnopqrstuvwxyz"

for char in alphabet:
  if char in letter_dict:
    letter_dict[char] += 1
  else:
    letter_dict[char] = 1
    
print(letter_dict)
