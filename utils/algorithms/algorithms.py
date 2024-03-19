from abc import abstractmethod
from typing import List

#Am adaugat max_val si max_size ca atribute pt clasa abstracta
#Am adaugat metoda verifWithinLimits
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
        elif size > self.max_size:
            print("Array size limit exceeded, couldn't sort")
            return False

        return True



class DefaultSort(SortingAlgorithm):
    def sort(self, array: List[int], array_size: int, max_value: int, reverse: bool = False):
        return sorted(array, reverse=reverse)

class CountingSort(SortingAlgorithm):
    def sort(self, array: List[int], array_size: int, max_value: int, reverse: bool = False):
        ...

#Implementez propriul counting_sort pt radix pt ca e diferit de cel normal
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
            #Sorting by each digit with counting sort
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






