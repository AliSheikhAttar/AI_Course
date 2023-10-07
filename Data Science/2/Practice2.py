#!/usr/bin/env python
# coding: utf-8

# ![0.jfif](attachment:0.jfif)

# <div style="direction:rtl">
# خب خب، درسته که نامپای ستون فقرات دیتا ساینیه، ولی ما کارامون رو با دست و چشم و پا انجام میدیم نه با خود ستون فقرات. برای همین تو این بخش زیاد تمرینای از جنس مساله نداریم و بیشتر تمرینامون حول تسلط به ابزار ها و متد های این کتابخونه است.
# <div style="direction:rtl">
# برای شروع، کتابخونه ی نامپای رو ایمپورت کنید.

# In[1]:





# <div style="direction:rtl">
# یه آرایه ی متشکل از 10 تا صفر بسازید.

# In[2]:





# <div style="direction:rtl">
# یه آرایه ی متشکل از 10 تا یک بسازید.

# In[3]:





# <div style="direction:rtl">
# یه آرایه ی متشکل از 10 تا پنج بسازید.

# In[5]:





# <div style="direction:rtl">
# یه آرایه ی متشکل از اعداد ده تا پنجاه بسازید.

# In[6]:





# <div style="direction:rtl">
# یه آرایه ی متشکل از اعداد زوج بین ده تا پنجاه بسازید.

# In[7]:





# <div style="direction:rtl">
# یه ماتریس سه در سه با مقادیر 0 تا 8 بسازید.

# In[8]:





# <div style="direction:rtl">
# یه ماتریس سه در سه قطری بسازید.

# In[9]:





# <div style="direction:rtl">
# یه ماتریس سه در سه با اعداد رندوم بسازید.

# In[11]:





# <div style="direction:rtl">
# یه ماتریس سه در سه با اعداد رندومی بسازید که به شکل نرمال حول 0 توزیع شده باشند.

# In[13]:





# <div style="direction:rtl">
# با دو روش مختلف دقیقا ماتریس زیر رو بسازید.

# In[20]:





# In[21]:





# <div style="direction:rtl">
# آرایه ای بسازید که شامل 20 تا عدد با فاصله های مساوی بین 0 و 1 باشه.

# In[22]:





# <div style="direction:rtl">
# ابتدا ماتریس زیر را با نام mat بسازید و سپس تکه های خواسته شده از ماتریس در هر بخش را به دست آورید.

# In[24]:





# In[25]:


mat


# In[26]:





# In[27]:





# In[28]:





# In[29]:





# In[31]:





# In[36]:





# In[37]:





# In[38]:





# <div style="direction:rtl">
# با مراجعه به بخش fancy از جلسه ی پیش، سعی کنید تکه ماتریس بالا را با روش اول آقای جانفدا هم محاسبه کنید و ایراد آن روش را در پایین بنویسید.

# In[45]:


# This Slice is the Same Code of Above, just Written Like Janfada First Method


# <div style="direction:rtl">
# تفاوت این روش با روش درست در این است که :...

# <div style="direction:rtl">
# جمع تک تک عناصر موجود در ماتریس را با استفاده از دو روش (یک بار متد و یک بار فانکشن) به دست آورید.

# In[40]:





# In[41]:





# <div style="direction:rtl">
# در آمار ، انحراف معیار، مقدارپراکندگی مجموعه ای از مقادیر است. انحراف استاندارد پایین نشان می دهد که مقادیر نزدیک به میانگین مجموعه هستند ، در حالی که انحراف استاندارد بالا نشان می دهد که مقادیر در دامنه وسیع تری پخش شده اند.
# انحراف معیار را در ریاضیات با STD یا همان standard deviation نشان می دهند.
# <div style="direction:rtl">
# با تحقیق و جست و جو، متدی برای محاسبه ی std در این ماتریس پیدا کنید و انحراف معیار داده های این ماتریس را محاسبه کنید.

# In[43]:





# <div style="direction:rtl">
# در باره ی axis ها(محور ها) در نامپای تحقیق کنید و axis دیفالت نامپای را معرفی کنید، سپس با کمک axis ها جمع سطر ها وستون های ماتریس را  به دست آورید.

# <div style="direction:rtl">
# axis دیفالت نامپای در جهت :...

# <div style="direction:rtl">
# جمع سطر ها:
# (هم با متد هم با فانکشن)

# In[47]:





# In[50]:





# <div style="direction:rtl">
# جمع ستون ها :
# (هم با متد هم با فانکشن)

# In[49]:





# In[51]:





# <div style="direction:rtl">
# حالا با کمک مفهومی که از محور ها در عملیات های نامپای فرا گرفته اید، سعی کنید با دستور concatenate دو ماتریس زیر را یک بار در جهت محور عمودی و یک بار در جهت محور افقی بهم بچسبانید.

# In[61]:


a = np.arange(1,10).reshape(3,3)
a


# In[62]:


b = np.arange(1,10).reshape(3,3).transpose()
b


# <div style="direction:rtl">
# چسباندن در راستای افقی:

# In[65]:





# <div style="direction:rtl">
# چسباندن در راستای عمودی:

# In[66]:





# <div style="direction:rtl">
# 
# ## موفق باشید.
