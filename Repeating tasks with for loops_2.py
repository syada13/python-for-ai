#!/usr/bin/env python
# coding: utf-8

# # Lesson 2 - Repeating tasks with for loops
from helper_functions import print_llm_response, get_llm_response

list_of_tasks = [
    "Compose a brief email to my boss explaining that I will be late for tomorrow's meeting.",
    "Write a birthday poem for Otto, celebrating his 28th birthday.",
    "Write a 300-word review of the movie 'The Arrival'."
]
print(list_of_tasks)


# You passed them one by one to the LLM, repeatedly updated the task variable, then re-executed the function call with this code:
task = list_of_tasks[0]
print_llm_response(task)


# If you wanted to complete all the tasks in your list, you would have to re-write the same code multiple times. Alternatively, you can use a `for` loop.
for task in list_of_tasks:
    print(task)


# Here's the code that automatically passes all items in list to `print_llm_response`
for task in list_of_tasks:
    print_llm_response(task)

# ## Iteratively updating AI prompts using lists
#ice cream flavor example
ice_cream_flavors = [
    "Vanilla",
    "Chocolate",
    "Strawberry",
    "Mint Chocolate Chip"
]


# You can use a for loop to iterate through the flavors and create a captivating description for each of them.
for flavor in ice_cream_flavors:
    prompt = f"""For the ice cream flavor listed below, 
    provide a captivating description that could be used for promotional purposes.

    Flavor: {flavor}

    """
    print_llm_response(prompt)


# Now that you know how to use lists, you can even save the promortional descriptions to another list using `.append()`:
#saving results to a list
promotional_descriptions = []
for flavor in ice_cream_flavors:
    prompt = f"""For the ice cream flavor listed below, 
    provide a captivating description that could be used for promotional purposes.

    Flavor: {flavor}

    """
    description = get_llm_response(prompt)
    promotional_descriptions.append(description)


# After you run that code, you should be able to access the promotional descriptions for each of your ice-cream flavors.
print(promotional_descriptions)


# ## Extra practice
# Translate the flavors in ice_cream_flavors to Spanish
ice_cream_flavors = ["Vanilla", "Strawberry"]

for flavor in ice_cream_flavors:
    prompt = f"""For the ice cream flavor listed below, 
    """
    ### --------------- ###
    print_llm_response(prompt)


# Write code to get a list with 
# words without typos

words_with_typos = ["Aple", "Wether", "Newpaper"]
words_without_typos = []

for word in words_with_typos:
    prompt = f"""Fix the spelling mistake in the following word: {word}
    Provide only the word.
    """
    correct_word = get_llm_response(prompt)
    ### WRITE CODE HERE  ###
    #Hint: Append the correct_word to the words_without_typos list 
    ### --------------- ###

print(words_without_typos)

