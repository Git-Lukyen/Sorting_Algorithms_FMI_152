from utils.algorithms import algorithms
from utils.tests import test_generator, test_handler
from utils.tests.test_generator import TestConfig
from utils.algorithms.algorithms import Complexity
import sys
import time


def main():
    # Example generating tests
    test_generator.generate_test("verification_test", [
        TestConfig(100, 100_000),
        TestConfig(10_000, 100_000),
        TestConfig(100_000, 100_000)])

    test_generator.generate_test("easy_verification_test", [
        TestConfig(10, 100),
        TestConfig(100, 1000)])

    # Example reading tests
    tests = test_handler.read_file(
        "tests/random_generated/easy_verification_test")

    # Example using a sort algo
    default_algo = algorithms.DefaultSort(
        "Python Default Sort", Complexity.N_LOG2_N, True)

    target_test = tests[0]
    sorted_arr = default_algo.sort(array=target_test.array,
                                   array_size=target_test.length,
                                   max_value=target_test.max_value)

    test_handler.verify_test(
        sorted_arr, target_test.length, target_test.max_value)

    # Quicksort test
    quicksort = algorithms.QuickSort(
        "Quick sort algorithm", Complexity.N_LOG2_N, False, sys.maxsize, 30_000_000)

    target_test = tests[0]
    sorted_arr = quicksort.sort(array=target_test.array,
                                array_size=target_test.length,
                                max_value=target_test.max_value)

    test_handler.verify_test(
        sorted_arr, target_test.length, target_test.max_value)

    # Heapsort test
    heapsort = algorithms.HeapSort(
        "Heap sort algorithm", Complexity.N_LOG2_N, True, sys.maxsize, 30_000_000)

    target_test = tests[0]
    sorted_arr = heapsort.sort(array=target_test.array,
                               array_size=target_test.length,
                               max_value=target_test.max_value)

    test_handler.verify_test(
        sorted_arr, target_test.length, target_test.max_value)
    
    test_generator.generate_test("radix_verification_test", [
        TestConfig(10, 100),
        TestConfig(100, 1000),
        TestConfig(1_000, 1_000),
        TestConfig(1_000, 1_000_000_000_000),
        TestConfig(1_000, 1_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000),
        TestConfig(10_000, 10_000),
        TestConfig(10_000, 1_000_000),
        TestConfig(10_000, 1_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000),
        TestConfig(100_000, 100_000),
        TestConfig(100_000, 1_000_000_000),
        TestConfig(100_000, 1_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000),
        TestConfig(1_000_000, 1000),
        TestConfig(1_000_000, 100_000),
        TestConfig(1_000_000, 1_000_000),
        TestConfig(1_000_000, 1_000_000_000),
        #TestConfig(1_000_000, 1_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000)
        ])

    #RadixSort test
    r_tests = test_handler.read_file("tests/random_generated/radix_verification_test")
    
    radix_algo = algorithms.RadixSort("Radix", Complexity.N_PLUS_MAX, False, 1_000_000, 1_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000)
    print("Radix tests:")
    for target_test in r_tests:
        start = time.time()
        sorted_arr = radix_algo.sort(array=target_test.array,
                                        array_size=target_test.length,
                                        max_value=target_test.max_value)
        try:
            test_handler.verify_test(sorted_arr, target_test.length, target_test.max_value)
            print("passed", time.time() - start)
        except:
            print("Not passed")
    
    #ShellSort test
    s_tests = test_handler.read_file("tests/random_generated/verification_test")
    
    shell_algo = algorithms.ShellSort("ShellSort", Complexity.N_LOG2_N, True, 1_000_000, 1_000_000)
    print("ShelSort tests:")
    for target_test in s_tests:
        start = time.time()
        sorted_arr = shell_algo.sort(array=target_test.array,
                                        array_size=target_test.length,
                                        max_value=target_test.max_value)
        try:
            test_handler.verify_test(sorted_arr, target_test.length, target_test.max_value)
            print("passed", time.time() - start)
        except:
            print("Not passed")
            


if __name__ == "__main__":
    main()
