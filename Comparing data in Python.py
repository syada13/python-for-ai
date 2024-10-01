#!/usr/bin/env python
# coding: utf-8

# # Lesson 5 - Comparing data in Python
# 

# In[1]:


from helper_functions import print_llm_response, get_llm_response


# Take a closer look at the True/False variable you saw at the end of the last lesson.

# In[2]:


food_preferences_tommy = {
    #"dietary_restrictions": "vegetarian",
    "favorite_ingredients": ["mushrooms", "olives"],
    "experience_level": "intermediate",
    "maximum_spice_level": 6
}


# You added the element `"is vegetarian"` with a value equal to `True`

# In[3]:


food_preferences_tommy["is_vegetarian"] = True


# This type of data is know as booleans. It can take only two values: `True` or `False`.

# In[4]:


print(food_preferences_tommy)


# ## True and False
# 
# `True` and `False` may look like strings without quotation marks. They are the two values that booleans can take. 

# In[5]:


print(True)
print(False)


# Below, you can check the type for each of these values.

# In[6]:


type(True)


# In[7]:


type(False)


# If you're curious, ask chatbot why it's called Boolean
# <p style="background-color:#F5C780; padding:15px"> 🤖 <b>Use the Chatbot</b>: Why is the True or False data type called a Boolean?
# </p>  
# 

# As with any other data type, you can assign booleans to variables:

# In[8]:


is_tommy_my_friend = True


# In[9]:


is_isabel_older_than_me = False


# In[10]:


print(is_tommy_my_friend)


# In[11]:


print(is_isabel_older_than_me)


# In[12]:


type(is_isabel_older_than_me)


# ### Comparison Operators
# 
# Booleans are what you get back when you compare variables in python. For example, here are the ages for Isabel, Daniel and Tommy:

# In[13]:


isabel_age = 28
daniel_age = 30
tommy_age = 30


# In Python you can compare values using the same operator you probably encounter in math classes. Let's start determining if Isabel is older than Daniel using `>`.

# In[14]:


print(isabel_age > daniel_age)     


# Now, let's determine if she is younger using `<`:

# In[15]:


print(isabel_age < daniel_age) 


# In[16]:


is_isabel_older_than_daniel = isabel_age > daniel_age
print(is_isabel_older_than_daniel)


# You can also use `<=` and `>=` to check if one number is greater than or equal to the other, or if it is lower than or equal to the other. 

# In[17]:


print(isabel_age <= daniel_age)


# Since Daniel and Tommy are the same age, when you use `<=` and `>=` you will get `True` for both cases:

# In[18]:


print(tommy_age < daniel_age)


# In[19]:


print(tommy_age <= daniel_age)


# ### Equality Operator
# So, what if you want to check if to things are equal? You would neeed to use `==`. 
# 
# - `= `is an assignment operator, it assigns values to variables
# - `==` is a comparison operator, it checks if two things are holding the same value, or if two pieces of data are equal 

# So, going back to comparing Daniel's and Tommy's age:

# In[20]:


print(tommy_age == daniel_age)


# And Isabel's and Daniel's:

# In[21]:


print(isabel_age == daniel_age) 


# This operator works for strings too. Here you have definitive proof that a vegetarian is not the same as a vegan.

# In[22]:


#strings
print("vegetarian" == "vegan")


# ### Logical Operators

# Operations with booleans involve logical operators like `and` and `or`. Let's define a couple of boolean variables:

# In[23]:


is_tommy_my_friend = True
is_isabel_my_friend = True


# If you want to check whether both Tommy and Isabel are your friends, you can use the `and` operator:

# In[24]:


print(is_tommy_my_friend and is_isabel_my_friend)


# If you want to check whether at least one of them is your friend, you can use the `or` operator:

# In[25]:


print(is_tommy_my_friend or is_isabel_my_friend)


# Let's say that Isabel, Tommy and Daniel are playing a game involving their ages:

# In[26]:


isabel_age = 28
daniel_age = 30
otto_age = 29


# The game involves checking whether Isabel is younger than both Tommy and Daniel:

# In[27]:


is_isabel_younger_than_tommy = isabel_age < tommy_age
is_isabel_younger_than_daniel = isabel_age < daniel_age


# In[28]:


print(is_isabel_younger_than_tommy and is_isabel_younger_than_daniel)


# In the next video, you will use booleans to write programs that execute different lines of code depending on the boolean value.

# ## Extra practice

# Please go through the exercises in the cells below if you want some extra practice for the topics you covered in this lesson.

# In[30]:


# Check whether Isabel is older
# than at least one of my friends (Tommy and Daniel)

### EDIT THE FOLLOWING CODE ###
# Hint: Replace the "?" with the correct comparison operator
is_isabel_older_than_tommy = isabel_age > tommy_age
is_isabel_older_than_daniel = isabel_age > daniel_age
### --------------- ###

### EDIT THE FOLLOWING CODE ###
#Hint: Recall the logical operators "and" and "or" 
print(f"Check if Isabel is older than at least one of my friends: {is_isabel_older_than_tommy or is_isabel_older_than_daniel}")
### --------------- ###

