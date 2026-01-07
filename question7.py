""""Q7. Build an Inventory class that:
•	Tracks the total number of items across all inventories.
•	Each instance maintains its own stock dictionary ({"item": quantity}).
•	Provides a method to add or remove stock.
•	Allows updating a minimum stock threshold globally.
•	Offers a static checker to verify if a stock level is below threshold.
Demonstrate:
1.	Managing multiple inventories.
2.	Adjusting stock threshold.
3.	Using static validation inside the instance logic.
"""
class Inventory:
    di={}
    min_stock=2
    def __init__(self,item,quantity):
        self.di[item]=quantity
    @classmethod
    def add(cls,item,quantity):
        Inventory.di[item]=quantity
    @classmethod
    def remove(cls, item):
        Inventory.di.pop(item)
    @classmethod
    def update_min_stock(cls,new_min):
        cls.min_stock=new_min
    @staticmethod
    def check(d):
        if d in Inventory.di:
            return True
        return False

stock=Inventory("soap",6)
stock1=Inventory("Sugar",26)
stock3=Inventory("Milk-Packets",2)
print(Inventory.di)
Inventory.add("SurfExcel",52)
Inventory.remove("soap")
print(Inventory.di)
if Inventory.check("soap"):
    print("In Stock")
else:
    print("Not in Stock")