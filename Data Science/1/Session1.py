#!/usr/bin/env python
# coding: utf-8

# ![0.jfif](attachment:0.jfif)

# Data Types

# Numbers

# In[7]:


1 + 1


# In[8]:


5 - 2


# In[9]:


2 * 3


# In[10]:


8 / 4


# In[11]:


2 ** 3


# In[12]:


9 / 3


# In[13]:


9 % 3


# In[15]:


8 / 5


# In[14]:


8 % 5 


# In[16]:


8 // 5


# In[17]:


2 + 3 * 5 + 5


# In[18]:


(2 + 3) * (5 + 5)


# Variables

# In[19]:


name_of_var = 2


# In[20]:


x = 2
y = 3


# In[21]:


z = x + y


# In[22]:


z


# String

# In[23]:


'Single Quotes'


# In[24]:


"Double Quotes"


# In[26]:


"Wrap lot's of other quotes"


# In[27]:


s = "Sahand"


# In[28]:


s[0]


# In[29]:


s[1]


# In[30]:


s[2]


# In[31]:


s[0:3]


# In[34]:


s[3:]


# In[35]:


s[:]


# In[38]:


s[0:6:2]


# In[40]:


s[::-1]


# Printing

# In[41]:


x = 'hello'


# In[42]:


x


# In[43]:


print(x)


# In[44]:


print('hello')


# In[45]:


print(hello)


# In[46]:


num = 12
name = 'Sam'


# In[47]:


print('My Number is : ',num,' and My Name is : ',name)


# In[51]:


print('My Number is :  {}  and My Name is : {}'.format(num,name))


# In[52]:


print('My Number is :  {one}  and My Name is : {two}'.format(one=num,two=name))


# In[53]:


print('My Number is :  {two}  and My Name is : {one}'.format(one=num,two=name))


# Lists

# In[54]:


[1,2,3]


# In[55]:


['hi','hello',1,2,3]


# In[56]:


my_list = ['a','b','c']


# In[57]:


my_list[0]


# In[58]:


my_list[2]


# In[59]:


my_list[3] = 'd'


# In[60]:


my_list.append('d')


# In[61]:


my_list


# In[62]:


my_list[2:]


# In[63]:


my_list[:3]


# In[64]:


my_list[0] = 'New'


# In[65]:


my_list


# In[66]:


nest = [1,2,3,[4,5,[0,'target']]]


# In[67]:


nest[0]


# In[68]:


nest[3]


# In[69]:


nest[3][0]


# In[70]:


nest[3][1]


# In[72]:


nest[3][2][1]


# Dictionaries

# In[80]:


d= {'key1':'item1','key2':'asghar',152:'Some Thing'}


# In[74]:


d


# In[75]:


d[0]


# In[76]:


d['key1']


# In[79]:


d['key2']


# In[81]:


d[152]


# Booleans

# In[82]:


True


# In[83]:


False


# Tuples

# In[84]:


t = (1,2,3)


# In[85]:


l = [1,2,3]


# In[86]:


l[0] = 'New'


# In[87]:


l


# In[91]:


t[0] = 'New'


# Sets

# In[94]:


d = {1:2}


# In[95]:


d[1]


# In[97]:


s = {1,2}


# In[98]:


s


# In[99]:


l = [1,2,1,2,1,2,1,2]


# In[100]:


l


# In[101]:


s = {1,2,1,2,1,2,1,2}


# In[102]:


s


# In[103]:


s.add(3)


# In[104]:


s


# In[105]:


s.add(3)


# In[106]:


s


# In[107]:


s.add(1)


# In[108]:


s


# Comparison Operators

# In[109]:


1 > 2


# In[110]:


1 < 2


# In[111]:


1 >= 2


# In[112]:


1 <= 2


# In[113]:


1 == 1


# In[115]:


x = 1


# In[116]:


1 = 1


# In[117]:


1 == 1


# In[118]:


'hi' == 'bye'


# In[119]:


'hi' == 'hi'


# In[120]:


'Hi' == 'hi'


# logic Operators

# In[121]:


(1 > 2) and (2 < 3)


# In[122]:


(1 > 2) or (2 < 3)


# In[123]:


(1 == 2) or (2 == 3) or (4 == 4)


# In[124]:


(1 == 2) and (2 == 3) or (4 == 4)


# In[125]:


not True


# In[126]:


(1 == 1)


# In[127]:


not (1 == 1)


# if , elif , else Statements

# In[129]:


if 1<2 :
    print('Yep!')


# In[130]:


if 1>2 :
    print('Yep!')


# In[131]:


if True :
    print('Yep!')


# In[133]:


if 1>2:
    print('Yep!')
else:
    print('NOO!')


# In[139]:


if 2<1:
    print('Yep!1')
elif  1 == 2:
    print('Yep!2')
elif 3 == 5:
    print('Yep!3')
else:
    print('NOO!')


# for Loops

# In[140]:


seq = [1,2,3,4,5]


# In[141]:


for i in seq:
    print(i)


# In[142]:


for i in seq:
    print('Yep!')


# In[143]:


for asghar in seq:
    print(asghar**2)


# while Loops

# In[144]:


i = 1
while i<5:
    print('i is : {}'.format(i))


# In[145]:


i = 1
while i<5:
    print('i is : {}'.format(i))
    i = i+1


# range()

# In[146]:


range(5)


# In[147]:


for i in range(5):
    print(i)


# In[148]:


list(range(5))


# In[149]:


list(range(1,5))


# In[150]:


list(range(3,13))


# In[151]:


list(range(3,13,3))


# In[152]:


for i in range(3,13,3):
    print(i)


# list comprehensions

# In[153]:


x = [1,2,3,4]


# In[156]:


out = []
for i in x:
    out.append(i**2)


# In[157]:


out


# In[158]:


[i**2 for i in x]


# functions

# In[167]:


#Comment Here
def my_func_name(param1='default'):
    """
    This Function Prints Any Thing that is present in input
    """
    print('Hello {}'.format(param1))


# In[168]:


my_func_name('Shervin')


# In[169]:


my_func_name('Sajjad')


# In[170]:


def square(x):
    print(x**2)


# In[171]:


square(5)


# In[172]:


out = square(5)


# In[173]:


print(out)


# In[174]:


def square(x):
    return(x**2)


# In[175]:


square(5)


# In[176]:


out = square(5)


# In[177]:


print(out)


# lambda expressions

# In[178]:


def time2(var):
    return var**2


# In[179]:


time2(6)


# In[181]:


time22 = lambda var:var**2


# In[182]:


time22(6)


# map and filter

# In[183]:


seq = [1,2,3,4,5]


# In[184]:


def time2(var):
    return var**2


# In[185]:


time2(6)


# In[186]:


time2(seq)


# In[187]:


[1,2,3,4,5]**2


# In[189]:


list(map(time2,seq))


# In[190]:


for i in map(time2,seq):
    print(i)


# In[191]:


list(map(lambda v:v**2,seq))


# In[193]:


def check_even(var):
    if var%2 ==0:
        return True
    else:
        return False


# In[194]:


check_even(2)


# In[195]:


check_even(3)


# In[196]:


def check_even(var):
    return var%2 == 0


# In[197]:


check_even(2)


# In[198]:


check_even(3)


# In[199]:


seq = [1,2,3,4,5,6,7,8,9,10]


# In[200]:


list(filter(check_even,seq))


# In[201]:


list(filter(lambda x : x%2==0 ,seq))


# Methods

# In[216]:


#String


# In[203]:


st = 'Hello My Name is MohamadReza'


# In[205]:


st.lower()


# In[206]:


st.upper()


# In[207]:


st.split()


# In[212]:


tweet = 'GO sports! #sports #Soccer #Tennis #Neymar'


# In[213]:


tweet.split()


# In[214]:


tweet.split('#')


# In[215]:


tweet.split('#')[1:]


# In[217]:


#Dictionaries


# In[219]:


d = {'key1':'apple','key2':'mashroom'}


# In[220]:


d.keys()


# In[221]:


d.values()


# In[222]:


#list


# In[223]:


l = [1,2,3]


# In[224]:


l.append(4)


# In[225]:


l


# In[226]:


l.pop()


# In[227]:


l


# In[228]:


l.pop(0)


# In[229]:


l


# In[230]:


l[0]


# In[231]:


l = [1,2,3,4,5,6,7,8,9,10]


# In[232]:


l.pop(2)


# In[233]:


l


# In[234]:


l = [1,2,3,4,5,6,7,8,9,10]


# In[235]:


l.remove(2)


# In[236]:


l


# In[237]:


l = ['a','b','c']


# In[238]:


l.remove('b')


# In[239]:


l


# In[240]:


'x' in [1,2,3]


# In[241]:


'x' in ['x','y','z']


# In[242]:


3 in [1,2,3]


# In[243]:


#Sets


# In[246]:


s = {1,2,3}


# In[247]:


s.add(4)


# In[248]:


s


# In[249]:


s.add(4)


# In[250]:


s


# In[251]:


#Tupples


# In[252]:


t = (1,2,3)


# In[253]:


t[2]


# Great Job!
