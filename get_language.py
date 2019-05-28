from googletrans import Translator
def get_language_from_input(linein):
	translator = Translator()
	result = translator.detect(linein)
	print(result)
	return result.lang


linein = input("Hi!  Good morning!")
language = get_language_from_input(linein)
print("You wrote to me in", language)