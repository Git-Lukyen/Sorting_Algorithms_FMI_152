from abc import abstractmethod, ABC
from typing import List


class SortingAlgorithm:
    def __init__(self, name: str = None, complexity: str = None, in_place: bool = False):
        self.name = name
        self.complexity = complexity
        self.in_place = in_place

    @abstractmethod
    def sort(self, array: List[int], array_size: int, max_value: int, reverse: bool = False):
        ...


class DefaultSort(SortingAlgorithm):
    def sort(self, array: List[int], array_size: int, max_value: int, reverse: bool = False):
        return sorted(array, reverse=reverse)
