

# In[1]:
print("HelloWorld!")



# In[2]:
name = input("Enter name:")
print(name)

# In[3]:

number = input("Enter number:")
print(number)

# In[4]:

txt = "hello,and welcome all."
x = txt.capitalize()
print(x)

# In[5]:

txt = "Hello,And Welcome To My Party!"
x = txt.casefold()
print(x)


# In[6]:


txt = "grapes"
x = txt.center(20)
print(x)


# In[7]:


txt = "I love Shreyas,Shreyas is one of the main players in Indian Cricket team"
x = txt.count("Shreyas")
print(x)


# In[8]:


txt = "My name is Sam"
x = txt.encode()
print(x)


# In[9]:


txt = "Hello, world."
x = txt.endswith(".")
print(x)


# In[10]:


txt ="H\te\tl\tl\to"
x = txt.expandtabs(2)
print(x)


# In[11]:


txt ="Hello,welcome to my home."
x = txt.find("welcome")
print(x)


# In[14]:


txt = "For only{price:.2f}dollars!"
print(txt.format(price = 49))


# In[15]:


txt ="Hello,welcome to my home."
x = txt.index("welcome")
print(x)


# In[16]:


txt ="Company12"
x = txt.isalnum()
print(x)


# In[17]:


txt ="CompanyX"
x = txt.isalpha()
print(x)


# In[18]:


txt ="\u0033"#unicode for 3
x = txt.isdecimal()
print(x)


# In[19]:


txt ="50800"
x = txt.isdigit()
print(x)


# In[20]:


txt ="Demo"
x = txt.isidentifier()
print(x)


# In[21]:


txt = "hello world!"
x = txt.islower()
print(x)


# In[22]:


txt ="54687"
x = txt.isnumeric()
print(x)


# In[24]:


txt ="Hello! Are you #1?"
x = txt.isprintable()
print(x)


# In[25]:


txt ="  "
x = txt.isspace()
print(x)


# In[26]:


txt = "Hello,And Welcome To My Party!"
x = txt.istitle()
print(x)


# In[27]:


txt ="THIS IS NEW!"
x = txt.isupper()
print(x)


# In[28]:


myTuple =("Joe","Peter")
x ="#".join(myTuple)
print(x)


# In[29]:


txt = "grapes"
x = txt.ljust(20)
print(x,"is my favourite fruit.")


# In[30]:


txt ="Hello my FRIENDS"
x = txt.lower()
print(x)


# In[31]:


txt = "   grapes   "
x = txt.lstrip()
print("of all fruits",x,"is my favourite")


# In[32]:


txt = "Hello Sam!"
mytable = txt.maketrans("S","P")
print(txt.translate(mytable))


# In[33]:


txt ="I could eat bananas all day"
x = txt.partition("bananas")
print(x)


# In[34]:


txt ="I like bananas"
x = txt.replace("bananas","apples")
print(x)


# In[35]:


txt ="Mi casa, su casa."
x = txt.rfind("casa")
print(x)


# In[36]:


txt ="Mi casa, su casa."
x = txt.rindex("casa")
print(x)


# In[37]:


txt = "grapes"
x = txt.rjust(20)
print(x,"is my favourite fruit")


# In[38]:


txt ="I could eat bananas all day,bananas are my favourite fruit"
x = txt.rpartition("bananas")
print(x)


# In[39]:


txt = "apple,banana,cherry"
x = txt.rsplit(",")
print(x)


# In[40]:


txt = "  grapes  "
x = txt.rstrip()
print("of all fruits",x,"is my favourite")


# In[41]:


txt ="welcome to the jungle"
x = txt.split()
print(x)


# In[42]:


txt ="Thank you for the music\nwelcome to my party"
x = txt.splitlines()
print(x)


# In[44]:


txt ="Hello,welcome to the jungle"
x = txt.startswith("Hello")
print(x)


# In[45]:


txt = "  grapes  "
x = txt.strip()
print("of all fruits",x,"is my favourite")


# In[46]:


txt ="Hello My Name Is DHEV"
x =txt.swapcase()
print(x)


# In[47]:


txt = "Welcome to the jungle"
x = txt.title()
print(x)


# In[48]:


#use a dictionary with ascii codes to replace 83 (S) with 80 (P):
mydict ={83:80}
txt ="Hello Sam!"
print(txt.translate(mydict))


# In[49]:


txt = "Hello dude"
x = txt.upper()
print(x)


# In[50]:


txt ="50"
x = txt.zfill(10)
print(x)


# In[51]:


fruits =['apple','banana']
fruits.append("orange")
print(fruits)


# In[52]:


fruits =['apple','banana']
fruits.clear()
print(fruits)


# In[53]:


fruits =['apple','banana']
fruits.copy()
print(fruits)


# In[54]:


fruits =['apple','banana']
fruits.count("apple")
print(fruits)


# In[55]:


fruits =['apple','banana']
cars =['Ford','BMW','Duster']
fruits.extend(cars)
print(fruits)


# In[58]:


fruits =['apple','banana']
x = fruits.index("banana")
print(x)


# In[60]:


fruits =['apple','banana']
fruits.insert(1,"grapes")
print(fruits)


# In[61]:


fruits =['apple','banana']
fruits.pop(1)
print(fruits)


# In[62]:


fruits =['apple','banana']
fruits.remove("banana")
print(fruits)


# In[63]:


fruits =['apple','banana']
fruits.reverse()
print(fruits)


# In[64]:


cars =['Ford','BMW','Duster']
cars.sort()
print(cars)

