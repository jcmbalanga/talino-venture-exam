# Problem Set 1: palindrome_pairs

## Problem Description
For this problem, there is an array of strings where you need to loop to check if the concatenation of two strings forms a palindrome.

## Solution Overview
To execute the problem, first perform a nested loop where the outer loop iterates over the array and the inner loop will be the items next to the outer item. 
Then, you need to validate if the reverse string of outer item is equal to inner item, if they match store the pair of indices on an array.
Finally, after looping over the data return the indices formed by matching the reverse string of outer loop and inner loop.

## Instructions to Run the Code
python .\problem_set_1\palindrome.py