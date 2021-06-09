def is_pangram(sentence):
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	for letter in alphabet:
		if (letter not in sentence) and (letter.capitalize() not in sentence):
			return False
	return True
	
