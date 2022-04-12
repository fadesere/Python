# create a function that prints out a greeting
# to any name passed to the function
def greet_me(a_name):
    print("Hello "+a_name)
# create a variable named author
author = "Susan E. McGregor"
# create another variable named editor
editor = "Jeff Bleiel"
# use my custom function, `greet_me` to output "Hello" messages to each person
greet_me(author)
greet_me(editor)

name = "hello world"
print(name.title())



# splitting a string "literal" and then printing the result
split_world = "Hello World!".split()
print(split_world)
# assigning a string to a variable
# then printing the result of calling the `split()` method on it
world_msg = "Hello World!"
print(world_msg.split())



# fictional list of chapter page counts
page_counts = [28, 32, 44, 23, 56, 32, 12, 34, 30]
# `print()` the result of using the `sum()` function on the list
print(sum(page_counts))