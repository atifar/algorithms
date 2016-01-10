"""Unit tests for data_structs.py"""

from data_structs import Stack


def initialize_stack(*entries):
    s = Stack()
    for entry in entries:
        s.push(entry)
    return s


###########################################################################
# size
###########################################################################

def test_size_of_empty_stack():
    s = Stack()
    assert s.size() == 0


def test_size_of_nonempty_stack():
    s = initialize_stack(3, 82, 6, -581, 71)
    assert s.size() == 5


###########################################################################
# push
###########################################################################

def test_push_one_entry_onto_empty_stack():
    s = initialize_stack()
    s.push(48)
    assert s.size() == 1
    assert s.entries[-1] == 48


def test_add_entries_to_stack():
    s = initialize_stack(3, 82, 61)
    assert s.size() == 3
    s.push(-295)
    assert s.size() == 4
    assert s.entries[-1] == -295


###########################################################################
# top
###########################################################################

def test_top_of_empty_stack():
    s = initialize_stack()
    assert s.top() is None


def test_top_of_nonempty_stack():
    s = initialize_stack(3, 82, 61)
    assert s.top() == 61


###########################################################################
# pop
###########################################################################

def test_pop_from_nonempty_stack():
    s = initialize_stack(3)
    assert s.pop() == 3


def test_pop_from_empty_stack():
    s = initialize_stack()
    assert s.pop() is None
