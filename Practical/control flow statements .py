#!/usr/bin/env python
# coding: utf-8

# In[4]:


#if else

# name = input("Enter your name:")
# if name == "":
#     print("you did not enter any name")
# else:
#     print("hello", name)


# In[3]:


#while

# name=input("Enter your name")

# while name == "":
#     print("you did not enter any name")
#     name=input("Enter your name")
    
# print("hello", name)


# In[1]:


#while loop another example

# age = int(input("Enter your age: "))

# while age < 0:
#     print("Age cant be negative")
#     age = int(input("Enter your age: "))
    
# print("you are:", age)


# In[ ]:
# In[ ]:
# name=input("Enter your name:")
# while (name==""):
#     print("U did not enter your name")
#     name=input("Enter your name:")

# print("hello"+name)    

age=int(input("Enter your age"))
while age<0:
    print("Age can't be negative")
    age=int(input("Enter your age"))

print("U r "+str(age))

