# IPND Stage 2 Final Project
# By: Kristen Davis
# Completed on 4/26/2016

import textwrap
#Quiz Library---------------------------------------------------------------------------------
easy_quiz = '''    ___1___ is the abbreviation for HyperText Markup Language. ___1___ defines
the ___2___ and content of a website. ___1___ has a ___3___-like structure called
the ___4___ (Document Object Model).
    ___5___ is the abbreviation for Cascading Style Sheets. ___5___ defines the
___6___ of the site. In ___5___ the most ___7___ overules the more general rules.
Avoid ___8___ style elements if possible.
    The ___9___ Model is the structure of a website's layout. The very
center element is the ___10___. ___11___ clears an area around the ___10___ and
the ___12___ frames them both.'''

medium_quiz = '''    A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes
by adding ___2___ separated by commas between the parentheses. ___1___s by default return
___3___ if you don't specify the value to return. ___2___ can be standard data types such
as ___4___, number, dictionary, tuple, and list or can be more complicated such as
objects and lambda functions.
    A ___5___ can be a sequence of anything surrounded by []. Specific locations
in a ___5___ can utilized by their ___6___. You start counting an ___6___ at ___7___. The
length of a ___5___ can be found using the ___8___() method.
    ___9___s let you repeat a task over and over without repeating code. ___10___
___9___s repeat as long as the condition in the first line is true. ___11___ ___9___s
iterate through every item in a list. An ___12___ ___9___ would continue forever and crash
your program. Avoid these!'''

hard_quiz = '''    ___1___ is the process of fixing what's broken in your code. In Python, error
messages are called ___2___s. In a ___2___ you are given the ___3___ number and error ___4___.
    ___5___ is your best friend when trying to decipher tracebacks. Other
good strategies include checking ___6___ results. Go through your code step by
step and compare to ___7___ code. ___8___ along the way to help see errors.
    ___9___ are often harder to find when they do not cause ___10___s. Use ___11___s
to make sure you cover all of the ___12___ cases when ___11___ing your code.'''

test_quiz = '''___1___, ___2___, ___3___, ___4___, ___5___, ___6___, ___7___, ___8___, ___9___,
___10___, ___11___s, ___12___fjkd'''

quiz_library = [easy_quiz, medium_quiz, hard_quiz, test_quiz]
#End Quiz Library-----------------------------------------------------------------------------

#Answer Set Library---------------------------------------------------------------------------
easy_answer_set = ["HTML","structure","tree","DOM",
				   "CSS","look","specific","inline",
				   "Box","Content","Padding","Border"]
medium_answer_set = ["function", "arguments", "none", "string",
					 "list", "index", "0", "len",
					 "loop", "while", "for", "infinite"]
hard_answer_set = ["debugging","traceback","line","type",
				   "Google","intermediate","example","print",
				   "bugs","error","test","edge"]
test_answer_set = ["1", "2", "3", "4",
				   "5", "6", "7", "8",
				   "9", "10", "11", "12"]

answer_set_library = [easy_answer_set, medium_answer_set, hard_answer_set, test_answer_set]
#End Answer Set Library-----------------------------------------------------------------------

#indicates the fill-in-the-blank to be replaced options
blank_set = ["___1___", "___2___", "___3___", "___4___",
			 "___5___", "___6___", "___7___", "___8___",
			 "___9___", "___10___", "___11___", "___12___",]

#storage list for user-inputted answers
answers = ["", "", "", "",
		   "", "", "", "",
		   "", "", "", ""]

#checks if current word in quiz is a blank value
def is_blank(word, blank_set):
	for blank in blank_set:
		if blank in word:
			return blank
	return None

#checks user_input for the current_blank against answer_set[blank_index] for accuracy
def check_answer(current_blank, blank_index, answer_set):
	user_input = raw_input("Fill in blank " + current_blank + ": ")
	if user_input == answer_set[blank_index]:
		print "\n" + "*"*8 + "\nCorrect!\n" + "*"*8 + "\n"
		return user_input
	else:
		print "\n" + "*"*29
		choice = raw_input("Incorrect. Try again? Y or N: ")
		print "*"*29 + "\n"
		if choice == "Y":
			return check_answer(current_blank, blank_index, answer_set)
		else:
			exit()

#given the quiz and correct user_input, replace all occurances of current_blank with user_input
def fill_blanks(quiz, difficulty):
	blank_index = 0
	while blank_index < len(blank_set):
		current_blank = blank_set[blank_index]
		if current_blank in quiz:
			answer_set = answer_set_library[difficulty]
			user_input = check_answer(current_blank, blank_index, answer_set)
			quiz = quiz.replace(current_blank, user_input, 4)
			print textwrap.fill(quiz)
			blank_index += 1
		else:
			blank_index += 1


#given user input, outputs a value indicating difficulty level
def set_difficulty_level(difficulty):
	difficulty_level = raw_input("Please select a difficulty level: easy, medium, or hard: \n")
	if difficulty_level == "easy":
		difficulty = 0
	elif difficulty_level == "medium":
		difficulty = 1
	elif difficulty_level == "hard":
		difficulty = 2
	elif difficulty_level == "test":
		difficulty = 3
	else:
		print "Input not recognized; please try again: \n"
		set_difficulty_level(difficulty)
	return difficulty

#main function of program, used to call other functions and inform user of beginning and end
def take_quiz():
	print " "
	print "*"*33 + "\n Welcome to the Vocabulary Quiz! \n"+ "*"*33 + "\n"
	difficulty = 0
	difficulty = set_difficulty_level(difficulty)
	quiz = quiz_library[difficulty]
	print "\n" + textwrap.fill(quiz)
	fill_blanks(quiz, difficulty)
	print "\n" + "*"*40 + "\nCongratulations! You completed the quiz!\n" + "*"*40

take_quiz()