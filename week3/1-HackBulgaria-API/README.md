#HackBulgaria API

As every nice company we have an API too. https://hackbulgaria.com/api/students/

It returns all the students with their courses, group, github accounts and a boolean filed that shows if they are in the classroom now.

Our task is to make a console application that uses this information. To match students in our classroom in __random__ teams.

To get informations for a remote host we are going to use: http://docs.python-requests.org/en/latest/

## 1. List all courses:

Using the information from the API, list all the courses that are available now.

__Example:__
```
>>> python3 team_matcher.py
Hello, you can use one the the following commands:
list_courses - this lists all the courses that are available now.
match_teams <course_id>, <team_size>, <group_time>

list_courses
Here are the courses:
[1] Programing 101 v2
[2] NodeJS
[3] Android
....

```

__You generate your ids.__

## Match command

Match command takes three arguments __course_id__, __team_size__, __group_time__ (1 or 2) and matches people in a groups of __team_size__ people.

__Example:__
```
>>> python3 team_matcher.py
Hello, you can use one the following commands:
list_courses - this lists all the courses that are available now.
match_teams <course_id>, <team_size>, <group_time>

match_teams 1 2 1
==========
Ivan Ivanov
Peter Ivanov
==========
Viktor Ivanov
Stefan Ivanov
==========
......
```

__match_teams 1 2 1__ This will match teams of people from course 1 (programing 101 v2 for example). Each team will be of 2 people and all of the people will be from the eary group (group_time = 1)
