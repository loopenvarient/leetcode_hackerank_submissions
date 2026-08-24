# Dynamic Array

> Data Structures | Arrays | HackerRank

## Problem Overview

- Platform: HackerRank
- Domain: Data Structures
- Track: Arrays
- Difficulty: Easy
- Problem ID: 13642
- Max Score: 15
- Problem Link: [https://www.hackerrank.com/challenges/dynamic-array/problem](https://www.hackerrank.com/challenges/dynamic-array/problem)

## Problem

- Declare a 2-dimensional array, $arr$, with $n$ empty arrays, all zero-indexed.
- Declare an integer, $lastAnswer$, and initialize it to 0.

You need to process two types of queries:

1. Query: $1\ x\ y$
   - Compute $idx = (x \oplus lastAnswer) % n$.
   - Append the integer $y$ to $arr[idx]$.

2. Query: $2\ x\ y$
   - Compute $idx = (x \oplus lastAnswer) % n$.
   - Set $lastAnswer = arr[idx][y \% size(arr[idx])]$.
   - Store the new value of $lastAnswer$ in an answers array.

**Notes:**  
- $\oplus$ is the *bitwise XOR* operation, which corresponds to the `^` operator in most languages. Learn more about it on [Wikipedia](https://en.wikipedia.org/wiki/Exclusive_or).  
- $\%$ is the modulo operator.   
- Finally, $size(arr[idx])$ is the number of elements in $arr[idx]$.  

**Function Description**  

Complete the $dynamicArray$ function with the following parameters:  
- $int\ n$: the number of empty arrays to initialize in $arr$  
- $int\ queries[q][3]$: 2-D array of integers

**Returns**  

- $int[]$:  the results of each type 2 query in the order they are presented

## Submission

| Item | Value |
| --- | --- |
| Status | Accepted |
| Language | python3 |
| Score | 15.0 |
| Testcases | 11/11 passed |
| Submission ID | 481107602 |

---

_Synced with AlgorithmHub_