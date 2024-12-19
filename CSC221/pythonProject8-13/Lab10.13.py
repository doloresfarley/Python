'''
LAB ACTIVITY
10.13.1: LAB: Reverse list


0 / 10

Complete the reverse_list() function that returns a new integer list containing all contents in the list parameter but in reverse order.

Ex: If the elements of the input list are:

[2, 4, 6]
the returned array will be:

[6, 4, 2]
Note: Use a for loop. DO NOT use reverse() or reversed().

'''


def reverse_list(li):
    if len(li) == 0:
        return []
    copy_list = li[:]
    for num, i in enumerate(li):
        copy_list[len(copy_list) - 1 - num] = i
    return copy_list

    # Type your code here.


if __name__ == '__main__':
    int_list = [2, 4, 6]
    print(reverse_list(int_list))  # Should print [6, 4, 2]