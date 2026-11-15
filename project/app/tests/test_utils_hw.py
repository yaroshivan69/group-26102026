from app.utils.utils import calculate_discount, is_even, get_full_name

def test_calculate_discount_20_percent() -> None:
    assert calculate_discount(100.0, 20.0) == 80.0

def test_calculate_discount_50_percent() -> None:
    assert calculate_discount(200.0, 50.0) == 100.0

def test_calculate_discount_0_percent() -> None:
    assert calculate_discount(150.0, 0.0) == 150.0

def test_calculate_discount_zero_price() -> None:
    assert calculate_discount(0.0, 25.0) == 0.0

def test_calculate_discount_other_valid() -> None:
    assert calculate_discount(80.0, 15.0) == 68.0

def test_is_even_positive_even() -> None:
    assert is_even(4) is True


def test_is_even_positive_odd() -> None:
    assert is_even(7) is False


def test_is_even_negative_even() -> None:
    assert is_even(-6) is True


def test_is_even_negative_odd() -> None:
    assert is_even(-3) is False


def test_is_even_zero() -> None:
    assert is_even(0) is True

def test_get_full_name_standard() -> None:
    assert get_full_name("Тарас", "Шевченко") == "Тарас Шевченко"


def test_get_full_name_short() -> None:
    assert get_full_name("Ян", "Лі") == "Ян Лі"


def test_get_full_name_long() -> None:
    assert get_full_name("Олександр", "Костянтинопольський") == "Олександр Костянтинопольський"


def test_get_full_name_single_char() -> None:
    assert get_full_name("А", "Б") == "А Б"


def test_get_full_name_other_valid() -> None:
    assert get_full_name("Леся", "Українка") == "Леся Українка"