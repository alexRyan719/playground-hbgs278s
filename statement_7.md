# Data Structures

  Data structures are objects, which means they are more complex variables. All objects can technically be considered data strucures, as they can hold more data than
  primitive variable. However, most Computer Scientists are referring to objects like Lists / Arrays, Dictionaries, Trees, Graphs, Etc when discussing data structures.
  
  Arrays are groups of primitive variables all stored together. In Python, we refer to these as lists. Here are a couple of examples of lists:
  
    example_list = []
    
    example_list_2 = [1,2,3]
    
    example_list_3 = ['a','b','c']
    
    example_list_4 = [1, 'b', 3]

  To add elements to a list, use the .append() function. To access specific items in a list, you can use an index. 

@[Try adding, accessing, and removing elements from this list!]({"stubs": ["py_files/list.py"], "command": "python3 py_files/list.py"})

  To sort a list, use the .sort() or sorted() functions. 

@[Try adding, accessing, and removing elements from this list!]({"stubs": ["py_files/list_sort.py"], "command": "python3 py_files/list_sort.py"})


  Dictionaries are Python's answer to Switch Statements. The logic of a dictionary is to return a value based on an input value / key. In other languages, Switch 
  Statements are used to accomplish similar logic. Here are a couple examples of dictionaries:
  
    alphabet_dict  = {
      'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10
      ,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18
      ,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26
    }
    
    number_dict  = {
      1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h',9:'i',10:'j'
      ,11:'k',12:'l',13:'m',14:'n',15:'o',16:'p',17:'q',18:'r'
      ,19:'s',20:'t',21:'u',22:'v',23:'w',24:'x',25:'y',26:'z'
    }

  Dictionaries are created in a similar way to lists. 

@[Try adding, accessing, and removing elements from this dictionary!]({"stubs": ["py_files/dict.py"], "command": "python3 py_files/dict.py"})

# Lists of Lists

2D Arrays are commonly used in coding. In Python, this can be thought of as a list of lists. 

@[Try accessing and setting different values in the list of lists!]({"stubs": ["py_files/list_of_lists.py"], "command": "python3 py_files/list_of_lists.py"})

