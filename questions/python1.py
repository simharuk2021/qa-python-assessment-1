#------------------------------------------------------------------------------------------------------------------------------------------------------------------ 

	# INSTRUCTIONS

	# In case it is not clear, the Question appears first, then examples, then any hints and finally the function that you need to complete appears underneath:
	#
	# 	<QUESTION>
	#
	# 	<EXAMPLES>
	#
	# 	<HINT>

	# You are allowed access to the internet for this assessment, but remember you could use the DOCUMENTATION that comes bundled with your Python installation. 
	# Every command has help documentation. To read it:
	# 	1. Access Python from your CLI
	# 	2. Type help(<command>) and hit enter, where <command> is the command you want help with. For example: help(str)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------ 

	# <QUESTION 1>

	# Define a function that can accept two strings as input and returns the input with maximum length to the console. 
	
	# If two strings have the same length, then the function should return both strings separated by a " ".

	# In this case, the strings should be returned in the same order in which they were given.

	# <EXAMPLES>

	# one("hi","hello") → "hello"
	# one("three", "two") → "three"
	# one("three", "hello") → "three hello"

	# <HINT>

	# What was the name of the function we have seen to check the length of a container?  Use your CLI to access the Python documentation and get help(len).

def one(input1, input2):
    if len(input1) > len(input2):
        return(input1)
    elif len(input1) == len(input2):
        result = (input1, input2)
        return (" ".join(result))
    else:
        return(input2)    
# print(one("Hello", "Hi"))

#------------------------------------------------------------------------------------------------------------------------------------------------------------------ 

	# <QUESTION 2>

    # given a number
	# if this number is divisible by 3 return "fizz"
	# if this number is divisible by 5 return "buzz"
	# if this number is divisible by both 3 and 5 return "fizzbuzz"
	# if this number is not divisible by 3 or 5 return "null"
	    
    # <EXAMPLES>

	# two(3) → "fizz"
	# two(10) → "buzz"
	# two(15) → "fizzbuzz"
	# two(8) → "null"

	# <HINT>

	# No hints for this question

def two(arg1):
    if arg1 % 3 == 0 and arg1 % 5 == 0:
        return "fizzbuzz"
    elif arg1 % 5 == 0:
        return "buzz"
    elif  arg1 % 3 == 0:
        return "fizz"
    else:
        return "null"

#------------------------------------------------------------------------------------------------------------------------------------------------------------------ 

	# <QUESTION 3>

    # Write a function which returns the integer number of vowels in a given input. 
    # You should ignore case.

	# <EXAMPLES>

    # three("Hello") → 2
    # three("hEelLoooO") → 6

	# <HINTS>

	# How do we ignore case in a String? help(str) may offer some insight.

def three(input):
    vowels = 0
    for letter in input.lower():
        if letter in 'aeiouy':
            vowels += 1
    return vowels
        

#------------------------------------------------------------------------------------------------------------------------------------------------------------------ 

	# <QUESTION 4>

    # There is a well known mnemonic which goes "I before E, except after C", which is used to determine which order "ei" or "ie" should be in a word.
    
    # Write a function which returns the boolean True if a input follows the mnemonic, and returns the boolean False if not.

	# <EXAMPLES>

    # four("ceiling") → True
    # four("believe") → True
    # four("glacier") → False
    # four("height") → False

	# <HINT>

	# Step through the logic here in order to solve the problem, you may find help(range) helpful.

def four(input):
    if 'ei' in input:
        index = input.index('ei')
        if input[index - 1] == 'c':
            return True
        else:
            return False
    if 'ie' in input:
        index = input.index('ie')
        if input[index -1] == 'c':
            return False
        else:
            return True

#------------------------------------------------------------------------------------------------------------------------------------------------------------------ 

	# <QUESTION 5>

	# Write a function which takes an input (between 1 and 10 inclusive) and multiplies it by all the numbers before it.
	# eg If the input is 4, the function calculates 4x3x2x1 = 24 

	# <EXAMPLES>

	# five(1) → 1
	# five(4) → 24
	# five(8) → 40320

	# <HINT>

	# You may need to create a list of numbers from 0 to i, take a look at help(range).

def five(input):

    if input == 0:
        return 1
    return input * five(input - 1)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------ 

	# <QUESTION 6>

    # Given a input, int and a char, return a boolean value if the 'nth' 
    # (represented by the int provided) char of the String supplied is the same as the char supplied.
    # The int provided will NOT always be less than than the length of the String.
    # IGNORE case and Whitespace. 
    
    # <EXAMPLES>

	# six("The",2,'h') → True
	# six("AAbb",1,'b') → False
	# six("Hi-There",10,'e') → False

	# <HINT>

	# How do we find the length of a container, take a look at help(len), you will also need to look at help(str) for String manipulation.
 
def six(input, int, char):
	return False

#------------------------------------------------------------------------------------------------------------------------------------------------------------------ 

	# <QUESTION 7>

    # Given a input and a char, returns the position in the String where the char first appears.
    # Ensure the positions are numbered correctly, please refer to the examples for guidance.
    # DO NOT ignore case
    # IGNORE whitespace
    # If the char does not occur, return the number -1.
    
    # <EXAMPLES>

	# seven("This is a Sentence","s") → 4
	# seven("This is a Sentence","S") → 8
	# seven("Fridge for sale","z") → -1

	# <HINT>

	# Take a look at the documentation for Strings, List and range.

def seven(inputString, char):
	return -1

#------------------------------------------------------------------------------------------------------------------------------------------------------------------ 

	# <QUESTION 8>

    # Given a input seperate the input into the individual numbers present, then add each digit of each number to get a final value for each number

	# String example = "55 72 86"
	
	# "55" will = the integer 10
	# "72" will = the integer 9
	# "86" will = the integer 14
	
	# You then need to return the highest value, in the example above this would be 14.
	 
    # <EXAMPLES>

	# eight("55 72 86") → 14
	# eight("15 72 80 164") → 11
	# eight("555 72 86 45 10") → 15

	# <HINT>

	# help(int) for working with numbers and help(str) for working with Strings.

def eight(arg1):
	return 0

#------------------------------------------------------------------------------------------------------------------------------------------------------------------ 

	# <QUESTION 9>

    # Return the input that is between the first and last appearance of "bert" in the given input
	
	# Return the empty input "" if there is not 2 occurances of "bert" 
	
	# IGNORE CASE
    
    # <EXAMPLES>

	# nine("bertclivebert") → "clive"
	# nine("xxbertfridgebertyy") → "fridge"
	# nine("xxBertfridgebERtyy") → "fridge"
	# nine("xxbertyy") → ""
	# nine("xxbeRTyy") → ""

	# <HINT>

	# What was the name of the function we have seen to seperate a String? How can we make a input all upper or lower case?
	
	# Use your CLI to access the Python documentation and get help manipulating strings - help(str).

def nine(input):
	return ""

#------------------------------------------------------------------------------------------------------------------------------------------------------------------ 

	# <QUESTION 10>

    # Given a large input that represents a csv, the structure of each record will be as follows:
    
    # owner,nameOfFile,encrypted?,fileSize
    
    # "Bert,helloWorld.py,True,1447,Bert,strings.py,False,1318,Jeff,dice.py,False,1445"
    
    # For each record, if it is not encrypted, return the names of the owners of the files in a String Array.
    # Do not include duplicate names.
	# If all records are encrypted, return an empty Array.
    
    # <EXAMPLES>
    
    # ten("Jeff,random.py,False,1445") → ["Jeff"]
	# ten("Bert,numberGen.py,True,1447,Bert,integers.py,True,1318,Jeff,floats.py,False,1445") → ["Jeff"]
	# ten("Bert,boolean.py,False,1447,Bert,conditions.py,False,1318,Jeff,loops.py,False,1445") → ["Bert","Jeff"]
    # ten("Bert,prime.py,True,1447,Bert,ISBN.py,False,1318,Jeff,OOP.py,False,1445") → ["Bert","Jeff"]
    
	# <HINT>

	# Dont't forget, False is a String, not a Boolean value in the Tests above.

	# help(str) and help(list), you might also need to use a function that can create a list of numbers for you, try help(range).

def ten(input):
	return []

#------------------------------------------------------------------------------------------------------------------------------------------------------------------ 

