import time


'''
    Реализация на основе массива
    Минусы: 
        - ограничен по размеру
        - для n вызовов время выполнения O(n)
    Плюсы:
        - простота реализации
'''
class fifo_v1():
    def __init__(self, max_size: int):
        self._max_size: int = max_size
        self._buffer: list = [None] * self._max_size
        self._tail: int = 0
        self._head: int = -1
        self._size: int = 0
    
    def put(self, value) -> None:
        if self._size == self._max_size:
            raise Exception('Переполнение')
        self._buffer[self._tail] = value
        self._tail = (self._tail + 1) % self._max_size
        self._size += 1        

    def pop(self):
        if self._size == 0:
            raise Exception('Нет элементов')
        self._head = (self._head + 1) % self._max_size     
        value = self._buffer[self._head]
        self._buffer[self._head] = None
        self._size -= 1
        return value

'''
Реализация на основе связанного списка
    Минусы:         
        - для n вызовов время выполнения O(n)
        - дополнительные траты по памяти для указаталей    
'''
class fifo_v2():
    def __init__(self):
        self._first = None
        self._last = None
        self._size = 0

    def put(self, value) -> None:
        if self._size == 0:
            self._first = self.Node(value)
            self._last = self._first
        else:
            self._last.next = self.Node(value)
            self._last = self._last.next
        self._size += 1

    def pop(self):
        if self._size == 0:
            raise Exception('Нет элементов')
        value = self._first.value
        self._first = self._first.next
        self._size -= 1
        return value

    class Node:
        def __init__(self, value=None, next=None):
            self.value = value
            self.next = next

def test():
    print("Тест очереди на основе массива")
    start_time = time.time()
    v1 = fifo_v1(100000)
    for i in range(100000):
        v1.put(i)
        v1.pop()
        v1.put(i)
    print(f"Затраченное время: {time.time() - start_time}")    

    print("Тест очереди на связанного списка")
    start_time = time.time()
    v2 = fifo_v2()
    for i in range(100000):
        v2.put(i)
        v2.pop()
        v2.put(i)
    print(f"Затраченное время: {time.time() - start_time}")    

if __name__=='__main__':
    test()