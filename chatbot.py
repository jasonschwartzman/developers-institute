# This program will be the 'library' for a set of functions to handle a multi-lingual chatbot.
# a chatbot is a way to get the computer to automatically understand / reply on questions without the need of a real person.
# We are not making a fancy one -- just one where we can in many languages get the information and problem to help with.
# so

def read_json_script(filename):
	import json
	with open(filename, 'r') as my_list:
		dict = json.loads(my_list.read())
	return dict

def get_language(dict):
	ask_user_language = input("what is your language you speak?")
	# Check if the language exists
	if ask_user_language in dict:
		language = ask_user_language
	else:
		print("No support for that language")
		language = 'en'
	return language

def get_user_details(language, dict):
	# ask each question
	questions = dict[language]
	answers = []
	for question in questions:
		answer = input(questions[question])
		answers.append(answer)
	# make a dictory of the results
	return answers

def get_service_call_number():
	# Pick any random number from 100000-999999
	service_call_number = 999999
	return service_call_number

def store_user_details(user_language, service_call_number, answers):
	my_json_output = {'lang': user_language, 'call_id': service_call_number, 'answers': answers}
	print("here is the json output ready to save in a file", my_json_output)
	#open file for write and save the my_json_output in the file.  
	return 

#Mainline
language_file = 'languages.json'
language_dict = read_json_script(language_file)
user_language = get_language(language_dict)
answers = get_user_details(user_language, language_dict)
service_call_number = get_service_call_number()
#print("Here is your language and your answers ",user_language, answers)
store_user_details(user_language, service_call_number, answers)
#Should work with receiving arguments/parameters...
#Step 1.  Read in a json file of the languages and the questions to ask.  
#(Make a function read_json_script and returns a dictionary)

#Step 2.  Ask which language they speak.  If it is not an available one then default to English.  (Make a function get_language, Ask the language, and based on a list of available return the selected language)
#Step 3.  Based on the language from step 2, ask for the name, phone, and problem.  Returns a dictionary of all the details. (This is a function get_user_details)
#Step 4.  Based on the user details from step 3, give the user a service call number.  (Make a function get_service_call_number)
#Step 5.  Store the user details, with the user language, and the service call, in a json file.

#This is a classic production type of flow.  When we learn about classes, we will be able to make some cool easier things, but this is an example of a multi-lingual app.
#FYI -- in the real world, I would not ASK the language but would take it from the browser or mobile as a default... or google translate.
#I want you to support English, Hebrew, French, Spanish, German, Turkish, Russian  -- You can easily get the text from any one of the native in the class.   I will do the spanish if you don't find someone.


#Here is a sample session:
#What language do you prefer to chat in?   English
#Good morning!
#How are you day?  I am your automated chatbot, and I would like to direct your call to the correct party.
#Please tell me your name:  Jason
#Hi, Jason, what is the best phone number to reach you?  +972545205096
#Ok, Jason, and what is your problem today? I can not figure out where the power plug on my phone is
#Ok, Jason, I am directing your call to the correct party.  Please wait.
#THank you for waiting.  Your service call number is #127834  A service representative will be contacting you shortly.



