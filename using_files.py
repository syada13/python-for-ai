#!/usr/bin/env python
# coding: utf-8
# # Lesson 1: Using files in Python

from helper_functions import get_llm_response
from IPython.display import display, Markdown


# Write a prompt to create a recipe using `get_llm_response`.

# Write a list of ingredients
ingredients = ['chicken', 'broccoli', 'rice']

# Write the prompt
prompt = f"""
    Create a short recipe that uses the following ingredients:
    {ingredients}
"""

# Get the response from the LLM
response = get_llm_response(prompt)

# Print the LLM response
print(response)


# ## Opening a text file and saving it as a string
# You will load data that has already been created and is stored 📁 for you in files.
# Start by loading an email that Daniel sent recently. It is stored in a '.txt' file.

f = open("email.txt","r")
email = f.read()
f.close()
print(email)


# ## Using LLMs to extract bullet points from the email
# * Create a prompt to extract bullet points from Daniel's email ✉️.
prompt = f"""Extract bullet points from the following email. 
Include the sender information. 
Email:
{email}"""
print(prompt)


# * Run the ```get_llm_response``` function to get the response with bullet points.
bullet_points = get_llm_response(prompt)
print(bullet_points)


# * Print the LLM response in Markdown format.
# Print in Markdown format
display(Markdown(bullet_points))


# ## Extra practice
# Try the exercises below to get an LLM to carry out different tasks using the email text you read in from file:

# ### Exercise 1
# Complete the code below to identify all of the countries mentioned 
# in the email
prompt = f"""Extract all countries name from the following email.
Email:
{email}
"""

countries = get_llm_response(prompt)
print(countries)


# ### Exercise 2
# Write code below to list all of the activities that Daniel did on his trip. You'll need to create a prompt and use either `get_llm_response` or `print_llm_response`.
# Write code below to list all of the activities that Daniel did on 
# his trip. You'll need to create a prompt and use either 
# get_llm_response or print_llm_response
# START YOUR CODE HERE
prompt = f"""List all activities that Daniel did on his trip from the following email.
Email:{email}"""
print(get_llm_response(prompt))

