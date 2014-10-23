We are going to do some basic OOP problems, mixed with unit testing and TDD!

In order to skip the long explanation that can be showed with code, we will jump to the problems.

__When implementing the classes, use the TDD technique!__

## Problem 0 - A hero.

So lets start with something simple. We are going to implement a hero class, step by step.

Implement a class, that represents a hero. Our hero is going to start simple:

* Our hero has a ```name``` attribute
* Our hero has a ```health``` attribute
* Our hero has a ```nicknamе``` attribute

If our hero is implemented in ```hero.py```, here is a simple usage in the __python interpreter__:

```
>>> import hero
>>> h = hero.Hero("Bron", 100, "DragonSlayer")
>>> h
<hero.Hero object at 0x7f5aa39c30d0>
>>> h.name
'Bron'
>>> h.nickname
'DragonSlayer'
>>> h.health
100
```
### known_as() method

Add a ```known_as()``` method to our Hero, which returns a string, formatted in the following way:
```hero_name the hero_nickname```

__For example:__

```
>>> h.known_as()
Bron the DragonSlayer
```

### get_health()

Every hero starts with the given ```health```.

__This ```health``` is the maximum health for the hero!__

When a hero reaches 0 ```health``` he is considered death.

Add this attribute to our hero and implement the following methods:

* ```is_alive()``` which returns True, if our hero is still alive. Otherwise - False.
* ```get_health()``` which returns the current health

### take_damage(damage_points)

So, our hero can take damage which reduces his health.

Implement a method, called ```take_damage(damage_points)``` where damage can be either integer or floating point value.

This method should reduce the hero's health by ```damage```

__If we inflict more damage than we have health, health will always be equal to zero and we cannot get below that!__

### take_healing(healing_points)

Our hero can also be healed!

Implement a method, called ```take_healing(healing_points)``` which heals our hero.

Here are the requirements:

* If our hero is dead, the method should return False. It's too late to heal our hero
* We cannot heal our hero above the maximum health, which is given by ```health```
* If healing is successful (Our hero is not dead), the method should return True

## Problem 1 - The Orc.

In order to have a world of heroes, we must have a world of villains and bad guys.

But this time, we are going one level up - we are having orcs!

In ```orc.py```, implement an Orc class with the following attributes, given to the constructor

* ```name``` - every orc has a name! A terrifying name.
* ```health``` - the starting health for the Orc. This is also his maximum health
* ```berserk_factor``` - a floating point number between 1 and 2. This factor is used, when the Orc goes berserk! __The output damage from the orc is multipled by that factor.__ (If a factor, larger than 2 or smaller than 1 is given, it is bounded by the limit (1 or 2))

Just like our hero, the orc has the same methods for healing, damage and life status:

* get_health()
* is_alive()
* take_damage(damage_points)
* take_healing(healing_points)

## Problem 2 - The Entity? Time to do some refactoring

If we take a look at our Hero and our Orc, they have few things in common:

* name
* health
* get_health()
* is_alive()
* take_damage(damage_points)
* take_healing(healing_points)

The OOP approach can save us some of the code repetition by doing inheritance.

Create a class, called ```Entity``` which shares all the common things between a hero and an orc.

After this, refactor your code and tests, in order to inherit from that Entity and still maintain the specific methods for each class.

If you want to call a superconstructor, you can do it like so:

```python
from entity import Entity


class Hero(Entity):
    def __init__(self, name, health, nickname):
        super().__init__(name, health)
    # ...
```

Refactor your tests as well, so everything can pass!

### Problem 3 - The Weapon!

We are going to make an army of heroes and an army of orcs and make them fight!
But first, we are going to need some weapons.

Create a class ```Weapon```, which takes the following attributes as a constructor:

* ```type``` - a string that represents the weapon. Imagine an axe!
* ```damage``` - how many health points you are going to take away, if you hit!
* ```critical_strike_percent``` - a floating number between 0 and 1 that gives the chance for double damage!

Implement a method, called ```critical_hit()``` which returns True, if the weapon, striking now, should do 2x times the damage, according to the ```critical_strike_percent```.

Otherwise, False

__Example__:

```
>>> from weapon import Weapon
>>> axe = Weapon("Mighty Axe", 25, 0.2)
```

### Problem 4 - Equipping some weapons

It's time to Equip our fighters.

In the ```Entity``` class, add the following methods:

* ```has_weapon()``` - return True, if the given Entity is already equipped with a weapon
* ```equip_weapon(weapon)``` - equips the given weapon to the Entity. If you equip a new weapon, the old one is discarded.
* ```attack()``` - return the damage, that the given Entity is doing. If the entity has no weapon, the damage is 0

In the ```Orc``` class, __override__ the ```attack()``` method to take into account the ```berserk_factor``` !

### Problem 5 - A class for Fighting

Now, it is time to make them fight!

Implement a class ```Fight``` which takes two arguments to the constructor:

* A ```Hero``` instance
* An ```Orc``` instance

The ```Fight``` class flips a coin and decides which will attack first. (Imagine, take random between 0 and 100. If it is < 50, hero attacks first, else orc attacks first)

Implement a ```simulate_fight()``` method, which starts a fight between the hero and the orc, and prints out the status of the battle to the console.

The fight ends, when either the hero or the orc dies!

### Problem 6 - Inside the dungeon

Now, when we can fight our Hero and our Orc, it's time to make an adventure!

But first, lets go step by step. Implement a class ```Dungeon```, that loads a dungeon map from a text file.

The file path should be given as the only argument to the constructor.

A dungeon, looks something like this:

```
S.##......
#.##..###.
#.###.###.
#.....###.
###.#####S
```

Where:

* ```S``` means a starting point - you can spawn there.
* ```#``` is an obstacle - you cannot go there
* ```.``` is a walkable path - you can follow the dots.

For example, lets have a file, called ```basic_dungeon.txt``` which represents the dungeon above.

We create new dungeon like this:

```
>>> from dungeon import Dungeon
>>> map = Dungeon("basic_dungeon.txt")
>>> map.print_map()
S.##......
#.##..###.
#.###.###.
#.....###.
###.#####S
```

For now, implement a method, called ```print_map()``` which prints the map to the output, in a formatted way.


### Problem 7 - It's spawning time.

So, we want to spawn heroes and orcs in our map. To do so, there are __spawning points__ in the map, marked with ```S```

### spawn

Implement a method, called ```spawn(player_name, entity)``` where:

* ```player_name``` is a string, uniquely identifying the player
* ```entity``` is either Orc or Hero

This one takes the first free spawning point in the map and populates it with:

* ```H``` if entity is a Hero
* ```O``` if entitity is an Orc

The first free spawning point is the one, that we get if we start from top-left and walk left.

If the spawning is successful - return True. Otherwise (If there are no more spawning points, return False)


So, if we have the map above, let's take the following example:

```
>>> map.spawn("player_1", some_hero_instance)
True
>>> map.print_map()
H.##......
#.##..###.
#.###.###.
#.....###.
###.#####S
>>> map.spawn("player_2", some_orc_instance)
True
>>> map.print_map()
H.##......
#.##..###.
#.###.###.
#.....###.
###.#####O
```

### Problem 8 move()

Now, implemented a method ```move(player_name, direction)``` where:

* ```player_name``` is the unique identifier for the player
* ```direction``` is ```up```, ```down```, ```left``` and ```right```

This should move the given player in the desired direction.

__For example:__

```
>>> map.move("player_1", "right")
True
>>> map.print_map()
.H##......
#.##..###.
#.###.###.
#.....###.
###.#####O
>>> map.move("player_1", "up")
False
>>> map.move("player_2", "up")
True
>>> map.print_map()
.H##......
#.##..###.
#.###.###.
#.....###O
###.#####.
```

Here are the cases:

* If you move into an obstacle, return False and don't make the move.
* If you move outside the map - return False and don't make the move.
* If you move into an enemy, create a new Fight and simulate it!

## Problem 9 spawn_weapons()
Different weapons are described at the end of every dungeon file. They are described in this way: weapon_name damage critical_chance. Every weapon is described on a new line.

Example:

```text
S.##......
#.##..###.
#.###.###.
#.....###.
###.#####S

BigAxe 25 0.2
SmallAxe 19 0.7
```

Your task is to load this weapons and to spawn it in a random places.

__For example:__

```
>>> from dungeon import Dungeon
>>> map = Dungeon("basic_dungeon.txt")
>>> map.print_map()
S.##..W...
#.##..###.
#.###.###.
#...W.###.
###.#####S
```

We mark a weapon on the map with __W__ while printing the map.

If a player gets to the weapons it automatically takes that weapon.

## Problem 10 start_fight()
If Ork and Hero gets in the same position they automatically start a fight until one of them is dead. Dead characters dose not show on the map.

__For example:__

```
>>> from dungeon import Dungeon
>>> map = Dungeon("basic_dungeon.txt")
>>> map.print_map()
S.W.W.S
>>> map.spawn("player_1", some_hero_instance)
>>> map.spawn("player_2", some_orc_instance)
>>> map.print_map()
H.W.W.O
>>> map.move("player_1", "right")
>>> map.move("player_1", "right")
Weapon Equipped
>>> map.move("player_1", "right")
>>> map.move("player_1", "left")
>>> map.move("player_1", "left")
Weapon Equipped
>>> map.move("player_1", "left")
Characters are fighting...
player_1 won!
>>> map.print_map()
...H...
```

## Problem 10 Console input wrapper
So all that classes and functions that you made were tested by unit tests. It is time make a new class called GameInteractor which interacts with you by the console. 

__The idea of this class is to make that game playable. This task is not mandatory! Do it if you have finished everything else!__

You have to implement commands such as:
```
load_map
show_map
spawn_weapons
make_new_hero Bron 100 
move Bron left
show_map
....
```

You don't have to test this class with unittests. Actually you can't test this in an easy way. 
