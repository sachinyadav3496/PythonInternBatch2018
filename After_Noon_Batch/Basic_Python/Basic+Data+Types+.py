
# coding: utf-8

# # Basic Data Types

# 1. Numbers
# 2. String
# 3. List
# 4. Tuple
# 5. Dictionary
# 6. Sets

# In[1]:


# Numbers
# 1. Integers
# 2. Floats
# 3. Complex 
x = 456  # Integer
y = 3.14 #Float
z = 3.14+6j # Complex
print('X = ',type(x),x)
print('Y = ',type(y),y)
print('Z= ',type(z),z)


# In[3]:


x = input("Enter a value : ")
x = int(x)
print("Type of value = ",type(x))
print(x)


# In[4]:


x = 'single quoted string'
y = "double qouted string"
z = """HI 
This is multiline String.
        Define in triple quotes"""
print(x)
print(y)
print(z)


# In[5]:


print("He said,\"Python is Awesome\"")


# In[6]:


print("He said,'Python is Awesome'")


# In[10]:


s = "Python"
k = len(s)
print("Length of Python ",k)
print(s)
print(s[3])
print(s[2])


# In[11]:


s = "Hello World"
print(len(s))
print(s[6:11])


# In[16]:


s = "Python is Interpreted Language"
x = s[10:21]
y = s[:21]
z = s[21:]
p = s[:]
print(s)
print(x)
print(y)
print(z)
print(p)
print(s)


# In[18]:


s = '0123456789'
k = s[::2]
print(k)
l = s[::-1]
print(l)


# In[21]:


s = 'hello world how are you'
print(s[::-1])
print(s[-13:-18:-1])


# In[22]:


x = 'python'
print(dir(x))


# In[23]:


s = "HeLlO WorLd"
k = s.upper()
l = s.lower()
h = s.swapcase()
print(s)
print(k)
print(l)
print(h)


# In[24]:


s = 'PYthon'
doc = s.title.__doc__
print(doc)


# In[26]:


s = "All Dogs are Cat but all Cats are not Dog."
k = s.find('Dog')
print(k)
l = s.replace('Dog','Cat')
print(s)
print(l)


# # LIST

# In[30]:


mylist = [ 5,2,3,56,34,23,46,2] #it can be called array(Homogenous)
mylist1 = [ 'hello',3.14,[1,2,3],12345] #Hetrogenous List
print(*mylist)
print(*mylist1)
k = mylist[3:7]
print(*k)


# In[31]:


l = [ 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(*l[3::3])
print(*l[::-1])
print(*l[::2])
print(*l[-20:-10])
print(*l[-5:-15:-2])


# In[32]:


mylist = [ 1,23,4,123,'hi',45,10,12,66,77,'hello']
print(dir(mylist))


# List Functions 
# 
# Functions that are used to add items into list
# 
# append
# insert
# extend
# 
# Functions that are used delete items from list
# 
# pop
# remove
# 
# Some Common Functions of list
# 
# sort
# revrese
# count
# index
# copy
# clear

# In[34]:


#Functions that are used to add items
#append -> it will add a item at the end of the list use - mylist.append(item)
mylist = [ 1,23,4,23,'hi',45,10,12,66,77,'hello']
print(*mylist)
mylist.append('bye')
print(*mylist)
mylist.append(56)
mylist.append(24)
mylist.append(23)
print(*mylist)


# In[38]:


mylist = [ 1,23,4,23,'hi',45,10,12,66,77,'hello']
print(*mylist)
#1 23 4 23 hi 45 10 12 66 77 hello bye 56 24 23
#insert -> it will take index number and item and add that item to given index
#use = mylist.insert(index,item)
mylist.insert(4,100)
mylist[5] = 23
print(*mylist)
#extend is used to add multiple items


# In[41]:


mylist = [ 1,23,4,23,'hi',45,10,12,66,77,'hello']
mylist.extend('python')
mylist.extend(['hello','world'])
print(mylist)


# In[58]:


mylist = [1, 23,'python', 4, 23, 'hi',23, 45,'hello', 10, 12,23, 66, 77, 'hello', 'p', 'y', 't', 'h', 'o', 'n', 'hello', 'world']
mylist.pop();mylist.pop();mylist.pop()
mylist.pop();mylist.pop();mylist.pop()
mylist.pop();mylist.pop();mylist.pop()
print(mylist)
mylist.pop(2)
print(mylist)
mylist.remove('hi')
mylist.remove('hello')
mylist.remove(23)
print(mylist)
k = mylist.count(23)
mylist.reverse()
print(k)
print(mylist)
mylist1 = mylist.copy()
#mylist1.clear()
mylist1.sort()
print(mylist1)
mylist.sort(reverse=True)
print(mylist)
l = [ 'zello','yellow','hello','challo']
l.sort()
print(l)
l.sort(reverse=True)
print(l)


# In[61]:


l = [ var for var in range(100) ]
print(l)

