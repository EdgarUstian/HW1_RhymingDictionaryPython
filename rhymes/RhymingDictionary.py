def isRhymeSounds(word1, word2):
	def getLastSyllable(pronunciation):
		vowel = ""
		position = 0
		for syllable in pronunciation:
			for letter in syllable:
				if letter in "AEIOU":
					vowel = syllable
		vowel_no_number = vowel[:-1]
		last_syllable = vowel_no_number
		for index in range(0, len(pronunciation)):
			if pronunciation[index] == vowel:
				position = index
		for syllable in range(position+1, len(pronunciation)):
			last_syllable += pronunciation[syllable]
		return last_syllable
	if getLastSyllable(word1) != getLastSyllable(word2):
		return False
	else:
		if not getLastSyllable(word1):
			return False
		else:
			return True

def getSounds(filename, word):
	dirty_sound = []
	clean_sound = []
	with open(filename) as file_input:
		for _ in range(56):
			next(file_input)
		for line in file_input:
			first_word = line.split("  ")[0]
			if word.upper() == first_word:
				dirty_sound = line.split("  ")[1].split(" ")
		for syllable in dirty_sound:
			clean_sound.append(syllable.strip("\n\r"))
		return clean_sound


def isRhyme(filename, word1, word2):
	pronunciation1 = getSounds(filename, word1)
	pronunciation2 = getSounds(filename, word2)
	if not pronunciation1 or not pronunciation2:
		return False
	else:
		return isRhymeSounds(pronunciation1, pronunciation2)

def findRhymes(filename, master_sword):
	rhyme_list = []
	all_sounds = {}
	def getAllSounds():
		all_sounds = {}
		with open(filename) as file_input:
			for _ in range(56):
				next(file_input)
			for line in file_input:
				split_line = line.split("  ")
				first_word = split_line[0]
				pronunciation = split_line[1].split(" ")
				all_sounds[first_word] = pronunciation
		return all_sounds
	all_sounds = getAllSounds()
	master_sword_pronunciation = all_sounds[master_sword.upper()]
	for word in all_sounds:
		if isRhymeSounds(master_sword_pronunciation, all_sounds[word]):
			rhyme_list.append(word)
		else:
			pass
	return rhyme_list
