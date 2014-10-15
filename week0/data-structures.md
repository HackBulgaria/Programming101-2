# Data Structures

As you may have already noticed, Python3 data structures are way different than the C++ structures you know.
List stores pointers to elements.


## List

It does not work like a traditional array. It is heterogeneous!

```python
hacker_things = [1, 2, 3, 'Ivan', [10, 'Hack']]
```

We can get elements by index:
```python
print(hacker_things[3]) # Ivan
```

We can iterate:
```python
for thing in hacker_things:
    print('I tend to like ' + thing)
```

You can look at the list's interface here: https://docs.python.org/3.4/tutorial/datastructures.html#more-on-lists


## Tuple

Tuples are much like lists but __they are immutable!__

super_heroes = ('Hackman', 'Spiderman', 'Hulk')

```python
super_heroes[1] = 'Spindi'

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
```

The interface is identical to a list's. You can see it in action [here](https://docs.python.org/3.4/tutorial/datastructures.html#tuples-and-sequences)


## Set
Go get your math books. This is a real set.

A set is an unordered collection with no duplicate elements.
Basic usage includes membership testing and eliminating duplicate entries.
Set objects also support mathematical operations like `union`, `intersection`, `difference`, and `symmetric difference`.


```python
rappers = set()
rappers.add('Eminem')
rappers.add('Jay-Z')
rappers.add('Eminem')

print(rappers) # {'Jay-Z', 'Eminem'}
```

You can see more sets usage [here](https://docs.python.org/3.4/tutorial/datastructures.html#sets).


## Dictionaries
__Are hash tables, also known as associative arrays!__


```python
youtube_views = {
    'Gangnam Style': 2096709806,
    'Baby': 1091538504,
    'Waka Waka': 746709408,
}

print(youtube_views['Waka Waka']) # 746709408
```

Values are added by assigning them to `keys`.

```python
youtube_views['Wrecking Ball'] = 709604432
```
If that `key` already exists, the value held by that key will be replaced.

```python
youtube_views['Wrecking Ball'] = 859604432
```

```python
print(youtube_views) # { 'Wrecking Ball': 859604432 , 'Gangnam Style': 2096709806, 'Waka Waka': 746709408, 'Baby': 1091538504}
```
