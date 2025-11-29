import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.math_ import fact, fact_recurs, fibb, fibb_recurs
from src.sort import bobble, count, heapy, bucket_s, qsort
from src.stract_ import Stack, Queue

def test_math():
    assert fact(5) == 120
    assert fact(1) == 1
    assert fact(0) == 1
    assert fact_recurs(5) == 120
    assert fact_recurs(1) == 1
    
    assert fibb(6) == 8
    assert fibb(1) == 1
    
    assert fibb_recurs(6) == 8
    assert fibb_recurs(1) == 1
    
def test_sort():    
    a = [5, 2, 8, 1, 9]
    b = [3, 1, 4, 1, 5, 9, 2, 6]
    c = [0.42, 0.32, 0.33, 0.52, 0.37, 0.47]
    
    sorted_bobble = bobble(a.copy(), len(a))
    assert sorted_bobble == [1, 2, 5, 8, 9]
    
    sorted_bobble2 = bobble(b.copy(), len(b))
    assert sorted_bobble2 == [1, 1, 2, 3, 4, 5, 6, 9]
    
    sorted_count = count(b.copy(), len(b))
    assert sorted_count == [1, 1, 2, 3, 4, 5, 6, 9]
    
    sorted_count2 = count(a.copy(), len(a))
    assert sorted_count2 == [1, 2, 5, 8, 9]
    
    sorted_heap = heapy(a.copy(), len(a))
    assert sorted_heap == [1, 2, 5, 8, 9]
    
    sorted_heap2 = heapy(b.copy(), len(b))
    assert sorted_heap2 == [1, 1, 2, 3, 4, 5, 6, 9]
    
    sorted_bucket = bucket_s(c.copy(), len(c))
    assert sorted_bucket == sorted(c)
    
    t = a.copy()
    qsort(t, 0, len(a)-1)
    assert t == [1, 2, 5, 8, 9]  
def test_stack():
    stack = Stack()
    
    stack.push(10)
    stack.push(20)
    stack.push(5)
    stack.push(15)
    
    assert stack.size_() == 4
    assert stack.top() == 15
    assert stack.mini() == 5
    
    popped = stack.pop()
    assert popped == 15
    assert stack.size_() == 3
    assert stack.mini() == 5
    
    empty_stack = Stack()
    assert empty_stack.pop() is None
    assert empty_stack.top() is None

def test_queue():
    queue = Queue()
    
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    
    assert queue.size_() == 4
    assert queue.front() == 1
    
    dequeued = queue.dequeue()
    assert dequeued == 1
    assert queue.size_() == 3
    assert queue.front() == 2
    
    empty_queue = Queue()
    assert empty_queue.dequeue() is None
    assert empty_queue.front() is None