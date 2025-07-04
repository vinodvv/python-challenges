"""
Day 27: Unique Numbers
Write a function called unique_numbers that takes a list of numbers
as an argument. Your function is going to find all the unique numbers
in the list. It will then sum up the unique numbers. You will calculate
the difference between the sum of all the numbers in the original
list and the sum of unique numbers in the list. If the difference is
an even number, your function should return the original list. If the
difference is an odd number, your function should return a list with
unique numbers only. For example [1, 2, 4, 5, 6, 7, 8, 8] should
return [1, 2, 4, 5, 6, 7, 8, 8].
"""


def uniq_numbers(numbers):
    list1 = []
    for number in numbers:
        if number not in list1:
            list1.append(number)
    difference = sum(numbers) - sum(list1)
    if difference % 2 == 0:
        return numbers
    else:
        return list1


def unique_numbers(numbers):
    uniques = list(set(numbers))  # get unique values from the list using set
    difference = sum(numbers) - sum(uniques)  # calculates the difference between the total sum and the sum of uniques
    if difference % 2 == 0:  # checks if the difference is even.
        return numbers  # if even, returns the original list.
    else:
        return uniques  # if odd, returns the list os unique values.


if __name__ == "__main__":
    nums = [1, 2, 4, 5, 6, 7, 8, 8]
    nums1 = [1, 2, 5, 5, 6, 7, 8, 8]
    print(uniq_numbers(nums))
    print(unique_numbers(nums))
    print(uniq_numbers(nums1))
    print(unique_numbers(nums1))
