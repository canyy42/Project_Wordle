import pytest
from project import get_feedback, validate_guess

# Note: we don't test network functions like load_words() or get_secret_word() directly,
# because they involve randomness or external requests.


def test_validate_guess_valid():
    word_list = ["apple", "grape", "brick"]
    assert validate_guess("apple", word_list)


def test_validate_guess_invalid_length():
    word_list = ["apple", "grape", "brick"]
    assert not validate_guess("app", word_list)


def test_validate_guess_not_in_list():
    word_list = ["apple", "grape", "brick"]
    assert not validate_guess("zebra", word_list)


def test_get_feedback_all_green():
    assert get_feedback("apple", "apple") == ["green"] * 5


def test_get_feedback_some_yellow():
    assert get_feedback("crane", "cared") == ["green", "yellow", "yellow", "gray", "gray"]


def test_get_feedback_all_gray():
    assert get_feedback("apple", "thumb") == ["gray", "gray", "gray", "gray", "gray"]


def test_get_feedback_mixed_case():
    assert get_feedback("spine", "sneak") == ["green", "gray", "yellow", "gray", "gray"]
