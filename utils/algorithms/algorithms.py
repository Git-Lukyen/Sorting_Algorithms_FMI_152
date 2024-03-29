from abc import abstractmethod
from typing import List
from enum import Enum
import random
from time import time


class Complexity(Enum):
    N_SQUARED = 1
    N_LOG2_N = 2
    N_PLUS_MAX = 3


def timer(func):
    def wrapper(*args, **kwargs):
        start = time()
        sorted_arr = func(*args, **kwargs)
        end = time()

        return (sorted_arr, round(end - start, 2))

    return wrapper


class SortingAlgorithm:
    max_val: int
    max_size: int

    def __init__(self, complexity: Complexity, in_place: bool = False):
        self.complexity = complexity
        self.in_place = in_place

    @abstractmethod
    def sort(self, array: List[int], array_size: int, max_value: int, reverse: bool = False):
        ...

    # decorated method that tracks time passed for all sorts
    @timer
    def sortTimed(self, array: List[int], array_size: int, max_value: int, reverse: bool = False):
        return self.sort(array, array_size, max_value, reverse)

    def verifyWithinLimits(self, val: int, size: int):
        if val > self.max_val or size > self.max_size:
            return False

        return True


class DefaultSort(SortingAlgorithm):
    max_val, max_size = 1_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000, 2_000_000

    def sort(self, array: List[int], array_size: int, max_value: int, reverse: bool = False):
        if self.verifyWithinLimits(max_value, array_size):
            return sorted(array, reverse=reverse)
        else:
            assert False, "Can't sort array"


class CountingSort(SortingAlgorithm):
    max_val, max_size = 10_000_000, 10_000_000

    def sort(self, array: List[int], array_size: int, max_value: int, reverse: bool = False):
        if not self.verifyWithinLimits(max_value, array_size):
            assert False, "Can't sort array"

        frequency = [0] * (max_value + 1)
        for value in array:
            frequency[value] += 1

        sorted_array = []
        for num in range(max_value + 1):
            if frequency[num] > 0:
                sorted_array.extend([num] * frequency[num])

        return sorted_array if not reverse else sorted_array[::-1]


class MergeSort(SortingAlgorithm):
    max_val, max_size = 1_000_000_000_000_000_000, 300_000

    def _merge(self, left_array, right_array):
        left_len, right_len = len(left_array), len(right_array)
        left_curr, right_curr = 0, 0

        merged_array = []
        while left_curr < left_len and right_curr < right_len:
            if left_array[left_curr] <= right_array[right_curr]:
                merged_array.append(left_array[left_curr])
                left_curr += 1
            else:
                merged_array.append(right_array[right_curr])
                right_curr += 1

        if left_curr < left_len:
            merged_array.extend(left_array[left_curr:])
        else:
            merged_array.extend(right_array[right_curr:])

        return merged_array

    def _merge_sort(self, array, left_index, right_index):
        if left_index < right_index:
            mid = (left_index + right_index) // 2

            left_of_mid = self._merge_sort(array, left_index, mid)
            right_of_mid = self._merge_sort(array, mid + 1, right_index)
            return self._merge(left_of_mid, right_of_mid)
        else:
            return [array[left_index]]

    def sort(self, array: List[int], array_size: int, max_value: int, reverse: bool = False):
        if not self.verifyWithinLimits(max_value, array_size):
            assert False, "Can't sort array"

        sorted_array = self._merge_sort(array, 0, len(array) - 1)

        return sorted_array if not reverse else sorted_array[::-1]


# Maxim baza 2^16
class RadixSort(SortingAlgorithm):
    max_val, max_size = 1_000_000_000_000_000_000_000, 120_000

    def __init__(self, complexity: Complexity = None, in_place: bool = False, base: int = 10):
        SortingAlgorithm.__init__(self, complexity, in_place)
        self.base = base

    def __countingSort(self, array: List[int], array_size: int, base: int, exp: int):
        output = [0] * array_size
        count = [0] * base

        # Calculate count of elements
        for i in range(0, array_size):
            index = array[i] // exp
            count[index % base] += 1

        # Calculate cumulative count
        for i in range(1, base):
            count[i] += count[i - 1]

        # Place the elements in sorted order
        i = array_size - 1
        while i >= 0:
            index = array[i] // exp
            output[count[index % base] - 1] = array[i]
            count[index % base] -= 1
            i -= 1

        return output

    def sort(self, array: List[int], array_size: int, max_value: int, reverse: bool = False):
        if self.verifyWithinLimits(max_value, array_size) and self.base <= 1 << 16:
            exp = 1
            # Sorting by each digit with counting sort
            while max_value // exp:
                array = self.__countingSort(array, array_size, self.base, exp)

                exp *= self.base

            if reverse:
                return array[::-1]

            return array
        else:
            assert False, "Can't sort array"


class ShellSort(SortingAlgorithm):
    max_val, max_size = 1_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000, 200_000

    def sort(self, array: List[int], array_size: int, max_value: int, reverse: bool = False):
        if self.verifyWithinLimits(max_value, array_size):
            gap = array_size // 2

            while gap > 0:
                for i in range(gap, array_size):
                    temp = array[i]
                    j = i
                    while j >= gap and array[j - gap] > temp:
                        array[j] = array[j - gap]
                        j -= gap

                    array[j] = temp

                gap //= 2

            if reverse:
                return array[::-1]

            return array
        else:
            assert False, "Can't sort array"


class QuickSort(SortingAlgorithm):
    max_val, max_size = 1_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000, 300_000

    def __quicksort(self, array: List[int], left_idx: int, right_idx: int):
        if left_idx < right_idx:
            pivot_idx = self.__random_partition(array, left_idx, right_idx)
            self.__quicksort(array, left_idx, pivot_idx - 1)
            self.__quicksort(array, pivot_idx + 1, right_idx)

    def __random_partition(self, array: List[int], left_idx: int, right_idx: int):
        pivot_idx = random.randint(left_idx, right_idx)

        # Change the first element with the pivot
        # this works since in __partition we will take
        # the first element as the pivot (witch will be random thanks to this)
        array[left_idx], array[pivot_idx] = array[pivot_idx], array[left_idx]
        return self.__partition(array, left_idx, right_idx)

    def __partition(self, array: List[int], left_idx: int, right_idx: int):
        pivot_idx = left_idx
        pivot_val = array[pivot_idx]
        left_margin = left_idx + 1

        for curr_idx in range(left_idx + 1, right_idx + 1):
            if array[curr_idx] <= pivot_val:
                array[curr_idx], array[left_margin] = array[left_margin], array[curr_idx]
                left_margin += 1

        (array[pivot_idx], array[left_margin - 1]) = (
            array[left_margin - 1], array[pivot_idx])

        pivot_idx = left_margin - 1
        return pivot_idx

    def sort(self, array: List[int], array_size: int, max_value: int, reverse: bool = False):
        if self.verifyWithinLimits(max_value, array_size):
            self.__quicksort(array, 0, array_size - 1)
        else:
            assert False, "Can't sort array"
        if reverse:
            array = array[::-1]
        return array


class HeapSort(SortingAlgorithm):
    max_val, max_size = 1_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000, 200_000

    def __heapsort(self, array: List[int], array_size: int):
        self.__build_maxheap(array, array_size)
        for idx in range(array_size - 1, 0, -1):
            array[idx], array[0] = array[0], array[idx]
            self.__heapify(array, idx, 0)

    def __heapify(self, array: List[int], array_size: int, root: int):
        left_node = 2 * root + 1
        right_node = 2 * root + 2

        max_node = root

        # cheks if the left child larger than the root
        if left_node < array_size and array[left_node] > array[max_node]:
            max_node = left_node

        # cheks if the right child larger than the root
        if right_node < array_size and array[right_node] > array[max_node]:
            max_node = right_node

        if max_node != root:
            array[max_node], array[root] = array[root], array[max_node]

            # continue to heapify the rest of the tree
            self.__heapify(array, array_size, max_node)

    def __build_maxheap(self, array: List[int], array_size: int):
        for idx in range(array_size // 2 - 1, -1, -1):
            self.__heapify(array, array_size, idx)

    def sort(self, array: List[int], array_size: int, max_value: int, reverse: bool = False):
        if self.verifyWithinLimits(max_value, array_size):
            self.__heapsort(array, array_size)
        else:
            assert False, "Can't sort array"
        if reverse:
            array = array[::-1]
        return array
