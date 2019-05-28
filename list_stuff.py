first_list = [1,2,3,4,5]
second_list = ['a','b',3.14, 10, 'this is a test']
print("1: ", first_list)
print("2: ", second_list)
third_list = first_list+second_list
first_list.extend(third_list)
fourth_list = first_list
print("3: ", third_list)
print("4: ", first_list)

sentence = input('How are you feeling today?')
my_words = sentence.split()
if my_words[0] == 'I':
	print('you\'re really think about yourself!')
else:
	print('have a good day')

sentence2 = input('Tell me about yourself?')
my_next_list = sentence2.split()
if 'shit' in my_next_list:
	print('STOP SWEARING!!!!')
elif 'I' in my_next_list:
	print('It is good you are focused on yourself')
elif 'bad' in my_next_list:
	print('I hope your day gets better')




