#!/usr/bin/env python
# coding: utf-8

# ![0.jfif](attachment:0.jfif)

# <div style="direction:rtl">
# 
# ## به سوالات زیر پاسخ دهید

# <div style="direction:rtl">
# پاسخ ها از قبل برای شما قرار داده شده اند تا بتوانید با پاسخ خود مقایسه نمایید.

# <div style="direction:rtl">
# هفت به توان چهار را محاسبه نمایید.

# In[6]:





# <div style="direction:rtl">
# ابتدا استرینگ زیر را تعریف نمایید و سپس با استفاده از متد های استرینگ، کلمات این جمله را از هم جدا کنید و در یک لیست ذخیره کنید.
# <div style="direction:ltr">
# s = "Hi there Mohammad!"

# In[8]:





# In[9]:





# <div style="direction:rtl">
# ابتدا دو متغیر زیر را تعریف نمایید :
# <div style="direction:ltr">    
# planet = "Earth"
#     
# diameter = 12742
# <div style="direction:rtl">
# سپس با دو روش مختلف 1.عادی 2.با کمک فرمت، جمله ی زیر را نمایش دهید :
# <div style="direction:ltr">  
# The diameter of Earth is 12742 kilometers.

# In[11]:





# In[12]:





# In[16]:





# <div style="direction:rtl">
# به کمک ایندکسینگ در لیست های تو در تو، به لغت ایران در لیست زیر دست پیدا کنید.

# In[17]:


lst = [1,2,[3,4],[5,[100,200,['Iran']],23,11],1,7]


# In[18]:





# <div style="direction:rtl">
# به کمک ایندکسینگ در دیکشنری های تو در تو، به لغت ایران در دیکشنری زیر دست پیدا کنید.

# In[19]:


d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'Iran']}]}]}


# In[20]:





# <div style="direction:rtl">
# تفاوت متغیر های tuple و list در چیست؟

# 

# <div style="direction:rtl">
# تابعی بنویسید که یک ایمیل را به عنوان ورودی دریافت نماید و شرکت ارائه دهنده ی دامنه ی ایمیل را معرفی کند.
# <div style="direction:rtl">
# برای مثال ایمیل abbasomidi77@gmail.com را دریافت نماید و gmail را برگرداند.
# <div style="direction:rtl">
# راهنمایی: ایندکس آخر یک متغیر را می توان با -1 و ایندکس یکی مانده به آخر را با -2 نشان داد و به همین ترتیب.
# <div style="direction:rtl">
# یعنی مثلا در استرینگ hello کلمه ی o هم با ایندکس 4 قابل دسترسی است هم با ایندکس -1.
# <div style="direction:rtl">
# همین قضیه در باره ی لیست ها و دیگر متغیر های پایتون نیز صادق است.

# In[35]:


def domainGet(email):
    pass


# In[33]:


domainGet("abbasomidi77@gmail.com")


# In[34]:


domainGet("itsatest@yahoo.com")


# <div style="direction:rtl">
# تابعی بنویسید که یک جمله را در ورودی دریافت کند و در صورت وجود لغت Dog در آن True را برگرداند.
# <div style="direction:rtl">
# دقت کنید که تابع شما نباید به حروف بزرگ و کوچک حساس باشد، یعنی dog با DOG با Dog هیچ فرقی ندارد و باید به ازای مشاهده ی هر کدام از این لغات، True را برگرداند.

# In[36]:


def findDog(st):
    return 'dog' in st.lower().split()


# In[37]:


findDog('Is there a dog here?')


# In[38]:


findDog('Is there a DoG here?')


# <div style="direction:rtl">
# تابعی بنویسید که تعداد لغات dog موجود در جمله را بشمارد.
# <div style="direction:rtl">
# پ.ن1: باز هم دقت کنید که تابع شما نباید حساس به حروف بزرگ و کوچک باشد.
# <div style="direction:rtl">
# این تابع را به دو صورت بنویسید، یک بار بدون استفاده از متد count و یک بار هم با تحقیق در باره ی این متد و استفاده از آن.

# In[53]:


def countDog(st):
    '''
    This Function dosn't Use Count Method
    '''
    pass


# In[40]:


countDog('This dog runs faster than the other DOG dude!')


# In[54]:


def countDog(st):
    #This Function Use Count Method
    pass


# In[50]:


countDog('This dog runs faster than the other DOG dude!')


# <div style="direction:rtl">
# از لامبدا استفاده کنید تا بدون ذخیره ی تابع از قبل، لغات موجود در یک لیست را بررسی کنید و آن هایی که با s شروع می شوند را برگردانید.

# In[55]:


seq = ['soup','dog','salad','cat','great']


# In[56]:





# <div style="direction:rtl">
# خب خب، فرض کنید که شما یک پلیس زحمت کش راهنمایی رانندگی هستید و قصد جریمه ی متخلفین را دارید. قبل از همه باید بدانید که شما سه مدل کار می توانید انجام دهید، سرعت های زیر 90 کیلومتر را جریمه نمی کنید پس باید به آن ها NO TICKET! به عنوان خروجی بدهید.
# <div style="direction:rtl">
# اما سرعت های بین 91 تا 110 کیلومتر را می توانید 40 هزار تومان جریمه کنید، به این متخلفین خروجی SMALL TICKET! را برگردانید.
# <div style="direction:rtl">
# اگر سرعت از 111 کیلومتر به بالاتر بود که متخلف گرامی 400 هزار تومان جریمه شده و باید به او خروجی BIG TICKET! را برگردانید.
# <div style="direction:rtl">
# اما برای رفاه حال متخلفین گرامی، ما از آن ها می پرسیم که آیا امروز تولد آنهاست یا خیر و اگر آن روز، روز تولد او بود، ما از سرعت او 5 کیلومتر کم می کنیم و سپس جریمه را اعمال می کنیم.
# <div style="direction:rtl">
# پ.ن1: تابعی بنویسید که ورودی های لازم را دریافت کند و موارد بالا را به خوبی پیاده سازی کند.
# <div style="direction:rtl">
# پ.ن2: ممکن است پس از اعمال تخفیف تولد، متخلف از پرداخت جریمه معاف شود و مشکلی نیست.
# <div style="direction:rtl">
# پ.ن3: جواب سوال این که آیا امروز تولد راننده است یا خیر را باید به شکل یک متغیر boolean دریافت کنیم.
# <div style="direction:rtl">
# مبلغ جریمه یک داده ی انحرافی و بی استفاده است :)

# In[11]:


def caught_speeding(speed, is_birthday):
    pass


# In[9]:


caught_speeding(91,True)


# In[10]:


caught_speeding(91,False)


# <div style="direction:rtl">
# 
# ## موفق باشید
