def rot13(plain_text):
    
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

    # other_dict = {
    #     0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9'
    #     ,10:':',11:';',12:'<',13:'=',14:'>',15:'?',16:'@',17:'!',18:'"'
    #     ,19:'#',20:'$',21:'%',22:'&',23:'\'',24:'(',25:')'
        
    # }

    # other_other_dict = {
    #     0:'*',1:'+',2:',',3:'-',4:'.',5:'/'
    # }

    found = False
    #found_2 = False
    cipher_text = ""
    new_index = 0
    capitalized = False
    new_char = ' '
  
    for char in plain_text:

        # Check for capitalization and set capitalized accordingly 
        if char.isupper():
            capitalized = True

        # Check if char is in alphabet_dict and assign index if so
        if char.lower() in alphabet_dict:      
            new_index = int(alphabet_dict[char.lower()]) + 13
            found = True

        # If the char is in other_dict, set found_2 to True
        # if char.lower() in other_dict:      
        #     #new_index = int(alphabet_dict[char.lower()]) + 13
        #     found_2 = True
        
        # If the new index is larger than 26, wrap around from the beginning
        if new_index > 26:
            new_index %= 26

        # Build the return string based on if capitalized and found
        if capitalized and found:
            cipher_text += number_dict[new_index].upper()
        elif found:
            cipher_text += number_dict[new_index]
        else:
            cipher_text += char


        
        # elif found2:
        #     print("It's found2")
            
        # else:
        #     if char in other:
        #         print(ok)
        #     elif char in other_2:
        #         print(ok)
        #     else:
        #         cipher_text += char
        
        capitalized = False
        found = False
        #found_2 = False
    #print("DEBUG")
    
    return cipher_text

print(rot13("Uryyb jbeyq!@#$%^&*()_+-=/\\<>?,.~`"))
print(rot13("Hello world!@#$%^&*()_+-=/\\<>?,.~`"))
      
