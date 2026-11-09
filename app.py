# Step 1
# In this workshop, you will create a program that implements a Caesar cipher, an encryption method that shifts letters in the alphabet to encode messages. Start by creating a variable called shift and assign the value 5 to your new variable.
shift = 5

# Step 2
# Declare another variable called alphabet and assign the string abcdefghijklmnopqrstuvwxyz to this variable.
alphabet = "abcdefghijklmnopqrstuvwxyz"

# Step 3
# In this workshop, you are going to build a Caesar cipher. A Caesar cipher encrypts text by replacing each letter of the plaintext with a letter a fixed number of positions later in the alphabet. For example, with a shift of 5, a would be replaced by f, b by g and so on.

# To implement this cipher, you'll need to create a new version of your alphabet that starts at the position indicated by the shift. As you learned in a previous lesson, you can extract part of a string using string slicing:

# Example Code
# fcc = 'freeCodeCamp'
# print(fcc[8:]) # Camp
# Create a variable named shifted_alphabet and use the slicing syntax to assign it the portion of alphabet that starts at the index of shift. Then, call the built-in print() function to print shifted_alphabet on the terminal and look at the result.
shifted_alphabet =  alphabet[shift:]+ alphabet[:shift]
print(shifted_alphabet)

# Step 4
# As you can see from the output, the shifted alphabet starts at the letter f because shift has the value 5. But now the first five letters of the alphabet – a, b, c, d and e – are missing from the shifted alphabet, so you'll need to add them at the end of the shifted alphabet. You can use the + operator to concatenate the missing portion of the alphabet.

# Modify the existing assignment of the shifted_alphabet variable: use the slicing syntax to extract the missing first portion of alphabet and concatenate it to alphabet[shift:].

# As a reminder, sentence[start:stop] returns the characters of sentence from position start (included) to stop (excluded).
#
