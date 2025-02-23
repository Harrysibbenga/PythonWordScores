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
    expected_words = ['aa', 'bb', 'cab', 'bad', 'ace']
    assert high_scoring_words.valid_words == expected_words
    
def test_compute_word_scores(high_scoring_words):
    high_scoring_words.compute_word_scores()
    expected_scores = {'aa': 2, 'bb': 6, 'cab': 7, 'bad': 6, 'ace': 5}
    assert high_scoring_words.word_scores == expected_scores
    
def test_build_leaderboard_for_word_list(high_scoring_words):
    """Test if the leaderboard is built correctly."""
    high_scoring_words.compute_word_scores()
    
    expected_words = [('cab', 7), ('bad', 6), ('ace', 5)]
    returned_words = high_scoring_words.build_leaderboard_for_word_list()

    assert returned_words == expected_words
    
def test_build_leaderboard_for_letters_invalid_word(high_scoring_words):
    """Test that invalid words (e.g., 'bulb') are not included due to insufficient letters."""
    starting_letters = "bulx"  # Only one 'B' available, so 'bulb' is invalid
    
    # Mock word_scores to simulate computed scores
    high_scoring_words.word_scores = {
        "bus": 4,
        "bulb": 7,
        "bull": 8,
        "bushel": 9,
        "lux": 6
    }
    
     # Debugging: Print word_scores to ensure it's set correctly
    print(f"Word scores: {high_scoring_words.word_scores}")

    # Build the leaderboard
    leaderboard = high_scoring_words.build_leaderboard_for_letters(starting_letters)
    
     # Debugging: Print the returned leaderboard
    print(f"Leaderboard: {leaderboard}")
    
    # Define the expected leaderboard (sorted by score, then alphabetically)
    expected_leaderboard = [
        ("lux", 6),  # Valid word
    ]
    
    # Check if 'bulb' is excluded and the leaderboard matches the expected output
    assert leaderboard == expected_leaderboard
