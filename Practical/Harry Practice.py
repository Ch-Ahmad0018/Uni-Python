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
# -------------------------------------Kaun bne ga CrorePati game--------------------------------------------------
questions=[["Which language was used For making Facebook?","Python","JavaScript","HTML","PHP","None",4],
           ["Which language was used For making Facebook?","Python","JavaScript","HTML","PHP","None",4],
           ["Which language was used For making Facebook?","Python","JavaScript","HTML","PHP","None",4],
           ["Which language was used For making Facebook?","Python","JavaScript","HTML","PHP","None",4],
           ["Which language was used For making Facebook?","Python","JavaScript","HTML","PHP","None",4],
           ["Which language was used For making Facebook?","Python","JavaScript","HTML","PHP","None",4],
           ["Which language was used For making Facebook?","Python","JavaScript","HTML","PHP","None",4],
           ["Which language was used For making Facebook?","Python","JavaScript","HTML","PHP","None",4],
           ["Which language was used For making Facebook?","Python","JavaScript","HTML","PHP","None",4],
           ]
levels=[100,200,400,800,1000,1500,2000,4000,8000]
money=0
i=0
for i in range(0,len(questions)):
    question=questions[i]
    print(f"Qustion for Rs {levels[i]}")
    print(question[0])
    print(f"a. {question[1]}           b. {question[2]}")
    print(f"c. {question[3]}           d. {question[4]}")
    reply=int(input("Enter your reply between 1 and 4: "))
    if (reply==question[-1]):
        print(f"Congratulation you have won money {levels[i]}")
        if(i==4):
            money=1000
        elif (i==9):
            money=4000
    else:
        print("Wrong Answer")
        break
       
print(f"You have won total of Rs {money}")