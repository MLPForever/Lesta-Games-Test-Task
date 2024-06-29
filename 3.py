'''
    Стабильно хорошим является сортировка слиянием O(n\log n).
    В некоторых случаях будут эффективны другие алгоритмы, которые смогут улучшить время до O(n).    
'''


import time

def merge(array: list) -> list:
    length = len(array)
    if length == 1:
        return array
    left = array[:(length // 2)]
    right = array[(length // 2):]
    left = merge(left)
    right = merge(right)
    i = 0
    j = 0
    newArray = []
    while i != len(left) and j != len(right):
        if left[i] < right[j]:
            newArray.append(left[i])
            i += 1
        else:
            newArray.append(right[j])
            j += 1
    while i != len(left):
        newArray.append(left[i])
        i += 1
    while j != len(right):
        newArray.append(right[j])
        j += 1
    return newArray


def test():    
    start_time = time.time()
    merge([1, 2, 3, 4] * 100)
    print(f"Затраченное время: {time.time() - start_time}")    

    start_time = time.time()
    merge([4, 3, 2, 1] * 100)
    print(f"Затраченное время: {time.time() - start_time}")

    start_time = time.time()
    merge([i for i in range(100000, 0, -1)])
    print(f"Затраченное время: {time.time() - start_time}")


if __name__ == '__main__':
    test()