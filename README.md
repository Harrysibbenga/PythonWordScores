# High Scoring Words Challenge

## Overview

This project implements a solution to a word scoring and leaderboard generation challenge. The goal is to create a Python class (`HighScoringWords`) that can:

1.  **Load word lists and letter scores:** Read valid words from a file (`wordlist.txt`) and letter scores from another file (`letterValues.txt`).
2.  **Compute word scores:** Calculate the score for each word based on the provided letter scores.
3.  **Build a leaderboard from the word list:** Generate a leaderboard of the top 100 highest-scoring words from the full word list, sorted by score (descending) and then alphabetically.
4.  **Build a leaderboard from given letters:** Create a leaderboard of the top 100 highest-scoring words that can be formed using a given set of letters, respecting letter counts, and sorted similarly.

## Thought Process

### 1.  Data Loading and Initialization

* The first step was to load the word list and letter scores from the provided text files.
* I used `open()` and `readlines()` to read the files, splitting the word list into a list of strings and the letter scores into a dictionary (`letter_values`).
* Error handling was added to catch `FileNotFoundError` and log the error, and raise the error again.
* Logging was added to show data loading success.

### 2.  Word Score Computation

* The `compute_word_scores()` method calculates the score for each word in the `valid_words` list.
* It iterates through each word and sums the scores of its letters, using the `letter_values` dictionary.
* A dictionary `word_scores` stores the word-score pairs.
* Logging was added to show that scores have been calculated.

### 3.  Leaderboard from Word List

* The `build_leaderboard_for_word_list()` method generates the top 100 leaderboard.
* It filters words shorter than `MIN_WORD_LENGTH`.
* It sorts the words by score (descending) and then alphabetically using `sorted()` and a lambda function as the key.
* It returns the top 100 words (or fewer if there are fewer valid words).
* Logging was added to show the leaderboard has been built.

### 4.  Leaderboard from Given Letters

* The `build_leaderboard_for_letters()` method is the core of the challenge.
* It uses `collections.Counter` to count the occurrences of letters in the `starting_letters` string and each word.
* It iterates through the `word_scores` dictionary, checking if each word can be formed using the available letters.
* A word is valid if all its letters are in `available_letters` and their counts do not exceed the available counts.
* It sorts the valid words by score (descending) and then alphabetically.
* It returns the top 100 valid words.
* Logging was added to show the available letters, and to show when a word is being checked, and if it is valid or invalid, and why.
* Logging was added to show the leaderboard has been built.

### 5. Production ready changes.

* Added logging to show the process of the program.
* Added error handling to deal with missing files.
* Added docstrings to functions.
* added if `__name__ == "__main__":` to ensure the code only runs when called directly.

## Solution Structure

* **`HighScoringWords` class:** Contains the logic for loading data, computing scores, and building leaderboards.
* **Data files:** `wordlist.txt` and `letterValues.txt` store the word list and letter scores.
* **`if __name__ == "__main__":` block:** Contains example usage and testing.

## How to Run Tests

1.  **Ensure data files:** Place `test_wordlist.txt` and `test_letterValues.txt` in the `tests/` directory or update the paths in the code. Note you can ccopy the original ones and make them smaller for testing !!
2.  **Run the script:** `pytest tests\test.py`

## How to Run

1.  **Ensure data files:** Place `wordlist.txt` and `letterValues.txt` in the `data/` directory or update the paths in the code.
2.  **Run the script:** `python app\high_scoring_words.py`

## Improvements

* Implement more efficient algorithms for larger word lists.
* Add more robust error handling and input validation.
* Add the ability to change the `MAX_LEADERBOARD_LENGTH` and `MIN_WORD_LENGTH` from command line arguments.