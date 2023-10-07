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

# In[1]:


7**4


# <div style="direction:rtl">
# ابتدا استرینگ زیر را تعریف نمایید و سپس با استفاده از متد های استرینگ، کلمات این جمله را از هم جدا کنید و در یک لیست ذخیره کنید.
# <div style="direction:ltr">
# s = "Hi there Mohammad!"

# In[2]:


s = "Hi there Mohammad!"


# In[3]:


s.split()


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

# In[4]:


planet = "Earth"
diameter = 12742


# In[5]:


print("The diameter of",planet,"is",diameter,"kilometers.")


# In[6]:


print("The diameter of {} is {} kilometers.".format(planet,diameter))


# <div style="direction:rtl">
# به کمک ایندکسینگ در لیست های تو در تو، به لغت ایران در لیست زیر دست پیدا کنید.

# In[7]:


lst = [1,2,[3,4],[5,[100,200,['Iran']],23,11],1,7]


# In[21]:


lst[3][1][2][0]


# <div style="direction:rtl">
# به کمک ایندکسینگ در دیکشنری های تو در تو، به لغت ایران در دیکشنری زیر دست پیدا کنید.

# In[14]:


d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'Iran']}]}]}


# In[19]:


d['k1'][3]['tricky'][3]['target'][3]


# <div style="direction:rtl">
# تفاوت متغیر های tuple و list در چیست؟

# l = [1,2,3]
# 
# t = (1,2,3)
# 
# Tuples are Immutable

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
    return list(email.split("@"))[1].split(".")[0]


# In[38]:


domainGet("abbasomidi77@elec.iust.ac.ir")


# In[37]:


domainGet("itsatest@yahoo.com")


# <div style="direction:rtl">
# تابعی بنویسید که یک جمله را در ورودی دریافت کند و در صورت وجود لغت Dog در آن True را برگرداند.
# <div style="direction:rtl">
# دقت کنید که تابع شما نباید به حروف بزرگ و کوچک حساس باشد، یعنی dog با DOG با Dog هیچ فرقی ندارد و باید به ازای مشاهده ی هر کدام از این لغات، True را برگرداند.

# In[27]:


def findDog(st):
    return 'dog' in st.lower().split()


# In[30]:


'Is there a dog here?'.lower().split()


# In[28]:


findDog('Is there a dog here?')


# In[29]:


findDog('Is there a DoG here?')


# <div style="direction:rtl">
# تابعی بنویسید که تعداد لغات dog موجود در جمله را بشمارد.
# <div style="direction:rtl">
# پ.ن1: باز هم دقت کنید که تابع شما نباید حساس به حروف بزرگ و کوچک باشد.
# <div style="direction:rtl">
# این تابع را به دو صورت بنویسید، یک بار بدون استفاده از متد count و یک بار هم با تحقیق در باره ی این متد و استفاده از آن.

# In[42]:


def countDog(st):
    '''
    This Function dosn't Use Count Method
    '''
    count = 0
    for word in st.lower().split():
        if word== 'dog':
            count +=1
    return count       


# In[43]:


countDog('This dog runs faster than the other DOG dude!')


# In[46]:


def countDog(st): 
    return st.lower().count('dog')


# In[47]:


countDog('This dog runs faster than the other DOG dude!')


# <div style="direction:rtl">
# از لامبدا استفاده کنید تا بدون ذخیره ی تابع از قبل، لغات موجود در یک لیست را بررسی کنید و آن هایی که با s شروع می شوند را برگردانید.

# In[49]:


seq = ['soup','dog','salad','cat','great']


# In[51]:


list(filter(lambda v:v.lower()[0]=='s',seq))


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

# In[71]:


def caught_speeding(speed, is_birthday):
    if is_birthday:
        speeding = speed -5
    else:
        speeding = speed
    if speeding>110:
        return "BIG TICKET"
    elif speeding>90:
        return "SMALL TICKET!"
    else:
        return "NO TICKET!"


# In[72]:


caught_speeding(91,True)


# In[73]:


caught_speeding(91,False)


# <div style="direction:rtl">
# 
# ## موفق باشید
