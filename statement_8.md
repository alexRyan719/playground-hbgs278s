# Example Algorithms

 ROT13

 ROT13 stands for rotation of 13 values. This means that every character / letter in the plain text will be changed / encrypted to a different character 13 values
 away. 13 is the classic beginning number for a rotation encryption algorithm due to the nature of being able to decrypt the cipher text simply by encrypting the
 cipher text again with the same ROT13 algorithm. This is also known as Symmetric Encryption


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

      cipher_text = ""
      new_index = 0
      capitalized = False
      new_char = ' '

  
    
      for char in plain_text:
        if char.isupper():
          capitalized = True
        if char.lower() in alphabet_dict:      
          new_index = int(alphabet_dict[char.lower()]) + 13
          if new_index > 26:
            new_index -= 26
          if capitalized:
            cipher_text += number_dict[new_index].upper()
          else:
            cipher_text += number_dict[new_index]
        else:
          cipher_text += char
        capitalized = False
    
    
      return cipher_text

    print(rot13("Uryyb jbeyq!@#$%^&*()_+-=/\\<>?,.~`"))
