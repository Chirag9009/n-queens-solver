# n-queens solver
A backtracking based n queens problem solver.
The N Queen is the problem of placing N chess queens on an N×N chessboard so that no two queens attack each other.

## Naive Algorithm
Generate all possible configurations of queens on board and print a configuration that satisfies the given constraints.

## Backtracking Algorithm
The idea is to place queens one by one in different columns, starting from the leftmost column. When we place a queen in a column, we check for clashes with already placed queens. In the current column, if we find a row for which there is no clash, we mark this row and column as part of the solution. If we do not find such a row due to clashes then we backtrack and return false.
