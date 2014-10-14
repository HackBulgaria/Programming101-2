# Python OOP problems set

## Cash_desk - problem

### 1. Make a simple class called Cash_desk that takes no arguments.

When you initialize your object it should create an empty dictionary that holds all kinds of note that exists: 
```python
self.money = {100:0, 50:0, 20:0, 10:, 5:0, 2:0, 1:0}
```
__ We don't use coins in our cash desk.

Interface:
```python
my_cash_desk = Cash_desk()
```

### 2. take_money function
Implement a function called ``take_money()`` that takes one argument. That argument is a dictionary which contains notes that you take and amount of them. 

Interface:
```python
my_cash_desk.take_money({1:2, 50:1, 20:1})
```

### 3. total() function
Implement a function called ``total()`` that takes no arguments. It returns an integer with the total amount of money that we have.

Interface:
```python
my_cash_desk = Cash_desk()
my_cash_desk.take_money({1:2, 50:1, 20:1})
my_cach_desk.total() # 72
```

### can_withdraw_money() function
Implement a function called ``can_withdraw_money(amount_of_money)`` that takes one argument. That argument is an integer that holds an amount of money that you should try to withdraw.

This function only returns True or False and it __does not__ withdraws any money.

Interface:
```python
my_cash_desk = Cash_desk()
my_cash_desk.take_money({1:2, 50:1, 20:1})
my_cach_desk.total() # 72
my_cach_desk.can_withdraw_money(30) #False
my_cach_desk.can_withdraw_money(70) #True
```
