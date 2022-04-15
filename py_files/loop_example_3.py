vowels = "aeiouAEIOU"
my_str = "This is my string!"
vowel_count = 0

for char in my_str:
  if char in vowels:
    vowel_count += 1
    
print(vowel_count)


