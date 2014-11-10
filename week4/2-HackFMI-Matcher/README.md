# HackFMI Matcher

HackFMI 0100 is coming soon. So our friend RadoRado needs some help to match teams with mentors.

## 1. Load mentors.

[We have a GitHub markdown file full of mentors.](https://github.com/Hackfmi/HackFMI-4/blob/master/mentors.md) Your task is to load that file and parse the names of the mentors.

## 2. Load teams and their choices.

Your console program should take an .csv file with teams and their choices. Every team can only choose up to 5 mentors.

Team | ChoiceOne | ChoiceTwo | ChoiceThree | ChoiceFour | ChoiceFive | ApplicationTime
--- | --- | --- | --- | --- | --- | ---
__TeamPanda__ | Тихомир Томов | Иван Атанасов | Божидар „Bave” Грозданов | Полина Атанасова | RadoRado | 08.11.2014 20:19

....

The hair you place your mentor the more you want him. It is like choosing your specialty after 12th grade.

## 3. List mentors with their teams.

A mentor can go to maximum 5 teams. Select the 5 teams that want him the most. 

__Example:__
```
>>>Иван Атанасов
-- TeamPanda
-- TeamRaper
-- TeamMain
-- HackTeam
-- TeamBlqq
>>>Иван Иванов
-- .....
```
