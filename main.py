from utils.algorithms import algorithms
from utils.tests import test_generator, test_handler
from utils.tests.test_generator import TestConfig
from utils.algorithms.algorithms import Complexity


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
        "Quick sort algorithm", Complexity.N_LOG2_N, True)

    target_test = tests[0]
    sorted_arr = quicksort.sort(array=target_test.array,
                                array_size=target_test.length,
                                max_value=target_test.max_value)

    test_handler.verify_test(
        sorted_arr, target_test.length, target_test.max_value)


if __name__ == "__main__":
    main()
