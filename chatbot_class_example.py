class Chatbot(object):
    chat_script = {}
    user_language = 'en'
    service_call_number = 0
    answers = []


    def read_chat_script(self, language_file):
        import json
        with open(language_file, 'r') as my_list:
            dict = json.loads(my_list.read())
        self.chat_script = dict
        return

    def get_language_from_input(self, linein):
        from googletrans import Translator
        translator = Translator()
        result = translator.detect(linein)
        print(result)
        return result.lang

    def get_language_automatically(self):
        ask_user_language = input("Hi! How can I help you? ")
        ul = self.get_language_from_input(ask_user_language)
        print("You wrote to me in", ul)
        #ul = ask_user_language.lower()
        # Check if the language exists
        if ul in self.chat_script:
            self.user_language = ul
        else:
            print("No support for that language.  Using English")
        return

    def get_user_details(self):
        # ask each question
        questions = self.chat_script[self.user_language]
        temp_answers = []
        for question in questions:
            answer = input(questions[question])
            temp_answers.append(answer)
        # make a dictionay of the results
        self.answers = temp_answers
        return

    def get_service_call_number(self):
        # Pick any random number from 100000-999999
        import random
        self.service_call_number = random.randint(100000,999999)
        return


my_chat_bot = Chatbot()
language_file = '/Users/yaakovschwartzman/Desktop/Python/languages.json'
my_chat_bot.read_chat_script(language_file)
my_chat_bot.get_language_automatically()
my_chat_bot.get_user_details()
my_chat_bot.get_service_call_number()

