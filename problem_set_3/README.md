# Problem Set 3: longest_increasing_subsequence

For this problem, there is a given array containing an unordered array, with the array you need to determine the possible sequence if each item in an increasing order without changing there order in the array. Then, determine what sequence has the greatest length and return it's length.

## Solution Overview
To execute the problem, first initialize an array that contains values equal to 1 and the length is based on the length of the data this array will be used to store the number of increase sequence each loop.

Then loop thought the given data using nested loop, in each loop validate if the outer item is greater than the inner item. If it is greater, I will update the score of the current outer item, if the score of the current outer item is greater than the score of inner item + 1, I will retain the score. But if it's lower, I will change it's value with the score of inner item + 1.

After looping, with the updated score for each data, I will get the highest number to determine the longest increasing subsequence.

## Instructions to Run the Code
python .\problem_set_3\longest_increasing_subsequence.py