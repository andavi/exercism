import re


def verify(isbn):
    # Create list of integers.
    nums = [10 if n == 'X' else int(n) for n in re.findall('[0-9X]', isbn)]
    
    # Check length, check digit, and modulo.
    return len(nums) == 10 and 10 not in nums[:9] \
        and sum([a*b for a,b in zip(nums, range(10, 0, -1))]) % 11 == 0
