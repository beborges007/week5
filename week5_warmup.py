# Problem Set 1: Indexing and Slicing Strings
# Basic Indexing:
# Given the string magic = 'abracadabra',
magic = "abracadabra"
# a. Retrieve the 5th character.
print(magic[5])
# b. Retrieve the second to last character.
print(magic[-2])
# c. Find the first occurrence of the letter 'c'.
magicIndexed = magic.find("c")
print(magicIndexed)
# Advanced Slicing:
# Given the string alphabet = 'abcdefghijklmnopqrstuvwxyz',
# a. Extract the letters 'hij'.
text="abcdefghijklmnopqrstuvwxyz"
print(text[7:10])
# b. Extract every second letter starting from 'a' to 'm'.
print(text[0:13:2])
# c. Reverse the entire string using slicing.
print(text[::-1])
# Problem Set 2: Extracting Information
# From Descriptions:
# Extract the name of the famous personality from the quote "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"
quote = "Ask not what your country can do for you - ask what you can do for your country. - John F. Kennedy"
quoteIndexed = quote.find("John F. Kennedy")
print(quoteIndexed)
print(quote[83:])
# Manipulating Words:
# Given the string info = "Python is fun. Fun is good. Good is subjective.",
info = "Python is fun. Fun is good. Good is subjective."
# a. Extract the word 'subjective' without knowing its exact position.
Subjective = info.find("subjective")
print(Subjective)
print(info[36:-1])
# b. Extract every third word.
print(info[0:-1:3])
# c. Reverse the positions of the words, but keep the characters in each word in the same order.
print(info[::-1])
# Problem Set 3: String Methods
# Upper & Lower:
# Convert the following text to lowercase: "MAY THE FORCE BE WITH YOU."
sentence = "MAY THE FORCE BE WITH YOU."
print(sentence.lower())

# String Joining and Splitting:
word_list = ["Make", "haste", "slowly."]
joined_list = " ".join(word_list)
print(joined_list)
# b. Now, split the string at every occurrence of the letter 'a'.
newWord_list = joined_list.replace("a", "")
print(newWord_list)
# Replacing Words:
# Modify the sentence: "Life is what happens when you are busy making other plans."
# a. Replace "busy" with "distracted".
# b. Replace "plans" with "mistakes".
sentence2="Life is what happens when you are busy making other plans."
new_sentence = sentence2.replace("busy", "distracted").replace("plans", "mistakes")
# Problem Set 4: String Properties and Advanced Operations
# Repetition:
# Concatenate the word "Iteration" 7 times.
Iteration="Iteration" * 7 
print(Iteration)
# Word Search:
# Check if the word "moonlight" appears in the quote: "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"
sentence3="With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"
indexsentence3 = sentence3.find("moonlight")
hasMoonlight = False
print(f"Has Moonlight: {hasMoonlight}")
# Length and Count:
# a. Calculate the number of characters (including spaces and punctuation) in the word/phrase: "Supercalifragilisticexpialidocious".
word = "Supercalifragilisticexpialidocious"
print(len(word))
# b. Count the number of times the letter 'i' appears in the same word/phrase.
wordIndex = word.count("i")
print(wordIndex)