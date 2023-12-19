
def count_words(text):
	word_count = text.split()
	return len(word_count)

def count_letters(text):
	letter_freq = {}
	for letter in text:
		l = letter.lower()
		if l in letter_freq:
			letter_freq[l] += 1
		else:
			letter_freq[l] = 1
	return letter_freq

with open("books/frankenstein.txt") as f:
		text = f.read()
		letter_freq = count_letters(text)
		letter_freq_sorted = sorted(letter_freq.items(), key = lambda x: -x[1])
		letter_freq_sorted_and_filtered = list(filter(lambda x: x[0].isalpha(), letter_freq_sorted))
		print("--- Begin report of books/frankenstein.txt ---")
		print(f"{count_words(text)} words found in the document\n")
		for letter, freq in letter_freq_sorted_and_filtered:
			print(f"The '{letter}' character was found {freq} times")
		print("--- End report ---")