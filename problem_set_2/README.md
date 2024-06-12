# Problem Set 2: valid_parenthesis

## Problem Description
For this problem, there is a string of kinds of bracket symbols and you need to determine if the string the closed accordingly based on the open and closing symbol and every open bracket symbol is closed by its correct closing bracket symbol.

## Solution Overview
To execute the problem, first I generated an array for opening symbols to match the current character if it's an opening or closing symbol, then I also generated an object where each key-value pair is the pairing of the brackets.
Then, I initialize an array to store the order of opening symbols, after that I loop throught the string, every loop I check if it's an opening symbol or not. If it's in the open array, I store the character in the array I initialze for storing the opening symbols named "last_open_symbols".
If the current character is a closing bracket, I validate what opening pair is associatated with that closing bracket then I check if the pair of the closing bracket is equal to the last item of "last_open_symbols", if it matches I will remove the last item in "last_open_symbols" since it means that it was closed correctly, but if the associated pair of the closing bracket and the last item in "last_open_symbols" is not same, I will return False since it means the opening bracket was not closed by it's closing bracket pair. 
Then after looping through the string, I will return True which means all opening brackets was closed correctly.

## Instructions to Run the Code
python .\problem_set_2\valid_parenthesis.py