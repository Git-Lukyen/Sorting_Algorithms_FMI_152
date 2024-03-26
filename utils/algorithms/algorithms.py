from abc import abstractmethod
from typing import List
from enum import Enum
import random


class Complexity(Enum):
    N_SQUARED = 1
    N_LOG2_N = 2
    N_PLUS_MAX = 3


# Am adaugat max_val si max_size ca atribute pt clasa abstracta
# Am adaugat metoda verifWithinLimits
class SortingAlgorithm:
    def __init__(self, name: str = None, complexity: str = None, in_place: bool = False, max_val: int = 0, max_size: int = 0):
        self.name = name
        self.complexity = complexity
        self.in_place = in_place
        self.max_val = max_val
        self.max_size = max_size

    @abstractmethod
    def sort(self, array: List[int], array_size: int, max_value: int, reverse: bool = False):
        ...

    def verifWithinLimits(self, val: int, size: int):
        if val > self.max_val:
            print("Max value limit exceeded, couldn't sort")
            return False
        if size > self.max_size:
            print("Array size limit exceeded, couldn't sort")
            return False

        return True


class DefaultSort(SortingAlgorithm):
    def sort(self, array: List[int], array_size: int, max_value: int, reverse: bool = False):
        return sorted(array, reverse=reverse)


class CountingSort(SortingAlgorithm):
    def sort(self, array: List[int], array_size: int, max_value: int, reverse: bool = False):
        ...


# Implementez propriul counting_sort pt radix pt ca e diferit de cel normal
class RadixSort(SortingAlgorithm):
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
            output[count[index % 10] - 1] = array[i]
            count[index % 10] -= 1
            i -= 1

        return output

    def sort(self, array: List[int], array_size: int, max_value: int, base: int = 10, reverse: bool = False):
        if self.verifWithinLimits(array_size, max_value) and CountingSort.verifWithinLimits(array_size, base - 1):
            exp = 1
            # Sorting by each digit with counting sort
            while max_value // exp:
                array = self.__countingSort(self, array, array_size, base, exp)

                exp *= base

            if reverse:
                return array[::-1]

            return array
        else:
            return None


class shellSort(SortingAlgorithm):
    def sort(self, array: List[int], array_size: int, max_value: int, reverse: bool = False):
        if self.verifWithinLimits(array_size, max_value):
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


class QuickSort(SortingAlgorithm):
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
        self.__quicksort(array, 0, array_size - 1)
        if reverse:
            array = array[::-1]
        return array


class HeapSort(SortingAlgorithm):
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
        self.__heapsort(array, array_size)
        if reverse:
            array = array[::-1]
        return array
