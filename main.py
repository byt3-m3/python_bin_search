from ipcalc import IP, Network
import timeit

__author__ = "Courtney S Baxter Jr."


# Helper function used to determine func execution time
def _get_time():
    return timeit.default_timer()


def bin_search(arr, target_val):
    start = _get_time()
    # TODO: Edge case to test if empty list is being provided
    if not arr or len(arr) == 0:
        return False

    # TODO: Creates the Lower and Upper bound index variables
    lower_index = 0
    upper_index = len(arr) - 1

    print("target:", target_val)

    # TODO: Begins the indexing process
    while lower_index <= upper_index:

        mid_index = (lower_index + upper_index) // 2  # Calculates the mid-point index
        print("\nLower:", lower_index, "Upper:", upper_index)
        print("mid-index:", mid_index)

        mid_val = arr[mid_index]  # Retrieves the mid-point value using the mid-point index.
        print("mid-value:", mid_val)

        # TODO: Test if mid-point value is equal to the target value
        if mid_val == target_val:
            end = _get_time()
            return True, end - start, len(arr)
        else:
            # TODO: Test if the mid-point value is less than the target value
            if mid_val < target_val:
                lower_index = mid_index + 1  # Shift Right
                print("new-lower-index:", lower_index)
            else:
                upper_index = mid_index - 1  # Shift Left
                print("new-upper-index:", upper_index)

    # TODO: Return if no target value is found
    end = _get_time()
    return False, end - start


def lin_search(array, target_val):
    start = _get_time()
    for num, i in enumerate(array):
        print("searching index:", num, i)
        if i == target_val:
            end = _get_time()
            return True, end - start, len(array)
    end = _get_time()
    return False, end - start


def test_int(method, _int):
    new_list = [i + 3 for i in range(10000000)]

    if method == "bin":
        return bin_search(new_list, _int)
    else:
        return lin_search(new_list, _int)


def test_demo(method, num):
    test_list = [6, 7, 45, 100, 154, 200]

    if method == "bin":
        return bin_search(test_list, num)
    else:
        return lin_search(test_list, num)


def test_ip(method, ip):
    my_ip = IP(ip)
    network = Network("10.0.0.0/12")
    net_list = list(network)

    if method == "bin":
        return bin_search(net_list, my_ip)
    else:
        return lin_search(net_list, my_ip)


def main():
    # TODO: Uncomment the print statements below to execute and print the function return values
    print(test_ip("lin", "10.1.140.2")) # Test the Linear IP search
    # print(test_ip("bin", "10.1.140.2")) # Test the Binary IP search
    #
    # print(test_int("lin", 66656)) # Test the Linear Integer search
    # print(test_int("bin", 66656)) # Test the Binary Integer search

    # print(test_demo("lin", 100)) # Test the demo Linear search illustrated in the README
    # print(test_demo("bin", 100)) # Test the demo Binary search illustrated in the README


if __name__ == "__main__":
    main()
