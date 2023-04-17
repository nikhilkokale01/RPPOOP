
class parent:
    def func1(self):
       
        print("This is the parent class")
        
class child(parent):
    def func2(self):
        print("This is the child class")
        
obj1=child()
obj1.func1()
obj1.func2()
        
        
  


# In[23]:


#Multiple inheritance
class Mother:
    def __init__(self,name1):
        self.mother=name1
        
class Father:
    def __init__(self,name2):
        self.father=name2
        
class Son(Mother,Father):
    def __init__(self,name1,name2):
        
        Mother.__init__(self,name1)
        Father.__init__(self,name2)
        print("Mother: ",self.mother)
        print("Father: ",self.father)
        
    
       
boy=Son("Savita","Karan")


# In[21]:


#Multi-level inheritance

class Grandfather:
    def __init__(self,grandfather):
        self.grandfathername=grandfather

        

class Father(Grandfather):
    def __init__(self,father,grandfather):
        self.fathername=father
        Grandfather.__init__(self,grandfather)
        

    
    
class Son(Father):
    def __init__(self,grandfather,father,son):
        self.sonname=son
        Father.__init__(self,father,grandfather)
        
   
    
    def printn(self):
        print("Grandfather: ",self.grandfathername)
        print("Father: ",self.fathername)
        print("Son: ",self.sonname)
        
child=Son("Shyam","Ram","Gopal")
child.printn()


# In[25]:


#Hierarchical inheritance
class A:
    def func(self):
        print("This is base class named as A")
        
class B(A):
    def func1(self):
        print("This is child class B which inherites the functions of A")
        
class C(A):
    def func2(self):
        print("This is child class C whilch inherites the functions of A")
        
name1=B()
name2=C()
name1.func1()
name1.func()
name2.func2()
name2.func()


# In[33]:


#Hybrid inheritance
class A:
    def func(self):
        print("This is base class named as A")
        
class B(A):
    def func1(self):
        print("This is child class B which inherites the functions of A")
        

        
class D(B,A):
    def func2(self):
        print("This class D inherites properties of both A and B")
        
        
name1=D()

name1.func()
name1.func1()
name1.func2()


        


# In[ ]:





# In[ ]:





# In[ ]:




