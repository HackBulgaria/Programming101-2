# Data Structures

As you may already have noticed python3 data structures are way different then C++ structures that you are used to.
List stores pointers to elements.

## List

It dose not work like a traditional array. It is heterogeneous!

```python
hacker_things = [1, 2, 3, 'Ivan', [10, 'Hack']]
```

We can index elements:
```python
print(hacker_things[3]) # Ivan
```

We can iterate them:
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

## Set
Go get your math books. This is a real set. 

A set is an unordered collection with no duplicate elements. Basic uses include membership testing and eliminating duplicate entries. Set objects also support mathematical operations like union, intersection, difference, and symmetric difference.


```python
rappers = set()
rappers.add('Eminem')
rappers.add('Jay-Z')
rappers.add('Eminem')

print(rappers) # {'Jay-Z', 'Eminem'}
```

## Dictionaries
__Hash table!__


```python
youtube_views = {
    'Gangnam Style': 2096709806,
    'Baby': 1091538504,
    'Waka Waka': 746709408,
}

print(youtube_views['Waka Waka']) # 746709408
```

We can add some values and there is no order too.

```python
youtube_views['Wrecking Ball'] = 709604432

print(youtube_views) # { 'Wrecking Ball': 709604432 , 'Gangnam Style': 2096709806, 'Waka Waka': 746709408, 'Baby': 1091538504}
```