def descending_order(num):
    # convert to string
    new_str = str(num)
    ordered_num = ""

    # store each number in a list
    # self emptying list
    unordered_list = []

    # Iterate through string and store each number as an integer
    for num in new_str:
        unordered_list.append(int(num))

    # Iterate through according to how many numbers there are
    while len(unordered_list) > 0:  # exit when the list is empty
        largest_num = max(unordered_list)  # get largest num in list
        ordered_num += str(largest_num)  # add num to string
        unordered_list.remove(largest_num)  # remove from list

    # Returning number in descending order as an integer
    return int(ordered_num)