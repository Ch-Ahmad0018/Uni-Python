import random
import string
ans=input("Do you want to code or decode, For code press c for decode press d:")
word=input("Enter the word : ")
if (ans=='c' or ans=='C'):
   
   a=""
   if (len(word)<=3):
      
     for char in word:
         a=char+a
         
   else:
      
    b=word[0]
    a=word[1:]+b
    random_characters_Start = ''.join(random.choice(string.ascii_letters) for _ in range(3))
    random_characters_End  =''.join(random.choice(string.ascii_letters) for _ in range(3))
    a=random_characters_Start+a+random_characters_End
    print(a)

elif (len(word)>=7 and ans=='d' or ans=='D'):
   if (len(word)<=3):
      for char in word:
         a=char+a      
   else:
      a=word
      char=word[:3]
      char2=word[-3:]
      a=a.replace(char,'')
      a=a.replace(char2,'')
      last=a[-1]
      a=a.replace(last,'')
      a=last+a
      print(a)
      
else:
   print("Length of words is less")      




# print(random_characters_Start)
# print(random_characters_End)