#!/usr/bin/env python
# coding: utf-8

# ![0.jfif](attachment:0.jfif)

# ### Using Numpy

# #### Numpy Arrays

# In[1]:


import numpy as np


# In[2]:


my_list = [1,2,3]


# In[3]:


my_list


# In[4]:


np.array(my_list)


# In[5]:


my_matrix = [[1,2,3],[4,5,6],[7,8,9]]


# In[6]:


my_matrix


# In[7]:


np.array(my_matrix)


# In[8]:


list(range(0,10))


# arange

# In[9]:


np.arange(0,10)


# In[10]:


np.arange(0,11,2)


# Zeros and Ones

# In[11]:


np.zeros(3)


# In[12]:


np.zeros((3,3))


# In[13]:


np.zeros((5,3))


# In[14]:


np.ones(3)


# In[15]:


np.ones((3,3))


# In[16]:


np.ones((5,3))


# linspace

# In[17]:


np.linspace(0,10,3)


# In[18]:


np.linspace(0,10,50)


# eye

# In[19]:


np.eye(4)


# Random

# rand

# In[20]:


np.random.rand(2)


# In[21]:


np.random.rand(5,5)


# In[22]:


np.random.rand(8,5)


# randn

# In[10]:


np.random.randn(2)


# In[8]:


np.random.randn(5,5)


# randint

# In[11]:


np.random.randint(1,100)


# In[12]:


np.random.randint(1,100,10)


# In[17]:


np.random.randint(30,50)


# Array Attributes and Methods

# In[18]:


arr = np.arange(25)


# In[19]:


arr


# In[20]:


randarr = np.random.randint(0,50,10)


# In[21]:


randarr


# reshape

# In[22]:


arr.reshape(5,5)


# In[23]:


randarr


# In[24]:


randarr.reshape(2,5)


# In[25]:


randarr.reshape(5,2)


# In[26]:


randarr


# In[32]:


np.random.randint(0,50,15).reshape(3,5)


# max,min,argmax,argmin

# In[39]:


randarr


# In[40]:


randarr.max()


# In[41]:


randarr.min()


# In[42]:


randarr.argmax()


# In[43]:


randarr.argmin()


# flatten

# In[225]:


arr = np.random.randn(5,5)


# In[228]:


arr.shape


# In[229]:


arr.flatten().shape


# vstack,hstack,concatenate

# In[230]:


a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])


# In[233]:


a


# In[234]:


b


# In[232]:


np.vstack((a,b))


# In[235]:


np.hstack((a,b))


# In[236]:


np.concatenate((a,b))


# shape

# In[48]:


arr


# In[53]:


arr.shape


# In[50]:


arr.reshape(1,25)


# In[51]:


arr.reshape(1,25).shape


# dtype

# In[55]:


arr.dtype


# In[56]:


sahand = np.array([1.2,7.56,119.568])


# In[57]:


sahand.dtype


# In[58]:


sahand = np.array([1,2,3,4,5,6,1.2])


# In[59]:


sahand.dtype


# In[60]:


sahand


# In[63]:


sahand = np.array([1,2,3,4,5,6],dtype = 'float64')


# In[64]:


sahand.dtype


# In[65]:


sahand


# In[66]:


sahand = np.array([1.5,2.7,3.8,4,5,6],dtype = 'int32')


# In[67]:


sahand


# In[68]:


list1 = [[1,2,3],['mamad','ali','naghi'],[4,5,6]]


# In[77]:


arr3 = np.array(list1)


# In[75]:


arr1 = np.arange(0,9).reshape(3,3)
arr2 = np.linspace(0,10,9).reshape(3,3)


# In[76]:


arr1 + arr2


# In[78]:


arr1 + arr3


# iterate

# In[238]:


arr = np.array([1,2,3])


# In[239]:


for x in arr:
    print(x)


# In[241]:


arr = np.array([[1,2,3],[4,5,6]])


# In[242]:


for x in arr:
    print(x)


# Numpy Indexing and Selection

# In[79]:


arr = np.arange(0,11)


# In[80]:


arr


# Bracket Indexing,Slicing 

# In[81]:


arr[0]


# In[82]:


arr[8]


# In[83]:


arr[0:4]


# In[84]:


arr[1:7]


# In[85]:


arr[3:]


# In[86]:


arr[:5]


# In[87]:


arr[0:7:2]


# In[88]:


arr[0:7:3]


# In[89]:


arr[::2]


# In[90]:


arr[::-1]


# Broadcasting

# In[92]:


arr[0:5] = 100


# In[93]:


arr


# In[97]:


list1 =[ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10]


# In[100]:


list1[0:5] = [100,100,100,100,100]


# In[101]:


list1


# In[102]:


arr=np.arange(0,11)


# copy

# In[103]:


arr


# In[108]:


slice_of_arr = arr[0:6]


# In[109]:


slice_of_arr


# In[110]:


slice_of_arr[:] = 99


# In[111]:


slice_of_arr


# In[112]:


arr


# In[113]:


arr=np.arange(0,11)


# In[115]:


arr_copy = arr.copy()[0:6]


# In[116]:


arr_copy[:] = 99


# In[117]:


arr_copy


# In[119]:


arr


# In[121]:


arr.copy()


# indexing a 2D array(matrices)

# In[128]:


arr_2d = np.array([[5,10,15],[20,25,30],[35,40,45]])


# In[129]:


arr_2d


# In[130]:


arr_2d[1]


# In[131]:


arr_2d[0]


# In[146]:


arr_2d[0][:2]


# In[132]:


arr_2d[0][0]


# In[133]:


arr_2d[0][2]


# In[134]:


arr_2d.transpose()


# In[243]:


arr = np.arange(0,100).reshape(10,10)


# In[138]:


arr


# In[141]:


arr[0:5]


# In[142]:


arr[3:]


# In[143]:


arr[3:][0]


# In[147]:


arr[3:,5:]


# In[151]:


arr[3:,5:][0,2]


# In[153]:


arr[3:,5:][0][2]


# In[158]:


arr


# In[160]:


arr[0:2,0:2]


# Fancy Indexing

# In[164]:


arr[2:5]


# In[165]:


arr[[2,4]]


# In[167]:


arr[[2,4],3:6]


# In[171]:


arr[[2,4],3:6]


# In[176]:


arr[2:4,[1,4,7]]


# In[180]:


arr[[2,4]]


# In[187]:


arr[[6,4,2,7][0:2],0:3]


# In[189]:


arr[[2,4],[[3],[5]]]


# Both Dimention Fancy Janfada Method

# In[191]:


arr[[1,2,5,7],[[2],[3],[5]]]


# In[192]:


arr[[[2],[3],[5]],[1,2,5,7]]


# Both Dimention Fancy Regular Method

# In[245]:


arr[[1,2],:][:,[3,5,7]]


# Selection

# In[193]:


arr = np.arange(1,11)
arr


# In[194]:


arr>4


# In[195]:


arr == 3


# In[196]:


bool_arr = arr>4


# In[197]:


bool_arr


# In[199]:


arr[4:]


# In[198]:


arr[bool_arr]


# In[200]:


arr[arr>4]


# In[201]:


arr[arr==2]


# In[202]:


arr[arr<=5]


# In[203]:


arr[arr%2==0]


# Numpy Operations

# Array with Array (Arithmetic)

# In[204]:


arr = np.arange(0,10)


# In[205]:


arr


# In[206]:


arr + arr


# In[207]:


arr * arr


# In[208]:


arr - arr


# In[209]:


arr / arr


# Array with Scaler

# In[210]:


arr + 100


# In[211]:


arr * 2


# In[212]:


arr - 5


# In[213]:


arr / 2


# In[214]:


1/arr


# Universal Array Functions

# In[216]:


arr


# In[215]:


np.sqrt(arr)


# In[217]:


np.exp(arr) #e^


# In[218]:


np.max(arr)


# In[220]:


np.min(arr)


# In[221]:


np.sin(arr)


# In[222]:


np.cos(arr)


# In[223]:


np.log(arr)

