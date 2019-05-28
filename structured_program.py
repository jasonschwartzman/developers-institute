def get_bad_words(bad_words_file_name):
	file = open(bad_words_file_name, "r")
	if file.mode == "r":
		bad_words_text = file.read()
	else:
		bad_words_text = ''
	file.close()
	bad_words = bad_words_text.split()
	return bad_words

def write_out_sentence(file, sentence):
	if file.mode == 'w+':
		file.write(sentence)

def get_a_sentence():
	# do this
	linein = input("What is your sentence to check? ")
	return linein

def check_for_bad_words(bad_words, sentence_to_check):
	# do this
	#bad_words = ['hell', 'damn']
	words = sentence_to_check.split()
	dirty = False
	for each_word in words:
		if each_word in bad_words:
			dirty = True
	return dirty

def read_and_sanitize_input(bad_words_filename, how_many_lines, output_file):
	bad_words_list = get_bad_words(bad_words_filename)
	for counter in range(how_many_lines):
		# get a sentence
		sentence = get_a_sentence()
	# check for bad words
		if check_for_bad_words(bad_words_list, sentence):
			print("Stop writing bad words!!!")
		else:
			print("You typed a clean sentence")
			write_out_sentence(output_file, sentence)

# Mainline
print("Starting my first structured program")
outputfile = open("clean_sentences.txt", "w+")
bad_words_filename = "badwords.txt"
number_of_sentences = 5
read_and_sanitize_input(bad_words_filename, number_of_sentences, outputfile)
outputfile.close()
print("Finished my first structured program")


