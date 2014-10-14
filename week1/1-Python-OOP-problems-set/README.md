# Python OOP problems set

## Cash_desk - problem
### 1. Make a simple class called Cash_desk that takes no arguments.

When you initialize your object it should create an empty dictionary that holds all kinds of note that exists: 
```python
self.money = {100:0, 50:0, 20:0, 10:, 5:0, 2:0, 1:0}
```
__ We don't use coins in our cash desk.__

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
https://www.youtube.com/watch?v=HIjU31bM2l0
Interface:
```python
my_cash_desk = Cash_desk()
my_cash_desk.take_money({1:2, 50:1, 20:1})
my_cach_desk.total() # 72
```

### 4. can_withdraw_money() function
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

## Laptop.bg - problem
### 1. Make a simple class called Product
Every product must have a name, stock_price and final_price.

Interface:
```python
new_product = Product('HP HackBook', 1000, 1243)
```

### 2. profit() function

Every product must have a profit function that returns the profit of every product.

Interface:
```python
new_product = Product('HP HackBook', 1000, 1243)
new_product.profit() # 243
```

### 3. Make a simple Laptop class
Every laptop object is like a normal product but it has diskspace and RAM. This class must inherit product class.

Interface:
```python
new_laptop = Laptop('HP HackBook', 1000, 1243, 1000, 4)
```

### 4. Make a simple Smartphone class
Every smartphone object is like a normal product but it has display_size and mega_pixels. This class must inherit product class too.

Interface:
```python
new_smarthphone = Smartphone('Hack Phone', 500, 820, 7, 10)
```

### 5. Make a simple Store class
Every store has just a name.

Interface:
```python
new_store = Store('Laptop.bg')
```

### 6. load_new_products function
Implement a function called load_new_products(product, count) that takes two arguments product and count. The first argument 'product' must be an instance of some kind of product. The next argument 'count' must be the amount of this products that you load into the store.

Interface:
```python
new_smarthphone = Smartphone('Hack Phone', 500, 820, 7, 10)
new_store = Store('Laptop.bg')
new_store.load_new_products(new_smarthphone, 20)
```

### 6. list_products function
Implement a function called list_products(product_class). It takes one argument: product_class which is a class __not an object__. This function prints all of the products of a given class with the amount of each.

Interface:
```python
store = Store('Laptop.bg')
smarthphone = Smartphone('Hack Phone', 500, 820, 7, 10)
laptop = Laptop('HP HackBook', 1000, 1243, 1000, 4)
store.load_new_products(smarthphone, 20)
store.load_new_products(laptop, 10)

store.list_products(Laptop) # HP HackBook - 10
```

### 7. sell_product function
Implement a function called sell_product(product). It takes one argument and that is the the product that you want to sell. It this product is not in stock then return False else return True.


Interface:
```python
store = Store('Laptop.bg')
smarthphone = Smartphone('Hack Phone', 500, 820, 7, 10)
store.load_new_products(smarthphone, 2)
store.sell_product(smarthphone) # True
store.sell_product(smarthphone) # True
store.sell_product(smarthphone) # False
```


### 8. total_income function
Implement a function called total_income(). It takes no arguments. It returns the amount of money that our store has earn. Use __profit()__ function of every sold product.

Interface:
```python
store = Store('Laptop.bg')
smarthphone = Smartphone('Hack Phone', 500, 820, 7, 10)
store.load_new_products(smarthphone, 2)
store.sell_product(smarthphone) # True
store.sell_product(smarthphone) # True

store.total_income() # 640
```