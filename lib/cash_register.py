#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount   # discount in %
        self.total = 0
        self.items = []
        self.last_transaction_amount = 0  # track last transaction amount for voiding

    def add_item(self, title, price, quantity=1):
        """Adds an item and updates the total"""
        transaction_amount = price * quantity
        self.total += transaction_amount
        self.items.extend([title] * quantity)
        self.last_transaction_amount = transaction_amount

    def apply_discount(self):
        """Applies discount and prints result"""
        if self.discount > 0:
            discount_amount = self.total * (self.discount / 100)
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        """Removes the last transaction"""
        self.total -= self.last_transaction_amount

   
        
  

   

