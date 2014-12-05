# Generate tests from a simple DSL file

We are going to implement a simple Python program, that reads a very minimal DSL (Domain Specific Language) and translates it to a Python unittest file.

Our language will be very basic:

* On the first lines, we are going to define imports
* After all imports, the next line contains the string for the unittest description
* Each line after that, defines one test case. We should skip the empty lines.


For example, lets have the following file, called `is_prime_test.dsl`:

```
from is_prime import is_prime
"This is a test class for testing is_prime funciton"

"7 should noot be prime" -> is_prime(7) == True

"8 should be prime" -> is_prime(8) == False
```

If we run our script like so:

```
$ python generate_tests.py is_prime_test.dsl
```

We should get a file, called `is_prime_test.py` with the following contents:

```python
import unittest

from is_prime import is_prime


class IsPrimeTests(unittest.TestCase):
    """This is a test class for testing is_prime funciton"""
    def testCase1(self):
        self.assertTrue(is_prime(7), "7 should noot be prime")

    def testCase2(self):
        self.assertFalse(is_prime(8), "8 should be prime")

if __name__ == '__main__':
    unittest.main()
```

## Names of files and classes

If our DSL file is named `is_prime_test.dsl`, then:

* The test file should be called `is_prime_test.py`
* The class should be called `IsPrimeTest`

## Different asserts

You should be smart about the asserts.

If there is a line in our DSL, that looks like that:

```
"8 should not be prime" -> is_prime(8) == False
```

The script should generate an `assertFalse` statement:

```python
self.assertFalse(is_prime(8), "8 should not be prime")
```

If we compare values, that are not Booleans, like:

```
"5 is the sum of 3 and 2" -> sum(3, 2) == 5
```

The script should generate an `assertEqual`:

```python
self.assertEqual(5,  sum(3,2), "5 is the sum of 3 and 2")
```

## Multiple imports

If we have multiple imports in the beginning of our dsl:

```
from is_prime import is_prime
from prime_factorization import prime_factorization
```

This should generate the beginning of a test like that:

```python
import unittest

from is_prime import is_prime
from prime_factorization import prime_factorization

class IsPrimeTests(unittest.TestCase):
    pass

if __name__ == '__main__':
    unittest.main()

```

You should take care of them.
We can have a variable number of imports, so be smart with the parsing!

Also, if there are no tests, make an empty class;
