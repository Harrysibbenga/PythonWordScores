import pytest
from app.highscoringwords import HighScoringWords

@pytest.fixture
def high_scoring_words():
    """Fixture to initialize HighScoringWords with test files."""
    return HighScoringWords("tests/test_wordlist.txt", "tests/test_letterValues.txt")

def test_load_letter_values(high_scoring_words):
    """Test if letter values are loaded correctly."""
    expected_values = {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1}
    assert high_scoring_words.letter_values == expected_values

def test_load_word_list(high_scoring_words):
    """Test if words are loaded correctly."""
    expected_words = ['cab', 'bad', 'ace']
    assert high_scoring_words.valid_words == expected_words