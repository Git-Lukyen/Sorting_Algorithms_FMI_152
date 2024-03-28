from utils.algorithms import algorithms
from utils.tests import test_generator, test_handler
from utils.tests.test_generator import TestConfig
from utils.algorithms.algorithms import Complexity
import sys

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

def main():
    # Example generating tests
    test_generator.generate_test("verification_test", [
        TestConfig(100, 100_000),
        TestConfig(10_000, 100_000),
        TestConfig(100_000, 100_000)])

    test_generator.generate_test("easy_verification_test", [
        TestConfig(10, 100),
        TestConfig(100, 1000)])
    
    test_generator.generate_test("radix/big_num", [
        TestConfig(1_000, 1_000_000_000_000_000_000_000),
        TestConfig(1_000, 1_000_000_000_000_000_000_000_000),
        TestConfig(1_000, 1_000_000_000_000_000_000_000_000_000),
        TestConfig(10_000, 1_000_000_000_000_000_000_000),
        TestConfig(10_000, 1_000_000_000_000_000_000_000_000),
        TestConfig(10_000, 1_000_000_000_000_000_000_000_000_000),
        TestConfig(100_000, 1_000_000_000_000_000_000_000),
        TestConfig(100_000, 1_000_000_000_000_000_000_000_000),
        TestConfig(100_000, 1_000_000_000_000_000_000_000_000_000),
        TestConfig(100_000, 1_000_000_000_000_000_000_000_000_000_000)
        ])
    
    test_generator.generate_test("radix/big_arr", [
        TestConfig(100_000, 1_000),
        TestConfig(120_000, 1_000),
        TestConfig(200_000, 1_000),
        TestConfig(100_000, 1_000_000),
        TestConfig(120_000, 1_000_000),
        TestConfig(200_000, 1_000_000),
        TestConfig(100_000, 1_000_000_000_000),
        TestConfig(120_000, 1_000_000_000_000),
        TestConfig(200_000, 1_000_000_000_000),
        TestConfig(100_000, 1_000_000_000_000_000_000_000),
        TestConfig(120_000, 1_000_000_000_000_000_000_000),
        TestConfig(200_000, 1_000_000_000_000_000_000_000),
        TestConfig(300_000, 1_000_000),
        TestConfig(300_000, 1_000_000_000_000),
        TestConfig(300_000, 1_000_000_000_000_000_000_000),
        TestConfig(500_000, 1_000_000_000_000)
        ])

    test_generator.generate_test("shell/big_arr", [
        TestConfig(100_000, 1_000_000_000_000_000_000_000),
        TestConfig(150_000, 1_000_000_000_000_000_000_000),
        TestConfig(200_000, 1_000_000_000_000_000_000_000),
        TestConfig(300_000, 1_000_000_000_000_000_000_000),
        TestConfig(100_000, 1_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000),
        TestConfig(150_000, 1_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000),
        TestConfig(200_000, 1_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000),
        TestConfig(300_000, 1_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000),
        TestConfig(500_000, 1_000_000_000_000),
        TestConfig(500_000, 1_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000)
        ])
    
    #Radix test
    test_path_radix_bnum = "tests/random_generated/radix/big_num"
    test_path_radix_barr = "tests/random_generated/radix/big_arr"
    test_path_shell = "tests/random_generated/shell/big_arr"

    #Default test
    test_path_ver = "tests/random_generated/verification_test"

    # Python sort
    default_algo = algorithms.DefaultSort(
        "Python Default Sort", Complexity.N_LOG2_N, True)
    
    benchmark(default_algo, test_path_ver)

    #Quicksort test
    quicksort = algorithms.QuickSort(
        "Quick sort algorithm", Complexity.N_LOG2_N, False, sys.maxsize, 1_000_000)
    
    benchmark(quicksort, test_path_ver)

    #Heapsort test
    heapsort = algorithms.HeapSort(
        "Heap sort algorithm", Complexity.N_LOG2_N, False, sys.maxsize, 1_000_000)
    
    benchmark(heapsort, test_path_ver)

    #Base 10
    radix_algb10 = algorithms.RadixSort("Radix", Complexity.N_PLUS_MAX, False, 10, 1_000_000_000_000_000_000_000, 120_000)

    benchmark(radix_algb10, test_path_radix_bnum)
    benchmark(radix_algb10, test_path_radix_barr)

    #Base 2^16
    radix_algb2_16 = algorithms.RadixSort("Radix", Complexity.N_PLUS_MAX, False, 1 << 16, 1_000_000_000_000_000_000_000_000_000, 300_000)

    benchmark(radix_algb2_16, test_path_radix_bnum)
    benchmark(radix_algb2_16, test_path_radix_barr)

    #Shell test
    shell_alg = algorithms.ShellSort("ShellSort", Complexity.N_LOG2_N, True, 1_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000, 200_000)

    benchmark(shell_alg, test_path_shell)


if __name__ == "__main__":
    main()

