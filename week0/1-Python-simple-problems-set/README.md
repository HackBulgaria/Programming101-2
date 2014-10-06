A bunch of simple problems, to warm up with Python. Those are the regular programming problems, that you meet in every beginners course.

The solutions should be written for Python 3.* version.

## N-th Fibonacci

The most annoying problem of all. Implement a function, called ```nth_fibonacci(n)``` that returns the n-th fibonacci number, given by the argument.

### Signature

```python
def nth_fibonacci(n):
    #implementation here
```

### Test examples

```
>>> nth_fibonacci(1)
1
>>> nth_fibonacci(2)
1
>>> nth_fibonacci(3)
2
>>> nth_fibonacci(10)
55
>>>
```

## Sum all digits of a number

Given an integer, implement a function, called ```sum_of_digits(n)``` that calculates the sum of the digits of n.

If a negative number is given, the function should work as if it was positive.

For example, if n is ```1325132435356```, the digit's sum is 43.
If n is -10, the sum is 1 + 0 = 1

Keep in mind that in Python, there is a special operator for integer division:

```
>>> 5 / 2
2.5
>>> 5 // 2
2
```

### Signature

```python
def sum_of_digits(n):
    # implementation
```

### Test examples

```
>>> sum_of_digits(1325132435356)
43
>>> sum_of_digits(123)
6
>>> sum_of_digits(6)
6
>>> sum_of_digits(-10)
1
```

## Sum all divisors of an integer

Given an integer, implement a function, called ```sum_of_divisors(n)``` that calculates the sum of all divisors of n.

For example, the divisors of 8 are 1,2,4 and 8 and ```1 + 2 + 4 + 8 = 15```
The divisors of 7 are 1 and 7, which makes the sum = 8

### Signature

```python
def sum_of_divisors(n):
    # implementation
```

### Test examples

```
>>> sum_of_divisors(8)
15
>>> sum_of_divisors(7)
8
>>> sum_of_divisors(1)
1
>>> sum_of_divisors(1000)
2340
```

## Check if integer is prime

Given an integer, implement a function, called ```is_prime(n)``` which returns True if n is a prime number. You should handle the case with negative numbers too.

A primer number is a number, that is divisible only by 1 and itself.

1 is not considered to be a prime number. [If you are curious why, find out here.](http://www.youtube.com/watch?v=IQofiPqhJ_s)

### Signature

```python
def is_prime(n):
    # implementation
```

### Test examples

```
>>> is_prime(1)
False
>>> is_prime(2)
True
>>> is_prime(8)
False
>>> is_prime(11)
True
>>> is_prime(-10)
False
```

## Check if a number has a prime number of divisors

Given an integer, implement a function, called ```prime_number_of_divisors(n)``` which returns True if the number of divisors of n is a prime number. False otherwise.

For example, the divisors of 8 are 1,2,4 and 8, a total of 4. 4 is not a prime.
The divisors of 9 are 1,3 and 9, a total of 3, which is a prime number.

### Signature

```python
def prime_number_of_divisors(n):
    # Implementation
```

### Test examples

```
>>> prime_number_of_divisors(7)
True
>>> prime_number_of_divisors(8)
False
>>> prime_number_of_divisors(9)
True
```

## Are there n sevens in a row?

Implement a function, called ```sevens_in_a_row(arr, n)```, which takes an array of integers ```arr``` and a number ```n > 0```

The function returns True, __if there are n consecutive sevens__ in ```arr```

For example, if ```arr``` is ```[10, 8, 7, 6, 7, 7, 7, 20, -7]``` and n is 3, the function should return True. Otherwise, it returns False

### Signature

```python
def sevens_in_a_row(arr, n)
```

### Test examples

```
>>> sevens_in_a_row([10,8,7,6,7,7,7,20,-7], 3)
True
>>> sevens_in_a_row([1,7,1,7,7], 4)
False
>>> sevens_in_a_row([7,7,7,1,1,1,7,7,7,7], 3)
True
>>> sevens_in_a_row([7,2,1,6,2], 1)
True
```

## Integer Palindromes

A palindrome is а word or a phrase or a number, that when reversed, stays the same.

For example, the following sequences are palindromes : "azobi4amma4iboza" or "anna".

But this time, we are not interested in words but numbers.
A number palindrome is a number, that taken backwards, remains the same.

For example, the numbers 1, 4224, 9999, 1221 are number palindromes.

Implement a function, called ```is_int_palindrome(n)``` which takes an integer and returns True, if this integer is a palindrome.

### Signature

```python
def is_int_palindrome(n):
    # implementation
```

### Test examples

```
>>> is_int_palindrome(1)
True
>>> is_int_palindrome(42)
False
>>> is_int_palindrome(100001)
True
>>> is_int_palindrome(999)
True
>>> is_int_palindrome(123)
False
```

## Number containing a single digit?

Implement a function, called ```contains_digit(number, digit)``` which checks if ```digit``` is contained by the given ```number```.

```digit``` and ```number``` are integers.

### Signature

```python
def contains_digit(number, digit):
    # Implementation
```

### Test examples

```
>>> contains_digit(123, 4)
False
>>> contains_digit(42, 2)
True
>>> contains_digit(1000, 0)
True
>>> contains_digit(12346789, 5)
False
```

## Number containing all digits?

Implement a function, called ```contains_digits(number, digits)``` where ```digits``` is a __list of integers__ and a ```number``` is an integer.

The function should return True if __all__ ```digits``` are contained by ```number```

### Signature

```python
def contains_digits(number, digits):
    # Implementation
```

### Test examples

```
>>> contains_digits(402123, [0, 3, 4])
True
>>> contains_digits(666, [6,4])
False
>>> contains_digits(123456789, [1,2,3,0])
False
>>> contains_digits(456, [])
True
```

## Is number balanced?

A number is called balanced, if we take the middle of it and the sums of the left and right parts are equal.

For example, the number ```1238033``` is balanced, bacause it has a left part, equal to 123, and right part, equal ot 033.

We have : ```1 + 2 + 3 = 0 + 3 + 3 = 6```

A number with only one digit is always balanced.

Implement a function, called ```is_number_balanced(n)``` which checks if the given number is balanced.

### Signature

```python
def is_number_balanced(n):
    # Implementation
```

### Test examples

```
>>> is_number_balanced(9)
True
>>> is_number_balanced(11)
True
>>> is_number_balanced(13)
False
>>> is_number_balanced(121)
True
>>> is_number_balanced(4518)
True
>>> is_number_balanced(28471)
False
>>> is_number_balanced(1238033)
True

```

## Counting substrings

Implement a function, called ```count_substrings(haystack, needle)``` which returns the count of occurrences of the string ```needle``` in the string ```haystack```.

__Don't count overlapped substings and take case into consideration!__
For overlapping substrings, check the "baba" example below.

### Signature

```python
def count_substrings(haystack, needle):
    # Implementation
```

### Test examples
```
>>> count_substrings("This is a test string", "is")
2
>>> count_substrings("babababa", "baba")
2
>>> count_substrings("Python is an awesome language to program in!", "o")
4
>>> count_substrings("We have nothing in common!", "really?")
0
>>> count_substrings("This is this and that is this", "this")  # "This" != "this"
2
```

## Vowels in a string

Implement a function, called ```count_vowels(str)``` which returns the count of all vowels in the given string ```str```. __Count uppercase vowels as well!__

The vowels are ```aeiouy```.

### Signature

```python
def count_vowels(str):
    # Implementation
```

### Test examples

```
>>> count_vowels("Python")
2
>>> count_vowels("Theistareykjarbunga") #It's a volcano name!
8
>>> count_vowels("grrrrgh!")
0
>>> count_vowels("Github is the second best thing that happend to programmers, after the keyboard!")
22
>>> count_vowels("A nice day to code!")
8
```

## Consonants in a string

Implement a function, called `count_consonants(str)` which returns the count of all consonants in the given string `str`. __Count uppercase consonants as well!__

The consonants are ```bcdfghjklmnpqrstvwxz```.

### Signature

```python
def count_consonants(str):
    # Implementation
```

### Test examples

```
>>> count_consonants("Python")
4
>>> count_consonants("Theistareykjarbunga") #It's a volcano name!
11
>>> count_consonants("grrrrgh!")
7
>>> count_consonants("Github is the second best thing that happend to programmers, after the keyboard!")
44
>>> count_consonants("A nice day to code!")
6
```

## Turn a number into a list of digits

Implement a function, called ```number_to_list(n)``` which takes an integer ```n``` and returns a list, containing the digits of ```n```

### Signature

```python
def number_to_list(n):
    # Implementation
```

### Test Examples

```
>>> number_to_list(123)
[1, 2, 3]
>>> number_to_list(99999)
[9, 9, 9, 9, 9]
>>> number_to_list(123023)
[1, 2, 3, 0, 2, 3]
```

## Turn a list of digits into a number

Implement a function, called ```list_to_number(digits)``` which takes a list of digits (integers) and returns the number, containing those digits.

### Signature

```python
def list_to_number(digits):
    # Implementation
```

### Test Examples

```
>>> list_to_number([1,2,3])
123
>>> list_to_number([9,9,9,9,9])
99999
>>> list_to_number([1,2,3,0,2,3])
123023
```

## Biggest difference between two numbers

Implement a function, called ```biggest_difference(arr)```, which takes an array of integers and returns the biggest difference between any two numbers from the array.

For every two elements from the array ```a``` and ```b```, we are looking for the minimum of ```a - b``` or ```b - a```

### Signature

```python
def biggest_difference(arr):
    # Implementation
```

### Test examples

```
>>> biggest_difference([1,2])
-1
>>> biggest_difference([1,2,3,4,5])
-4
>>> biggest_difference([-10, -9, -1])
-9
>>> biggest_difference(range(100))
-99
```

## Increasing sequence?

Implement a function, called ```is_increasing(seq)``` where ```seq``` is a list of integers.

The function should return True, if the given sequence is monotonously increasing.

And before you skip this problem, because of the math terminology, let me explain:

> A sequence is monotonously increasing if for every two elements a and b, that are next to each other (a is before b), we have a < b

For example, ```[1,2,3,4,5]``` is monotonously increasing while ```[1,2,3,4,5,1]``` is not.

### Signature

```python
def is_increasing(seq):
    # Implementation
```

### Test examples

```
>>> is_increasing([1,2,3,4,5])
True
>>> is_increasing([1])
True
>>> is_increasing([5,6,-10])
False
>>> is_increasing([1,1,1,1])
False
```

## Descreasing sequence?

Implement a function, called ```is_decreasing(seq)``` where ```seq``` is a list of integers.

The function should return True, if the given sequence is monotonously decreasing.

And before you skip this problem, because of the math terminology, let me explain:

> A sequence is monotonously decreasing if for every two elements a and b, that are next to each other (a is before b), we have a > b

For example, ```[5,4,3,2,1]``` is monotonously decreasing while ```[1,2,3,4,5,1]``` is not.

### Signature

```python
def is_decreasing(seq):
    # Implementation
```

### Test examples

```
>>> is_decreasing([5,4,3,2,1])
True
>>> is_decreasing([1,2,3])
False
>>> is_decreasing([100, 50, 20])
True
>>> is_decreasing([1,1,1,1])
False
```

## Zero Insertion

Given an integer, implement a function, called `zero_insert(n)`, which returns a new integer, constructed by the following algorithm:

* If two neighboring digits are the same (like `55`), insert a 0 between them (`505`)
* Also, if we add two neighboring digits and take their module by 10 (`% 10`) and the result is 0 - add 0 between them.

For example, if we have the number `116457`, result will be: `10160457`:

* 1 and 1 are the same, so we insert 0 between them
* `6 + 4 % 10 = 0`, so we insert 0 between them.


### Examples

```python
zero_insert(116457)
10160457
zero_insert(55555555)
505050505050505
zero_insert(1)
1
zero_insert(6446)
6040406
```

## Sum Numbers in Matrix

You are given a `NxM` matrix  of integer numbers.

Implement a function, called `sum_matrix(m)` that returns the sum of all numbers in the matrix.

The matrix will be represented as nested lists in python.

### Examples:

```python
>>> m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> sum_matrix(m)
45
>>> m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
>>> sum_matrix(m)
0
>>> m = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
>>> sum_matrix(m)
55
```

## Matrix Bombing

You are givn a `NxM` matrix of integer numbers.

We can drop a bomb at any place in the matrix, which has the following effect:

* All of the 8 neighbours of the target are reduced by the value of the target.
* Numbers can be reduced only to 0 - they cannot go to negative.

For example, if we have the following matrix:

```
10 10 10
10  9  10
10 10 10
```

and we drop bomb at `9`, this will result in the following matrix:

```
1 1 1
1 9 1
1 1 1
```

Implement a function called `matrix_bombing_plan(m)`.

The function should return a dictionary where keys are positions in the matrix, represented as tuples, and values are the total sum of the elements of the matrix, after the bombing at that position.

The positions are the standard indexes, starting from `(0, 0)`

For example if we have the following matrix:

```
1 2 3
4 5 6
7 8 9
```

and run the function, we will have:

```python
{(0, 0): 42,
 (0, 1): 36,
 (0, 2): 37,
 (1, 0): 30,
 (1, 1): 15,
 (1, 2): 23,
 (2, 0): 29,
 (2, 1): 15,
 (2, 2): 26}
```

We can see that if we drop the bomb at `(1, 1)` or `(2, 1)`, we will do the most damage!

## Hack Numbers

A hack number is an integer, that matches the following criteria:

* The number, represented in binary, is a palindrom
* The number, represented in binary, has an odd number of 1's in it

Example of hack numbers:

* 1 is `1` in binary
* 7 is `111` in binary
* 7919 is `1111011101111` in binary

Implement a function, called `next_hack(n)` that takes an integer and returns the next hack number, that is bigger than `n`

### Examples

```python
>>> next_hack(0)
1
>>> next_hack(10)
21
>>> next_hack(8031)
8191
```

## NaN Expand

In most programming languages, `NaN` stands for `Not a Number`

If we take a look at the following JavaScript code:

```javascript
typeof NaN === 'number' // true
```

We will see that in JavaScript, `NaN` stands for `Not a NaN`, which is recursive by nature.

Implement a python function, called `nan_expand(times)`, which returns the expansion of `NaN` (In JavaScript terms :P) that many `times`

For example:

* If we expand `NaN` once (`times=1`), we will have `"Not a NaN"`
* If we expand `NaN` twice (`times=2`), we will have `"Not a Not a NaN"`
* If `times=3`, we have `"Not a Not a Not a NaN"`
* And so on ...

### Examples

```python
>>> nan_expand(0)
""
>>> nan_expand(1)
"Not a NaN"
>>> nan_expand(2)
"Not a Not a NaN"
>>> nan_expand(3)
"Not a Not a Not a NaN"
```

## Iterations of NaN Expand

Implement a function, called `iterations_of_nan_expand(expanded)` that takes a string `expanded`, which is an unkown iteration of NaN Expand (check the problem for more information)

The function should return the number of iterations that have been made, in order to get to `expanded`

For example, if we have `"Not a Not a Not a NaN"` - this is the 3rd iteration of `NaN`

**If `expanded` is not a valid NaN expand string, the function should return false! (This is the hard part)**

### Examples

```python
>>> iterations_of_nan_expand("")
0
>>> iterations_of_nan_expand("Not a NaN")
1
>>> iterations_of_nan_expand('Not a Not a Not a Not a Not a Not a Not a Not a Not a Not a NaN')
10
>>> iterations_of_nan_expand("Show these people!")
False
```



## Integer prime factorization

Given an integer ```n```, we can factor it in the following form:

> n = p1^a1 * p2^a2 * ... * pn^an

Where each p is a prime number and each a is an integer and p^a means p to the power of a.

[This is called prime factorization.](http://mathworld.wolfram.com/PrimeFactorization.html)

Lets see few examples

> 10 = 2^1 * 5^1
> 25 = 5^2
> 356 = 2^2 * 89 ^ 1

Implement a function, called ```prime_factorization(n)``` which takes an integer and returns a list of tuples ```(pi, ai)```, which is the result of the factorization.

The list should be sorted in increasing order of the prime numbers.

### Signature

```python
def prime_factorization(n):
    # Implementation
```

### Test examples

```
>>> prime_factorization(10)
[(2, 1), (5, 1)] # This is 2^1 * 5^1
>>> prime_factorization(14)
[(2, 1), (7, 1)]
>>> prime_factorization(356)
[(2, 2), (89, 1)]
>>> prime_factorization(89)
[(89, 1)] # 89 is a prime number
>>> prime_factorization(1000)
[(2, 3), (5, 3)]
```
## Calculate coins

This problem is from the [Python 2013 course in FMI](http://2013.fmi.py-bg.net/)

Implement a function, called ```calculate_coins(sum)``` where sum is a floating point number.

The function should return a dictionary, that represents a way to get the sum with minimal number of coins.

__The coins that we can use are with values 1,2,100,5,10,50,20.__

Check the examples below.

### Signature

```python
def calculate_coins(sum):
    # Implementation
```

### Test examples

```
>>> calculate_coins(0.53)
{1: 1, 2: 1, 100: 0, 5: 0, 10: 0, 50: 1, 20: 0} # We pay with one coin of value 50 and two coins of value 2 and one coin of value 1 - that's the minimal number of coins to get to 0.53
>>> calculate_coins(8.94)
{1: 0, 2: 2, 100: 8, 5: 0, 10: 0, 50: 1, 20: 2}
```

## What is the sign?

This problem is from the Python 2013 course in FMI. [Link to original problem statement.](http://2013.fmi.py-bg.net/tasks/1)

Implement a function, called ```what_is_my_sign(day, month)``` which takes two integers (one for the day and one for the month) and returns the name of the zodiac for the given time period.

Consider the following zodiac table ([Or check wikipedia](http://en.wikipedia.org/wiki/Zodiac#Table_of_dates)) :

* Aries: 21 March – 20 April
* Taurus: 21 April – 21 May
* Gemini: 22 May – 21 June
* Cancer: 22 June – 22 July
* Leo: 23 July – 22 August
* Virgo: 23 August – 23 September
* Libra: 24 September – 23 October
* Scorpio: 24 October – 22 November
* Sagittarius: 23 November – 21 December
* Capricorn: 22 December – 20 January
* Aquarius: 21 January – 19 February
* Pisces: 20 February – 20 March


### Signature

```python
def what_is_my_sign(day, month):
    # Implementation
```

### Test examples

```
>>> what_is_my_sign(5, 8)
"Leo"
>>> what_is_my_sign(29, 1)
"Aquarius"
>>> what_is_my_sign(30, 6)
"Cancer"
>>> what_is_my_sign(31, 5)
"Gemini"
>>> what_is_my_sign(2, 2)
"Aquarius"
>>> what_is_my_sign(8, 5)
"Taurus"
>>> what_is_my_sign(9, 1)
"Capricorn"
```
