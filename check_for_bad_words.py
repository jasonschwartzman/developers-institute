def get_a_sentence():
	# do this
	linein = input("What is your sentence to check? ")
	return linein

def check_for_bad_words(sentence_to_check):
	# do this
	bad_words = ['hell', 'damn']
	words = sentence_to_check.split()
	dirty = False
	for each_word in words:
		if each_word in bad_words:
			dirty = True
	return dirty

# Mainline
for counter in range(5):
	# get a sentence
	sentence = get_a_sentence()
	# check for bad words
	if check_for_bad_words(sentence):
		print("Stop writing bad words!!!")
	else:
		print("You typed a clean sentence")
	# do something



