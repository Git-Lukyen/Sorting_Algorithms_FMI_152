from utils.algorithms import algorithms
from utils.tests import test_generator, test_handler
from utils.tests.test_generator import TestConfig
from utils.algorithms.algorithms import Complexity
import sys
from time import time, sleep
import multiprocessing

def main():
    # Example generating tests
    test_generator.generate_test("verification_test", [
        TestConfig(100, 100_000),
        TestConfig(10_000, 100_000),
        TestConfig(100_000, 100_000)])

    test_generator.generate_test("easy_verification_test", [
        TestConfig(10, 100),
        TestConfig(100, 1000)])
    
    test_generator.generate_test("radix_verification_test", [
        # TestConfig(10, 100),
        # TestConfig(100, 1000),
        # TestConfig(1_000, 1_000),
        # TestConfig(1_000, 1_000_000_000_000),
        TestConfig(1_000, 1_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000),
        # TestConfig(10_000, 10_000),
        # TestConfig(10_000, 1_000_000),
        TestConfig(10_000, 1_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000),
        # TestConfig(100_000, 100_000),
        TestConfig(100_000, 1_000_000_000),
        TestConfig(200_000, 1_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000),
        # TestConfig(500_000, 1_000_000_000),
        # TestConfig(1_000_000, 1_000),
        TestConfig(1_000_000, 1_000_000),
        TestConfig(1_000_000, 1_000_000_000),
        #TestConfig(10_000_000, 10_000),
        #TestConfig(10_000_000, 1_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000)
        ])


    test_path = "tests/random_generated/verification_test"

    # Python sort
    default_algo = algorithms.DefaultSort(
        "Python Default Sort", Complexity.N_LOG2_N, True)
    benchmark(default_algo, test_path)

    #Quicksort test
    quicksort = algorithms.QuickSort(
        "Quick sort algorithm", Complexity.N_LOG2_N, False, sys.maxsize, 30_000_000)
    benchmark(quicksort, test_path)

   
    #Heapsort test
    heapsort = algorithms.HeapSort(
        "Heap sort algorithm", Complexity.N_LOG2_N, True, sys.maxsize, 30_000_000)
    benchmark(heapsort, test_path)

    #Radix test(Max value incorrectly set)
    test_path = "tests/random_generated/radix_verification_test"

    radix_alg = algorithms.RadixSort("Radix", Complexity.N_PLUS_MAX, False, 10, 1_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000, 1_000_000)
    benchmark(radix_alg, test_path)

    #Shell test(Max val can be anything really)
    shell_alg = algorithms.ShellSort("ShellSort", Complexity.N_LOG2_N, False, 1_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000, 200_00)
    benchmark(shell_alg, test_path)


if __name__ == "__main__":
    main()



def benchmark(alg : algorithms.SortingAlgorithm, filePath : str):
    tests = test_handler.read_file(filePath)

    print(alg.name, "tests: ")
    for test in tests:
        sorted_arr, duration = alg.sortTimed(array = test.array, 
                                             array_size=test.length, 
                                             max_value=test.max_value)
        try:
            test_handler.verify_test(sorted_arr, test.length, test.max_value)
            print("Passed:", duration, "s")
        except AssertionError:
            print("Failed")