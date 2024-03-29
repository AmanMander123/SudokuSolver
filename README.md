# Sudoku Solver

## Purpose
The purpose of this Python program is to solve a sudoku puzzle. 

## Input
The input is a CSV file consisting of an unsolved Sudoku with 0's representing as blanks. For example:
  
0,3,5,2,9,0,8,6,4

0,8,2,4,1,0,7,0,3

7,6,4,3,8,0,0,9,0

2,1,8,7,3,9,0,4,0

0,0,0,8,0,4,2,3,0

0,4,3,0,5,2,9,7,0

4,0,6,5,7,1,0,0,9

3,5,9,0,2,8,4,1,7

8,0,0,9,0,0,5,2,6

## Output
The output will be a CSV file consisting of the solved Sudoku. For example, the solutions to the above Sudoku:

1,3,5,2,9,7,8,6,4

9,8,2,4,1,6,7,5,3

7,6,4,3,8,5,1,9,2

2,1,8,7,3,9,6,4,5

5,9,7,8,6,4,2,3,1

6,4,3,1,5,2,9,7,8

4,2,6,5,7,1,3,8,9

3,5,9,6,2,8,4,1,7

8,7,1,9,4,3,5,2,6

## About
Required packages:

  * numpy

  * math
  
  Please name your input CSV file as 'infile.csv' and place it in the same directory as the script
  
  The output file containing the solved puzzle is called 'outfile.csv'
