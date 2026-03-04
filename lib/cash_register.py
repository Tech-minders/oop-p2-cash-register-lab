#!/usr/bin/env python3

class CashRegister:
    #Simulates a cash register for an e-commerce site.

    def __init__(self, discount=0):
        #Initialize the cash register.
      
        self._discount = 0
        self.discount = discount  # Use setter for validation
        self.total = 0
        self.items = []
        self.previous_transactions = []

    @property
    def discount(self):
        #Get the current discount percentage.
        return self._discount

    @discount.setter
    def discount(self, value):
        #Set and validate the discount percentage.
       
        if isinstance(value, int) and 0 <= value <= 100:
            self._discount = value
        else:
            print("Not valid discount")

    def add_item(self, item, price, quantity=1):
        #Add an item to the register.
        # Add the item name once per unit to the items list
        self.items.extend([item] * quantity)

        # Calculate the total cost for this transaction
        transaction_total = price * quantity

        # Update the running total
        self.total += transaction_total

        # Record this transaction so it can be voided later
        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity,
            "transaction_total": transaction_total
        })

    def apply_discount(self):
        #Apply the discount percentage to the current total.
      
        if self.discount == 0:
            print("There is no discount to apply.")
            return

        # Calculate and apply the discount
        discount_amount = self.total * (self.discount / 100)
        self.total = self.total - discount_amount

        print(f"After the discount, the total comes to ${self.total:.0f}.")

    def void_last_transaction(self):
        #Remove the last transaction from the register.
        
        if not self.previous_transactions:
            return

        # Get the last transaction
        last = self.previous_transactions.pop()

        # Subtract its cost from the total
        self.total -= last["transaction_total"]

        # Round to avoid floating point drift
        self.total = round(self.total, 2)

        # Remove its items from the items list
        for _ in range(last["quantity"]):
            if last["item"] in self.items:
                self.items.remove(last["item"])
