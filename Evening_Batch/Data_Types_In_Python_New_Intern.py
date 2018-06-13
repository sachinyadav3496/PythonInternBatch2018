
# coding: utf-8

# <h1 style='color:green' >Basic Data Types in Python</h1>

# ![Title](data_type.png)

# 1. Numbers
# 2. Strings
# 3. Lists
# 4. Tuples
# 5. Dictionary
# 6. Sets

# In[3]:


#Numbers
#Intergers
x = 5 # the x is a container which will contain a integer number 5
#let's pring type of x
print("Type of x = ",type(x))
#Floats
y = 6.25 # Now y will a float type container which holds value 6.25
#let's print type of y 
print("Type of y = ",type(y))
#Complex
z = 6+5j #here j denotes complex number and it will store in z
#let's print type of Z
print("Type of Z = ",type(z))
#Now print all values
print("Value of X = ",x)
print("Value of y = ",y)
print("Value of z = ",z)


# In[1]:


#Strings -> String is group of or collection of charcters
#By default python supports utf-8 charcter set
s = 'hi I am string.' #string can be define in single quotes
s1 = "Hi I am also String." #or it can be in double quotes
s3="""HI I am a Paragraph.
                            You see have multiple lines.
So you can write your paragraph.
    As you wish in python.
    
                by Python Strings
"""
print(type(s))
print(s)
print(s1)
print(s3)


# In[6]:


newstring = "He said, \"She is Beautiful.\"" #C way
print(newstring)


# In[5]:


newstring1 = 'He said, "She is Beautiful."'
print(newstring1)


# In[7]:


s = "Hello world"
print("Total Charcters in String s is ",len(s))


# In[9]:


one_char = s[6]
print(one_char)
same_char = s[-5]
print(same_char)


# In[2]:


#slicing s[start:end:step]
s = "Hello World"
c = s[6:11]
x = s[-5:]
print(s)
print(c)
print(x)


# In[3]:


y = s[::-1]
print(y)


# In[4]:


z = s[:-1]
print(z)


# In[5]:


p = s[::2]
print(p)


# In[6]:


s = "Hello Word"
print(type(s))


# In[7]:


import this


# In[16]:


s = "Hello World"
print(dir(s))


# In[17]:


# . is known as access specifier
x = s.center.__doc__
print(x)


# In[21]:


y = s.center(550,'-')
print(y)


# In[22]:


s = "HeLLo WoRlD!!"
u = s.upper()
l = s.lower()
k = s.swapcase()
print("s.upper() = ",u)
print("S.lower() = ",l)
print("s.swapcase() = ",k)


# In[23]:


s = "         HeLLo WoRLd!!        "
k = s.strip() #both leading and trailing spaces removed
l = s.lstrip() #remove leading spaces
r = s.rstrip() #remove trailing spaces
print("String is  - '{}'".format(s))
print("After Strip String is - '{}'".format(k))
print("After Lstrip String is - '{}'".format(l))
print("After Rstrip String is - '{}'".format(r))


# In[33]:


s = "Every dog is not a real dog."
x = s.find("dog")#return pos (index) where pattern firest match
print(x)
y = s.find("cat")#return -1 if there is no pattern found in string
print(y)
z = s.replace("dog","DOG") # replace old patterns with new pattern
print(s)
print(z)
sm = s.partition('dog')
ms = s.split('dog')
print(sm)
print(ms)
c = s.count('dog')
print(c)


# In[27]:


s = "All cat's are not cat but all dogs behaving like cat's"
x = s.replace("cat","dog")
print(s)
print(x)


# In[34]:


s = "Hello World Welcome to python"
x = s.split() #by default split string from spaces
y = s.partition('World') #Will partition string from world
print(x)
print(y)
abc = '-'.join(x)
print(abc)


# In[38]:


s = "abcd"
k = '^--^'.join(s)
print(k)
s = "Hello World"
print(s)


# <h1 style='color:gray' >List Data Type in Python</h1>

# list is a collection of homogenous or hetrogenous data elements.
# All arrays are list but all list are not arrays.
# 

# In[40]:


mylist = [ 34, 4, 542, 43, 2324, 63423, 2345, 432334,] #list initlization
#This is homogenous list can be called as interger array
mylist1 = [ "Hello", "World","Welcome","to","python","list" ]
#indexing, slicing
print(mylist)
print(mylist1)


# In[42]:


s = mylist[5]
print(s)
print(len(mylist1))


# In[43]:


y  = mylist1[2:6]
print(y)


# In[44]:


x = mylist1[:3]
print(x)


# In[45]:


l = [ 1,2,3,4,5,6,7,8,9]
r = l[::-1]
print(r)


# In[47]:


d2 = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]
print(d2[1][1])


# In[48]:


print(dir(l))


# Built-in Functions to add items in list
# 1. mylist.append(item)
# 2. mylist.insert(index,item)
# 3. mylist.extend(seq)

# In[49]:


#mylist.append(item) -> it will add item into list mylist at the end
mylist = [ 'hello',1,2,3.14,]
print(mylist)
mylist.append(5)
mylist.append('world')
mylist.append([1,2,3,4,5,6])
print(mylist)


# In[51]:


#mylist.insert(index,item)
mylist = [ 1,5,3,324,21,'hello','hi']
mylist.insert(3,'bye') #[1,5,3,'bye',324,21,'hello','hi']
mylist.insert(0,'python')#['python',1,5,3,'bye',324,21,'hello','hi']
mylist.insert(-2,3.14) #['python',1,5,3,'bye',324,21,3.14'hello','hi]
print(mylist)


# In[52]:


l = [ 1,'hello',5,8]
l.extend('python')
print(l)


# In[53]:


l = ['hello','hi','bye',1,2,3]
l.extend(['python','java','c','c++',3.14])
print(l)


# In[55]:


k = [1,2,3]
p = [4,5,6]
k.extend(p)
print(k)
p.append(k)
print(p)


# Built-in List Function to remove a item for list mylist
# 1. mylist.pop() -> will las element from list ( opposite of append) and return deleted item
# 2. mylist.pop(index) -> will delete item from mylist which position at index no index
# 3. mylist.remove(item) -> will search occurence of item and delet first occurence of item from list

# In[57]:


l = [ 1,2,3,4,5,6,7,8,9,10]
print(l)
item1 = l.pop()
item2 = l.pop()
item3 = l.pop(0)
item4 = l.pop(4)
print("Item1 ",item1)
print("Item2 ",item2)
print("Item3 ",item3)
print("Item4 ",item4)
print(l)


# In[59]:


#remove
l = [ "hello",1,2,3,"python",75,"java"]
l.remove("python")
print(l)
l.remove(75)
print(l)


# In[63]:


l = [ 1,2,3,1,2,3,1,2,3]
#mylist.count(item) -> return a num which show repeatation 
#of item in list
one = l.count(1)
two = l.count(2)
three = l.count(3)
print("one ",one)
print("two ",two)
print("three ",three)
l.remove(1)
l.remove(2)
l.remove(3)
one = l.count(1)
two = l.count(2)
three = l.count(3)
print(l)
print("one ",one)
print("two ",two)
print("three ",three)


# other function of list sort, reverse, index, clear

# In[65]:


l = [ 23,34,231,1,5,46,53,432]
l.sort()
print(l)
l.sort(reverse=True)
print(l)
l = [ "hello","abc","good to go","let's see","what happens"]
l.sort()
print(l)
l.sort(reverse=True)
print(l)


# In[69]:


l = [ "hello","hi","bye","bye bye"]
l.reverse()
print(l)
l.sort()
print(l)
l.clear()
print(l)


# In[70]:


l = [ 1,2,3,"hello","hi","bye",1,2,3,"Hello","hi","bye"]
x  = l.index("hello")
y = l.index(3)
print(x)
print(y)


# In[86]:


l = [1,2,3,4]
s = "Hello World"
print(l)
print(s)
print(*l)
print(*s)
l[2] = "python"
print(l)


# Tuple is immmutable data type 

# In[71]:


k = ( 1,2,3,'hello','hi')
print(type(k))
print(dir(k))


# In[78]:


x = 1234
print(dir(x))
print(x.__sizeof__())
print(x.bit_length())


# In[79]:


mydict = {
    'key':'value',
    'name':'python',
    'year':1991,
    'frame works':['Django','Flask','Web2py']
}
print(type(mydict))
print(mydict)
print(dir(mydict))


# In[81]:


l = [ 1, 2, 3, 4]
k = l
j = l.copy()
print(l)
l.insert(0,'hello')
l.append('hi')
l.append('bye')
print(l)
print(k)
print(j)


# In[83]:


info = { 
        'name':'hari',
        'age' : 21,
        'language': 'hindi',
        'skills' : ['linux','python','r','sql'],
        'country' : 'india'
        }
print(dir(info))
print(info)


# In[85]:


print("Name = ",info['name'])
print("skils = ",*info['skills'])


# In[88]:


print(info['name'])
info['name'] = 'python'
print(info['name'])


# In[89]:


info['address'] = 'jaipur'
print(info)


# In[90]:


print(*info)


# In[91]:


print(dir(info))


# In[92]:


x = info.get('name')
print(x)


# In[96]:


y = info.get('shorcut')
print(y)


# In[97]:


print(info.keys())


# In[98]:


print(info.values())


# In[99]:


print(info.items())

