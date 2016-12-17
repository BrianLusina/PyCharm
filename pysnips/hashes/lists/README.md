# Lists

This comprises of list exercises of programs that deal mainly in the manipulation of lists using Python

Here is a breakdown of the lists programs and their descriptions

## Sum of Repeats

Write a function that takes a list comprised of other lists of integers and returns the sum of all numbers that appear in two or more lists in the input list. Now that might have sounded confusing, it isn't:

```python
repeat_sum([[1, 2, 3],[2, 8, 9],[7, 123, 8]])
>>> sum of [2, 8]
return 10

repeat_sum([[1], [2], [3, 4, 4, 4], [123456789]])
>>> sum of []
return 0

repeat_sum([[1, 8, 8], [8, 8, 8], [8, 8, 8, 1]])
sum of [1,8]
return 9
```

## Lists to Tuples

Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
```python
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')
```
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
tuple() method can convert list to tuple

## 2D Array

Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,..,Y-1.
Example
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
```python
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 
```

Hints:
Note: In case of input data being supplied to the question, it should be assumed to be a console input in a comma-separated form.

## Counter

Function that counts the number of times an item appears in a list

## Purify

takes in a list of numbers, removes all odd numbers in the list, and returns the result.

## Product

Returns the product of all the items in a list

## Remove Duplicates

Function that takes in a list and removes elements of the list that are the same

## Square Odds

Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.
Suppose the following input is supplied to the program:
1,2,3,4,5,6,7,8,9
Then, the output should be:
1,3,5,7,9

## Print array

Input: Array of elements
["h","o","l","a"]
Output: String with comma delimited elements of the array in th same order.
"h,o,l,a"

## Bus stops
There is a bus moving in the city, and it takes and drop some people in each bus stop.

You are provided a list (or array in JS) of integer array. Each integer array has two items which represent number of 
people get into bus (The first item) and number of people get off the bus (The second item).

The first integer array has 0 number in the second item, since the bus is empty in the first bus stop.

Your task is to return number of people in the bus after the last bus station. Take a look on the test cases :)

Please keep in mind that the test cases ensure that the number of people in the bus is always >= 0. So the return integer can't be negative.

## Array Diff

Your goal in this kata is to implement an difference function, which subtracts one list from another.
It should remove all values from list a, which are present in list b.
array_diff([1,2],[1]) == [2]
If a value is present in b, all of its occurrences must be removed from the other:
array_diff([1,2,2,2,3],[2]) == [1,3]