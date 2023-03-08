import pytest
from algorithms import SecretAlgorithm


@pytest.fixture
def algo_instance():
    return SecretAlgorithm()


def test_calculate_suitability_score(algo_instance):
    # any input is empty causes score 0
    assert algo_instance.calculate_suitability_score(driver="", destination="") == 0
    assert algo_instance.calculate_suitability_score(driver="a", destination="") == 0
    assert algo_instance.calculate_suitability_score(driver="", destination="a") == 0

    # even length of destination, no common factor other than 1 between driver's name and destination
    assert algo_instance.calculate_suitability_score(driver="aaabb", destination="even") == 4.5

    # even length of destination, has common factor other than 1 between driver's name and destination
    assert algo_instance.calculate_suitability_score(driver="aaab", destination="even") == 6.75

    # odd length of destination, no common factor other than 1 between driver's name and destination
    assert algo_instance.calculate_suitability_score(driver="aaabb", destination="odd") == 2.0

    # odd length of destination, has common factor other than 1 between driver's name and destination
    assert algo_instance.calculate_suitability_score(driver="aaabbb", destination="odd") == 4.5


def test_optimized_result(algo_instance):
    # empty drivers or destinations cause an Exception (the default value is a empty list)
    with pytest.raises(Exception):
        algo_instance.optimized_result()
    with pytest.raises(Exception):
        algo_instance.set_drivers(["test"])
        algo_instance.optimized_result()
    algo_instance = SecretAlgorithm()
    with pytest.raises(Exception):
        algo_instance.set_destinations(["test"])
        algo_instance.optimized_result()
    algo_instance = SecretAlgorithm()

    # any non-string in the lists causes an Exception
    with pytest.raises(Exception):
        algo_instance.set_drivers(["test1", 1, "test2"])
        algo_instance.set_destinations(["test3"])
        algo_instance.optimized_result()
    algo_instance = SecretAlgorithm()

    # get the right result with a set of valid input
    algo_instance.set_drivers(["aaaa", "abca", "efgh"])
    algo_instance.set_destinations(["aaaa", "bbb"])
    assert algo_instance.optimized_result() == (12.0, [("aaaa", "aaaa"), ("efgh", "bbb")])

# we can't run test for private methods, this is showing the cases I considered while building that method
# def test_vowel_and_consonant_count():
#     assert algo_instance.__vowel_and_consonant_count("abcde") == {"vowel": 2, "consonant": 3}
#     assert algo_instance.__vowel_and_consonant_count("AbCde") == {"vowel": 2, "consonant": 3}
#     assert algo_instance.__vowel_and_consonant_count("ab c d e ") == {"vowel": 2, "consonant": 3}
#     assert algo_instance.__vowel_and_consonant_count("  ") == {}
#     assert algo_instance.__vowel_and_consonant_count("") == {}
