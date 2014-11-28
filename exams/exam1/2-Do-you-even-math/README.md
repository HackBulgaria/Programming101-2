# Problem to be solved by using SQLAlchemy's ORM

## Guidelines

* Start with the database and first create your classes, that are going to be mapped.
* Add the interface later - when you are OK with the classes and you are sure that they are mapping correctly to the tables.
* Use sqlite
* You can skip the tests for now. [__We are going to make this a spike!__](http://www.extremeprogramming.org/rules/spike.html)
* Experiment with the library and don't be afraid if your program is not working correctly. The given specifications are not that strict!

## The "Do you even math?" game

We are going to implement a dead-simple console game, that asks the user to give the right answer to a random mathematical expression.

__For example:__

```
What is the answer to 6 x 6?
?>36
?>Correct!

What is the answer to 2 ^ 8?
?>10
Incorrect! Ending game. You score is: 1
```

__We want to have the following features:__

* The game can be played by different user. In the beginning, a user can choose his playername to play with
* We want to keep the score for every user that played the game
* We want to be able to display a highscores table, that lists the top 10 users, played this game

__The implementation details are up to you!__

### Calculating the score

We will have a function, that will calculate the score for each player.

The game ends when a player gives a wrong answer to the asked mathematical expression.

If we have `n` consecutive right answers, the final score is calculated by:

```
score(n) = n * n
```

It's just the square of `n`

### Example of playing the game

```
Welcome to the "Do you even math?" game!
Here are your options:
- start
- highscores
?>start

Enter your playername>radorado
Welcome radorado! Let the game begin!

Question #1:
What is the answer to 6 x 6?
?> 36
Correct!

Question #2:
What is the answer to 5 + 1?
?> 6
Correct!

Question #3:
What is the answer to 1 + 1?
?> 3
Incorrect! Ending game. You score is: 4
```

```
?>highscores

This is the current top10:

1. radorado with 4 points
```
