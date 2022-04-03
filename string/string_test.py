import datetime
import calendar
from math import pi

# time 
def get_string_len(sMsg):
	count = 0
	for char in sMsg:
		count += 1
	return count

def get_count_number_character(sMsg):
	arr_char = {}
	for aChar in sMsg:
		if aChar not in arr_char:
			count = 0
			for aChar_temp in sMsg:
				if aChar_temp == aChar:
					count += 1
			arr_char.update({aChar:count})
			
	for key, value in arr_char.items():
		print(key, value)

def convert_list_to_string():
	my_list = ['abc','xyz']
	string_new = " ".join(my_list)
	return string_new

def chars_mix_up():
	my_list = ['abc','xyz']
	new_a = my_list[0]
	new_b = my_list[1]
	
	new_a_temp = new_b[:2] + new_a[2:]
	new_b_temp = new_a[:2] + new_b[2:]
	
	new_string = new_a_temp + ' ' + new_b_temp
	return new_string

def convert_noun_to_adverb(my_str):
	count = get_string_len(my_str)
	if count > 2:
		my_str_end = my_str[count-3:]
		if my_str_end == 'ing':
			my_str += 'ly'
		else:
			my_str += 'ing'
	return my_str	

def get_the_longest_word_in_list(my_list):
	count = 0
	longest_word = ''
	for my_str in my_list:
		count_temp = get_string_len(my_str)
		if count < count_temp:
			count = count_temp
			longest_word = my_str
	return longest_word

def get_count_number_word(sMsg):
	arr_words = {}
	words = sMsg.split()
	
	for aWord in words:
		if aWord not in arr_words:
			count = 0
			for aChar_temp in words:
				if aChar_temp == aWord:
					count += 1
			arr_words.update({aWord:count})
			
	for key, value in arr_words.items():
		print(key, value)

def get_last_string_with_specified_character(specifed_char, sMsg):
	my_splited_word = sMsg.rsplit(specifed_char, 1)[0]
	return my_splited_word

def reverse_string(my_str):
	reverse_str = ''.join(reversed(my_str))
	return reverse_str


get_count_number_character('thequickbrownfoxjumpsoverthelazydog')
get_count_number_word('the quick brown fox jumps over the lazy dog.')
convert_list_to_string()
print('get_string_len: ', get_string_len('w3resource.com'))
print('chars_mix_up: ', chars_mix_up())
print('reverse_string: ', reverse_string('w3resource.com'))
print('convert_noun_to_adverb: ', convert_noun_to_adverb('stringtest'))
print('convert_noun_to_adverb: ', convert_noun_to_adverb('string'))
print('convert_noun_to_adverb: ', convert_noun_to_adverb('ab'))
print('get_the_longest_word_in_list: ', get_the_longest_word_in_list(["PHP", "Exercises", "Backend"]))
print('get_last_string_with_specified_character: ', get_last_string_with_specified_character('/', 'https://www.w3resource.com/python-exercises'))
