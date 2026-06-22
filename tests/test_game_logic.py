from logic_utils import (
    check_guess,
    get_range_for_difficulty,
    parse_guess,
    update_score,
)


def test_winning_guess():
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert "Correct" in message


def test_guess_too_high():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message


def test_guess_too_low():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message


def test_parse_guess_valid_integer():
    ok, value, error = parse_guess("42")
    assert ok is True
    assert value == 42
    assert error is None


def test_parse_guess_valid_decimal_string():
    ok, value, error = parse_guess("42.0")
    assert ok is True
    assert value == 42
    assert error is None


def test_parse_guess_invalid_input():
    ok, value, error = parse_guess("abc")
    assert ok is False
    assert value is None
    assert error == "That is not a number."


def test_get_range_for_easy():
    assert get_range_for_difficulty("Easy") == (1, 20)


def test_get_range_for_normal():
    assert get_range_for_difficulty("Normal") == (1, 50)


def test_get_range_for_hard():
    assert get_range_for_difficulty("Hard") == (1, 100)


def test_update_score_for_win_minimum_points():
    score = update_score(0, "Win", 10)
    assert score == 10


def test_update_score_for_too_high_even_attempt():
    score = update_score(10, "Too High", 2)
    assert score == 15


def test_update_score_for_too_high_odd_attempt():
    score = update_score(10, "Too High", 3)
    assert score == 5


def test_update_score_for_too_low():
    score = update_score(10, "Too Low", 4)
    assert score == 5
