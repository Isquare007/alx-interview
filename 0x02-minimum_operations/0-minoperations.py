#!/usr/bin/python3
"""
 In a text file, there is a single character H.
 Your text editor can execute only two operations in this file:
 Copy All and Paste. Given a number n, write a method that calculates
 the fewest number of operations needed to result
 in exactly n H characters in the file.
"""


def minOperations(n):
    """
    it calculate the total number of operations needed
    to get the value of n
    """
    if n <= 1:
        return 0

    operations = 0
    i = 2
    while i <= n//2:
        while n % i == 0:  # check prime
            operations += i
            n //= i
        i += 1
    if n > 1:  # if n is prime number add it
        operations += n
    return operations
