my_str = "Hello, ThIs Is A mUcH lOnGeR sTrInG"
upper_case_count = 0

for char in my_str:
  if char.isupper():
    upper_case_count += 1
    
print(upper_case_count)
