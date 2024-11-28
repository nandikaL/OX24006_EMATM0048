"""OX24006, Nandika, This file contains the vendor class"""

#Class - vendor
class Vendor:
    """Vendor clas contains these items"""
    def __init__(self,name,fertilizer_cost,feed_cost,salt_cost):
        self.name = name
        self.fertilizer_cost = fertilizer_cost
        self.feed_cost = feed_cost
        self.salt_cost = salt_cost
    
    def display(self):
        """Dislays the vendors nicely for user"""
        print(f"{self.name}: Fertilizer Cost:£{self.fertilizer_cost}/litre \nFeed Cost:£{self.feed_cost}/kg \nSalt Cost{self.salt_cost}/kg")