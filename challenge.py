"""Find Max Sum
Given an array of strings, each made up of a combination of letters and digits, 
write the functionality to find and return the largest sum of digits within a string.

Considering a variety of different input arrays, state any assumptions 
or design choices you had to make.

Notes:

Each digit should be considered its own 1-digit number i.e. in the third string
below 36 is evaluated as 3 and 6 separately.
The input arrays can vary in length; however, they will not be larger than 10 strings.
Strings can vary in length; however, they will not be larger than 12 characters.

Example:

Input		[ "dh7js4jf", "or2rjvn2w", "h1n36mfl", "a7e6fw" ]
has the sums		11, 4, 10, 13 respectively
so the output is 13"""

import re

def find_max_sum(strings):
    if not strings:
        return 0
    
    max_sum = 0
    
    for string in strings:
        # Extract digits using regex
        digits = re.findall(r'\d', string)
        # Convert to integers and sum them
        current_sum = sum(int(digit) for digit in digits)
        # Tracking of maximum sum
        max_sum = max(max_sum, current_sum)
    
    return max_sum