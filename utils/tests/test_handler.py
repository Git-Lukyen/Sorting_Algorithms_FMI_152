from typing import List


class TestUnit:
    def __init__(self, index: int, array: List[int], length: int, max_value: int):
        self.index = index
        self.array = array
        self.length = length
        self.max_value = max_value


def read_file(path):
    final_tests: List[TestUnit] = []

    with open(path, "r") as input_file:
        nr_of_tests = int(input_file.readline())

        for test_index in range(nr_of_tests):
            array_length, max_value = [int(num) for num in input_file.readline().split()]
            array = [int(num) for num in input_file.readline().split()]

            final_tests.append(TestUnit(test_index + 1, array, array_length, max_value))

    return final_tests


def verify_test(array: List[int], length: int, max_value: int, reverse: bool = False):
    assert __array_sorted__(array, reverse) == True
    assert len(array) == length
    assert max_value >= max(array)


def __array_sorted__(array: List[int], reverse: bool = False):
    is_sorted = True

    if not reverse:
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                is_sorted = False
    else:
        for i in range(len(array) - 1):
            if array[i] < array[i + 1]:
                is_sorted = False

    return is_sorted
