# -------------------------------------Exception Handling----------------------------------
# a=input("Enter the number: ")
# print(f"Multiplication table of {a} is : ")
# try:
#   for i in range(1,11):
#     print(f" {int(a)} * {i} = {int(a)*i}")

# except Exception as e:
#   print(e)    


# Another Error
# try:
#   num=int(input("Enter an integer:"))
#   a=[6,3]
#   print(a[num])

# except ValueError:
#     print("Number entered is not an integer")
#     # We can use multiple exceptions
# except IndexError:
#     print("Index Error")    


# -------------------------------------------Finally Keyword-----------------------------------------------
# -------------------------------------------Simple------------------------------------------------------
# def funct1():
#     try:
#         l=[1,5,6,7]
#         i=int(input("Enter the index: "))
#         print(l[i])
        
#     except:
#         print("Some error occured")

    
#         print("I am always executed")


# x=funct1()
# print(x)
# # ------------------------------------------Why finally to use---------------------------------------------
# def funct1():
#     try:
#         l=[1,5,6,7]
#         i=int(input("Enter the index: "))
#         print(l[i])
#         return 1
#     except:
#         print("Some error occured")
#         return 0
    
#         print("I am always executed")


# x=funct1()
# print(x)
# # -----------------------------------------How to use-------------------------------------------------------
# def funct1():
#     try:
#         l=[1,5,6,7]
#         i=int(input("Enter the index: "))
#         print(l[i])
#         return 1
#     except:
#         print("Some error occured")
#         return 0
#     finally:
#         print("I am always executed")

# x=funct1()
# print(x)

# ----------------------------------------Custom Errors--------------------------------------------------------
# a=int(input("Enter any number between 5 and 10:"))
# if(a<5 or a>9):
#     raise ValueError("Value should be between 5 and 9")

# practice
# a=input("Enter any string:")
# if(a=='quit'):
#     print("Hello")
# else:
#     raise ValueError("Value should be quit")    

# -----------------------------------for loop with else statement-----------------------------------------------
# ---------------------------------------i----------------------------------------------------------------------
# for i in range(6):
#     print(i)
    
# else:
#     print("Sorry no i")    
# #  Else Statement get executed

# # ---------------------------------------ii----------------------------------------------------------------------
# for i in range(6):
#     print(i)
#     if(i==4):
#         break
    
# else:
#     print("Sorry no i")
# # Else statement does not execute because loop break

