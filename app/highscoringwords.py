from collections import Counter
import logging

__author__ = 'codesse'

# Configure logging for production use
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class HighScoringWords:
    MAX_LEADERBOARD_LENGTH = 100  # the maximum number of items that can appear in the leaderboard
    MIN_WORD_LENGTH = 3  # words must be at least this many characters long
    letter_values = {}
    valid_words = {}

    def __init__(self, validwords='data/wordlist.txt', lettervalues='data/letterValues.txt'):
        """
        Initialise the class with complete set of valid words and letter values by parsing text files containing the data.
        :param validwords: a text file containing the complete set of valid words, one word per line.
        :param lettervalues: a text file containing the score for each letter in the format letter:score one per line.
        :return: None
        """
        try:
            with open(validwords) as f:
                self.valid_words = f.read().splitlines()
            logging.info(f"Loaded {len(self.valid_words)} valid words.")
        except FileNotFoundError:
            logging.error(f"Valid words file not found: {validwords}")
            raise

        try:
            with open(lettervalues) as f:
                for line in f:
                    (key, val) = line.split(':')
                    self.letter_values[str(key).strip().lower()] = int(val)
            logging.info(f"Loaded letter values for {len(self.letter_values)} letters.")
        except FileNotFoundError:
            logging.error(f"Letter values file not found: {lettervalues}")
            raise

    def compute_word_scores(self):
        """
        Compute scores for all words in the valid word list.
        """
        self.word_scores = {
            word: sum(self.letter_values.get(char, 0) for char in word)
            for word in self.valid_words
        }
        logging.info("Computed word scores.")

    def build_leaderboard_for_word_list(self):
        """
        Build a leaderboard of the top scoring MAX_LEADERBOAD_LENGTH words from the complete set of valid words.
        :return: The list of top words.
        """

        # Ensure scores are computed
        if not hasattr(self, 'word_scores'):
            self.compute_word_scores()

        # Filter words based on minimum length
        filtered_words = {word: score for word, score in self.word_scores.items()
                          if len(word) >= self.MIN_WORD_LENGTH}

        # Sort words by score (descending), then alphabetically
        sorted_words = sorted(filtered_words.items(), key=lambda x: (-x[1], x[0]))

        # Return top 100 words
        logging.info("Built leaderboard for word list.")
        return sorted_words[:self.MAX_LEADERBOARD_LENGTH]

    def build_leaderboard_for_letters(self, starting_letters):
        """
        Build a leaderboard of the top scoring MAX_LEADERBOARD_LENGTH words that can be built using only the letters contained in the starting_letters String.
        """

        available_letters = Counter(starting_letters.upper())
        valid_words = {}

        logging.debug(f"Available letters: {available_letters}")

        for word, score in self.word_scores.items():
            word_counter = Counter(word.upper())
            logging.debug(f"Checking word: {word}, Word counter: {word_counter}")

            is_valid = True
            for char, count in word_counter.items():
                if char not in available_letters or count > available_letters[char]:
                    is_valid = False
                    logging.debug(f"  Word {word} is invalid because {char} count is {count}, available is {available_letters.get(char,0)}")
                    break

            if is_valid:
                valid_words[word] = score
                logging.debug(f"  Word {word} is valid with score {score}")

        sorted_words = sorted(valid_words.items(), key=lambda x: (-x[1], x[0]))
        logging.info(f"Built leaderboard for letters: {starting_letters}")
        return sorted_words[:self.MAX_LEADERBOARD_LENGTH]


if __name__ == "__main__":
    high_scoring_words = HighScoringWords()

    letters = "bulx"

    high_scoring_words.compute_word_scores()
    leaderboard_for_word_list = high_scoring_words.build_leaderboard_for_word_list()
    leaderboard_for_letters = high_scoring_words.build_leaderboard_for_letters(letters)

    print(f" Leaderboard words from word list {letters} ==== >> {leaderboard_for_word_list}")

    print(f" Leaderboard words from letters {letters} ==== >> {leaderboard_for_letters}")