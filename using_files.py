#!/usr/bin/env python
# coding: utf-8
# # Lesson 1: Using files in Python

from helper_functions import get_llm_response
from IPython.display import display, Markdown


# Write a prompt to create a recipe using `get_llm_response`.
ingredients = ['chicken', 'broccoli', 'rice']
prompt = f"""
    Create a short recipe that uses the following ingredients:
    {ingredients}
"""
response = get_llm_response(prompt)
print(response)



# You will load data that has already been created and is stored 📁 for you in files.
f = open("email.txt","r")
email = f.read()
f.close()
print(email)


# Using LLMs to extract bullet points from the email
prompt = f"""Extract bullet points from the following email. 
Include the sender information. 
Email:
{email}"""
print(prompt)


# * Run the ```get_llm_response``` function to get the response with bullet points.
bullet_points = get_llm_response(prompt)
print(bullet_points)
display(Markdown(bullet_points))


#Exercise 1
# Complete the code below to identify all of the countries mentioned in the email
prompt = f"""Extract all countries name from the following email.
Email:
{email}
"""
countries = get_llm_response(prompt)
print(countries)


#Exercise 2
# Write code below to list all of the activities that Daniel did on his trip. You'll need to create a prompt and use either `get_llm_response` or `print_llm_response`.
# Write code below to list all of the activities that Daniel did on 
# his trip. You'll need to create a prompt and use either 
# get_llm_response or print_llm_response
# START YOUR CODE HERE
prompt = f"""List all activities that Daniel did on his trip from the following email.
Email:{email}"""
print(get_llm_response(prompt))

