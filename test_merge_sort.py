from merge_sort import merge_sort
# import pytest


def test_merge_sort_one_element():
    assert merge_sort([6]) == [6]


def test_merge_sort_two_elements():
    assert merge_sort([6, 9]) == [6, 9]
    assert merge_sort([6, -9]) == [-9, 6]
    assert merge_sort([9, 9]) == [9, 9]


def test_merge_sort_even_length_list():
    assert merge_sort([6, 9, 2, 0]) == [0, 2, 6, 9]
    assert merge_sort([6, 9, 2, 0, 3, 6, 2, 5]) == [0, 2, 2, 3, 5, 6, 6, 9]


def test_merge_sort_odd_length_list():
    assert merge_sort([7, 6, 9, 2, 0]) == [0, 2, 6, 7, 9]
    assert merge_sort([6, 2, 0, -3, 6, 2, 5]) == [-3, 0, 2, 2, 5, 6, 6]
