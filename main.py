from utils.algorithms import algorithms
from utils.tests import test_generator, test_handler
from utils.tests.test_generator import TestConfig
from utils.algorithms.algorithms import Complexity


# TO DO:Add bounds for python sort
def benchmark(alg: algorithms.SortingAlgorithm, filePath: str):
    tests = test_handler.read_file(filePath)

    print("\n", str(alg.__class__).split(".")[-1][:-2], "tests: ")
    for test in tests:
        try:
            sorted_arr, duration = alg.sortTimed(array=test.array,
                                                 array_size=test.length,
                                                 max_value=test.max_value)

            test_handler.verify_test(sorted_arr, test.length, test.max_value)
            print("Passed:", duration, "s")
        except AssertionError as error:
            print(f"Failed: {str(error)}")


def main():
    test_generator.generate_test("default/big_arr", [
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

    test_generator.generate_test("quick/mix_array_val", [
        TestConfig(1_000, 1_000_000_000_000_000_000_000),
        TestConfig(1_000, 1_000_000_000_000_000_000_000_000),
        TestConfig(1_000, 1_000_000_000_000_000_000_000_000_000),
        TestConfig(10_000, 1_000_000_000_000_000_000_000),
        TestConfig(10_000, 1_000_000_000_000_000_000_000_000),
        TestConfig(10_000, 1_000_000_000_000_000_000_000_000_000),
        TestConfig(100_000, 1_000_000_000_000_000_000_000),
        TestConfig(100_000, 1_000_000_000_000_000_000_000_000),
        TestConfig(100_000, 1_000_000_000_000_000_000_000_000_000),
        TestConfig(100_000, 1_000_000_000_000_000_000_000_000_000_000),
        TestConfig(200_000, 1_000_000_000_000_000_000_000_000_000_000),
        TestConfig(300_000, 1_000_000_000_000_000_000_000_000_000_000),
    ])

    test_generator.generate_test("heap/mix_array_val", [
        TestConfig(1_000, 1_000_000_000_000_000_000_000),
        TestConfig(1_000, 1_000_000_000_000_000_000_000_000),
        TestConfig(1_000, 1_000_000_000_000_000_000_000_000_000),
        TestConfig(10_000, 1_000_000_000_000_000_000_000),
        TestConfig(10_000, 1_000_000_000_000_000_000_000_000),
        TestConfig(10_000, 1_000_000_000_000_000_000_000_000_000),
        TestConfig(100_000, 1_000_000_000_000_000_000_000),
        TestConfig(100_000, 1_000_000_000_000_000_000_000_000),
        TestConfig(100_000, 1_000_000_000_000_000_000_000_000_000),
        TestConfig(100_000, 1_000_000_000_000_000_000_000_000_000_000),
        TestConfig(200_000, 1_000_000_000_000_000_000_000_000_000_000)
    ])

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
        TestConfig(500_000, 1_000_000_000_000),
        TestConfig(1_000_000, 1_000_000),
        TestConfig(
            2_000_000, 1_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000)
    ])

    test_generator.generate_test("shell/big_arr", [
        TestConfig(100_000, 1_000_000_000_000_000_000_000),
        TestConfig(150_000, 1_000_000_000_000_000_000_000),
        TestConfig(200_000, 1_000_000_000_000_000_000_000),
        TestConfig(300_000, 1_000_000_000_000_000_000_000),
        TestConfig(
            100_000, 1_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000),
        TestConfig(
            150_000, 1_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000),
        TestConfig(
            200_000, 1_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000),
        TestConfig(
            300_000, 1_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000),
        TestConfig(500_000, 1_000_000_000_000),
        TestConfig(
            500_000, 1_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000)
    ])

    test_generator.generate_test("counting/big_arr", [
        TestConfig(100, 1_000),
        TestConfig(100_000, 1_000),
        TestConfig(120_000, 1_000),
        TestConfig(200_000, 1_000),
        TestConfig(100_000, 100_000),
        TestConfig(300_000, 1_000_000),
        TestConfig(500_000, 1_000_000),
        TestConfig(1_000_000, 5_000_000),
        TestConfig(10_000_000, 10_000_000),
    ])

    test_generator.generate_test("merge/big_arr", [
        TestConfig(100, 1_000),
        TestConfig(100_000, 1_000),
        TestConfig(120_000, 1_000),
        TestConfig(200_000, 1_000),
        TestConfig(100_000, 100_000),
        TestConfig(300_000, 1_000_000)
    ])

    # Tests paths
    test_path_default = "tests/random_generated/default/big_arr"
    test_path_quick = "tests/random_generated/quick/mix_array_val"
    test_path_heap = "tests/random_generated/heap/mix_array_val"
    test_path_radix_bnum = "tests/random_generated/radix/big_num"
    test_path_radix_barr = "tests/random_generated/radix/big_arr"
    test_path_shell = "tests/random_generated/shell/big_arr"
    test_path_counting_barr = "tests/random_generated/counting/big_arr"
    test_path_merge_barr = "tests/random_generated/merge/big_arr"

    # Python sort
    default_algo = algorithms.DefaultSort(Complexity.N_LOG2_N, True)
    benchmark(default_algo, test_path_default)

    # Quicksort test
    quicksort = algorithms.QuickSort(Complexity.N_LOG2_N, False)
    benchmark(quicksort, test_path_quick)

    # Heapsort test
    heapsort = algorithms.HeapSort(Complexity.N_LOG2_N, False)
    benchmark(heapsort, test_path_heap)

    # Radix test

    # Base 10
    radix_algb10 = algorithms.RadixSort(Complexity.N_PLUS_MAX, False, 10)
    benchmark(radix_algb10, test_path_radix_bnum)
    benchmark(radix_algb10, test_path_radix_barr)

    # Base 2^16
    radix_algb2_16 = algorithms.RadixSort(
        Complexity.N_PLUS_MAX, False, 1 << 16)
    benchmark(radix_algb2_16, test_path_radix_bnum)
    benchmark(radix_algb2_16, test_path_radix_barr)

    # Shell test
    shell_alg = algorithms.ShellSort(Complexity.N_LOG2_N, True)
    benchmark(shell_alg, test_path_shell)

    # Counting test
    count_alg = algorithms.CountingSort(Complexity.N_PLUS_MAX, False)
    benchmark(count_alg, test_path_counting_barr)

    # Merge test
    merge_alg = algorithms.MergeSort(Complexity.N_LOG2_N, False)
    benchmark(merge_alg, test_path_merge_barr)


if __name__ == "__main__":
    main()
