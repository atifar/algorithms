"""Unit tests for data_structs.py"""

from data_structs import Stack, Queue


###########################################################################
# stack tests #############################################################
###########################################################################

def initialize_stack(*entries):
    s = Stack()
    for entry in entries:
        s.push(entry)
    return s


###########################################################################
# stack creation
###########################################################################

def test_create_empty_stack():
    s = Stack()
    assert s.entries == []


def test_create_stack_with_entries():
    STACK_ENTRIES = (-4, 2, 999, 17, 0)
    s = initialize_stack(*STACK_ENTRIES)
    for idx, entry in enumerate(STACK_ENTRIES):
        assert s.entries[idx] == entry


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


###########################################################################
# queue tests #############################################################
###########################################################################

def initialize_queue(*entries):
    q = Queue()
    for entry in entries:
        q.push(entry)
    return q


###########################################################################
# queue creation
###########################################################################

def test_create_empty_queue():
    q = Queue()
    assert q.entries == []


def test_create_queue_with_entries():
    QUEUE_ENTRIES = (99, 0, -58, 17, 30)
    q = initialize_queue(*QUEUE_ENTRIES)
    for idx, entry in enumerate(QUEUE_ENTRIES):
        assert q.entries[-1 - idx] == entry


###########################################################################
# push
###########################################################################

def test_push_one_entry_onto_empty_queue():
    q = initialize_queue()
    q.push(48)
    assert q.size() == 1
    assert q.entries[-1] == 48


def test_add_entries_to_queue():
    q = initialize_queue(3, 82, 61)
    assert q.size() == 3
    q.push(-295)
    assert q.size() == 4
    assert q.entries[0] == -295


###########################################################################
# end
###########################################################################

def test_end_of_empty_queue():
    q = initialize_queue()
    assert q.end() is None


def test_end_of_nonempty_queue():
    q = initialize_queue(3, 82, 61)
    assert q.end() == 3


###########################################################################
# pop
###########################################################################

def test_pop_from_nonempty_queue():
    q = initialize_queue(3)
    assert q.pop() == 3


def test_pop_from_empty_queue():
    q = initialize_queue()
    assert q.pop() is None
