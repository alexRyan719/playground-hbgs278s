to_sort = [9,8,7,6,5,4,3,2,1]

print("Just using sorted(), which sorts the list for use but doesn't ACTUALLY sort the data stored in the variable")
print(sorted(to_sort))
print(to_sort)
print()

print("Assigning the sorted version of the list to a new list variable")
sorted_list = sorted(to_sort)
print(sorted_list)
print()

print("Using .sort()")      
to_sort.sort()
print(to_sort)
