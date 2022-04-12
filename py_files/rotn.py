def rot_n(plain_text, n):
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
      new_index = int(alphabet_dict[char.lower()]) + n
      if new_index > 26:
        new_index %= 26
      if new_index < 1:
        new_index %= 26
        new_index += 26
      if capitalized:
        cipher_text += number_dict[new_index].upper()
      else:
        cipher_text += number_dict[new_index]
    else:
      cipher_text += char
    capitalized = False
    
  return cipher_text

print(rot_n("Uryyb jbeyq!@#$%^&*()_+-=/\\<>?,.~`", 14))
print(rot_n("Ifmmp xpsme!@#$%^&*()_+-=/\\<>?,.~`",-1))
print(rot_n("Hello world!@#$%^&*()_+-=/\\<>?,.~`",12))
print(rot_n("Tqxxa iadxp!@#$%^&*()_+-=/\\<>?,.~`",14))
