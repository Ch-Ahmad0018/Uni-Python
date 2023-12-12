#============================================= Classes and Objects
# class ahmad:
#     a=10
#     def sum(self):
#         print(20+30)

# obj=ahmad()
# print(obj.a)
# obj.sum()    
# =============================================Show Value 
# class OriginalClass:
#     a=10
#     def showvalue(self):
#         print(self.a)
    
# obj=OriginalClass()
# obj.showvalue()     
# =============================================Show value 2 Functions
# class originalClass:
#     a="Welcome to Pakistan"
#     def showValue(self):
#         print(self.a)
#     def showValue1(self):
#         print("Welcome to India")
# obj=originalClass()
# obj.showValue()
# obj.showValue1()            
# --------------------------------------------Constructor
# class originalClass:
#     def __init__(self):
#         print("Welcome to Pakistan")
#     def showValue(self):
#         print("Welcome to India")
# obj=originalClass()
# obj.showValue()            

# -------------------------------------------Inheritance
# class A:
#     def showValue(self):
#         print("Welcome to India")
# class B(A):
#        def __init__(self):
#            print("Chaudhry")
           
#        def showValue1(self):
#         print("Welcome to I")     
# obj=B()
# obj.showValue()
# obj.showValue1()   
#  ---------------------------------------MultiLevel Inheritance
# class A:
#     def showValue(self):
#         print("Welcome to Pakistan A")
# class B(A):
#     def showValue2(self):
#          print("Welcome to Pakistan B")
# class C(B):
#     def showValue3(self):
#         print("Welcome to Pakistan c")               
# obj=C()
# obj.showValue()
# obj.showValue2()
# obj.showValue3()
#-------------------------------------------multiple inheritance
#-------------------------------------------use c directly from B and A
#-------------------------------------------inherit B,A directly to C   
# class A:
#     def showValue(self):
#          print("Welcome to Pakistan A")
# class B():
#     def showValue2(self):
#          print("Welcome to Pakistan B")
# class C(A,B):
#     def showValue3(self):
#         print("Welcome to Pakistan c")               
# obj=C()
# obj.showValue()
# obj.showValue2()
# obj.showValue3()    
# -----------------------------------------Private Variable
# class A:
#     __name="Ali"
#     def __init__(self):
#         print(self.__name)
# obj=A() 
# print(obj.__name)   
#--------------------------------------Private method
# class A:
#     __name="Ali"
#     def __init__(self):
#         print(self.__name)
#         self.__printName()
#     def __printName(self):
#         print("Welcome to Pakistan")    
# obj=A() 

# class A:
#     __value=23
#     def __init__(self):
#         print(self.__value)
#         self.__showValue()
#     def __showValue(self):
#         print("Chaudhry Ahmad Mubashir")  
# obj=A()
# obj.__showValue()     Agar simple function hota to aise print ho jata   

# --------------------------------------Encapsulation 

# class A:
#     def __init__(self):
#         self.__name=""
#     def setName(self,name):
#         self.__name=name
#     def getName(self):
#         return self.__name

# obj=A()
# obj.setName("Coding in Python")
# name=obj.getName()
# print(name)    

# class A:
#     def __init__(self):
#         self.name=""
#     def setName(self,name):
#         self.name=name
#     def getName(self):
#         return self.name

# obj=A()
# obj.setName("Chaudhry AHmad")
# name=obj.getName()
# print(name)            

# class A:
#     def __init__(self):
#         self._title=""
#     def setTitle(self,title):
#         self._title=title
#     def getTitle(self):
#         return self._title
# obj=A()
# obj.setTitle("Introduction to Python")
# hello=obj.getTitle()
# print(hello)

# class A:
#     def __init__(self,radius):
#         self._radius=radius

#     def setRadius(self,newradius):
#         self._radius=newradius
#     def getRadius(self):
#         return self._radius
# obj=A(5)
# print(obj.getRadius()) 
# obj.setRadius(9)
# print(obj.getRadius())  

# -----------------------------------------Polymorphism
# ----------------------------------------Method Overloading
# l=[10,20,30]
# print(len(l))
# s="Chaudhry"
# print(len(s))

# class A:
#     def display(self,name):
#         print("Hello World "+ name)
# obj=A()
# obj.display("Chaudhry")       

# ---------------------------------------Method Over riding

# class A:
#     def showValue(self):
#         print("wELCOME TO pAkistan")
# class B(A):
#     def showValue(self):
#         print("Welcome to India")

# obj=B()
# obj.showValue()      

class A:
    def showValue(self):
        print("wELCOME TO pAkistan")
class B(A):
    def showValue(self):
        super().showValue()
        print("Welcome to India")

obj=B()
obj.showValue()

         