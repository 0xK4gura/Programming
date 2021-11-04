# How to split 'Hello' from 'Hello World'

text = "Hello World" # setting the string value in 'text' variable

def first_word(text): # defining a function called 'first_word' that takes string from variable text
    return text.split()[0] # split the word and return the 1st position [0] to the function
    
print(first_word(text)) # print the function that called the variable