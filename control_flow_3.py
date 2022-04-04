my_int = 5

if my_int < 10 and my_int > 0:
  print("It's between 0 and 10")

my_char = 'c'
to_search = "Does this string have your letter?"

if my_char not in to_search:
    print("Nope, my char is not in there!") 

if my_char not in to_search or 1:
    print("Either part can be true") 

if my_char not in to_search or 1 or my_int < -1000:
    print("You can have as many conditionals as you want!")  
