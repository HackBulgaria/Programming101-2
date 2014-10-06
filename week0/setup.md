# Programing 101 Setup guide

At this point you should already have an installed and working Ubuntu.
Now we're going to setup Python, an editor and start coding.


## Setup Python3.3+

We're going to use CPython 3.3+, the default Python interpreter.

You can install python3.3+ using your package manager.

```
	$ sudo apt-get install python3
```

At the end of the process you should see:
```
Python 3.4.0 (default, Apr 11 2014, 13:05:11)
[GCC 4.8.2] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

## Setup an editor

If you are not a Vim user, we suggest you to install Sublime Text 3 or Github Atom.

They're highly configurable text editors.

For the difference between an IDE and a text editor, we suggest you to watch the following video: https://www.youtube.com/watch?v=qLDU8ugpO9Y (It's in Bulgarian)

### Sublime Text 3 (recommended)

[Installation steps and guide](http://scotch.io/bar-talk/the-complete-visual-guide-to-sublime-text-3-getting-started-and-keyboard-shortcuts)

After you've installed Sublime Text 3, install packages:
* Anaconda
* SideBarEnhancements

To install a package watch [Sublime Text 3: Installing Package Control Part II](https://www.youtube.com/watch?v=Y1f6BuSdP_c)
and in the newly opened bar, type the package name and press Enter.

### Github Atom (the alternative and future)

[Installation steps and guide](http://syndbg.github.io/atom-setting-up-for-python-development.html)

The above link covers the necessary packages for Python development.


## All working?

To illustrate things, let's imagine that we have to implement a python program,
 that calculates the sum of two integers.

Here we have the code:

```python
def awesome_sum(a, b):
    return a + b
```

And now, we want to use our function.

We propose two different approaches for this:

#### Simple import

If your source file is named `solution.py`, do the following:

* Navigate to the directory, where `solution.py` is located;
* Run the python interpreter by typing `python` or `python3` (Depends on the version you have. We need 3.3+)
* Import the function - `from solution import awesome_sum` - The algorithm here is `from file_name_without_py import function_name`
* Use it - `awesome_sum(1, 2)`

```
>>> awesome_sum(1, 2)
3
```

#### main() method

Add a main method and a call it in your `solution.py` file:

```python
def awesome_sum(a, b):
    return a + b


def main():
    print(awesome_sum(1, 3))
    # more test cases to follow

# This piece of code will call the main method,
# When you run solution.py via the interpreter
if __name__ == '__main__':
    main()
```

After this, you can just call the program with your python interpreter:

```bash
$ python solution.py
4
```
