import unittest

from rhymes import RhymingDictionary


class TestIsRhymeSounds(unittest.TestCase):
	def test_possible_words(self):
		filename = "../../data/cmudict-0.7b.txt"
		rhyme_pairs = {
			"testicle1": [["CH", "EH2", "R"], ["S", "T", "EH1", "R"]],
			"testicle2": [["K", "UH1", "K", "IY0"], ["B", "UH1", "K", "IY0"]],
			"testicle3": [["G", "UH1", "D"], ["HH", "UH1", "D"]],
			"testicle4": [["Aw1"], ["Aw0"]],
			"testicle5": [["BEE", " ", "B", "IY1"], ["GEE", " ", "JH", "IY1"]]
			}
		no_rhyme_pairs = {
			"testicle1": [["B", "L", "AE1", "NG", "K", "AH0", "T"], ["B", "R" "AO1", "N", "ER0"]],
			"testicle2": [["D", "AO1", "G"], ["F", "R", "AA1", "G"]],
			"testicle3": [["B", "UH1", "K", "IY0"], ["F", "L", "OW1", "N"]],
			"testicle4": [["D", "IHO", "F", "AYl", "N"], ["R", "AYl", "M"]],
			"testicle5": [["M", "IH2", "N", "D", "AHO", "N", "AW1"], ["M", "AE1", "K", "5", "AHO", "M", "AHO"]],
			"testicle6": [[], []],
			"testicle7": [[], ["R", "AYl", "M"]],
			"testicle8": [["Aw0", "Awl"], ["Aw0", "Ay1"]]
		}
		for testicle in rhyme_pairs:
			self.assertTrue(
				RhymingDictionary.isRhymeSounds(
					rhyme_pairs[testicle][0], rhyme_pairs[testicle][1]))
		for testicle in no_rhyme_pairs:
			self.assertFalse(
				RhymingDictionary.isRhymeSounds(
					no_rhyme_pairs[testicle][0], no_rhyme_pairs[testicle][1]), no_rhyme_pairs[testicle][0])
	

if __name__ == '__main__':
	unittest.main()
