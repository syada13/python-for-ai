#!/usr/bin/env python
# coding: utf-8

# # Loading and using your own data
from helper_functions import upload_txt_file, list_files_in_directory,print_llm_response
list_files_in_directory()

# Open the email.txt file and print its contents
f = open("email.txt", "r")
email = f.read()
f.close()
print(email)


# Open the recipe.txt file and print its contents
f = open("recipe.txt", "r")
recipe = f.read()
f.close()
print(recipe)


# ## Uploading and reading your own text files
upload_txt_file() 

# Print the list of the files inside this folder
list_files_in_directory()

# Change the file name on the next line to the one you uploaded. 
# Make sure you keep the double quotation marks around the file name!
f = open("notes.txt", "r")
your_file_content = f.read() 
f.close()
print(your_file_content)


# ## Use AI to summarize your file contents
# * Ask an LLM to create a summary of your file content
prompt = f"""Summarize the content from the following text
in at most two sentences. 
Text:
{your_file_content}"""
print(prompt)


# * Print out the response from the LLM
print_llm_response(prompt)


# ### Exercise 1
# Modify the prompt below to ask the LLM a different question about your text data.
# Modify the prompt below to ask the LLM a different question about 

prompt = f"""Extract relationship between subject and subclasses in following text. 
Text:
{your_file_content}"""
print_llm_response(prompt)


# ### Exercise 2
# Modify the prompt to use the data that you loaded in from `recipe.txt`
f = open("recipe.txt","r")
my_recipe_file = f.read()
f.close()
prompt = f"""Identify all of the cooking techniques used in the 
following recipe:

Recipe:
{my_recipe_file}"""

print_llm_response(prompt)

