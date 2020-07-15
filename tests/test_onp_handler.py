import pytest

phrase = '1 3 +'
result = 4


@pytest.mark.parametrize(
    "phrase_i, result_o",
    [(phrase, result)],
)
def test_onp_adding(onp_handler, phrase_i, result_o):
    assert (onp_handler.onp(phrase_i) == result_o)


phrase = '1 3 + 2 * 9 /'
result = 8/9


@pytest.mark.parametrize(
    "phrase_i, result_o",
    [(phrase, result)],
)
def test_onp_complex(onp_handler, phrase_i, result_o):
    assert (onp_handler.onp(phrase_i) == result_o)


phrase = '1 3 + 2 * 9 ~ /'
result = -8/9


@pytest.mark.parametrize(
    "phrase_i, result_o",
    [(phrase, result)],
)
def test_onp_complex_with_negation(onp_handler, phrase_i, result_o):
    assert (onp_handler.onp(phrase_i) == result_o)