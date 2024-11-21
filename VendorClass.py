class Vendor:
    def __init__(self,name,fertilizer_cost,feed_cost,salt_cost):
        self.name = name
        self.fertilizer_cost = fertilizer_cost
        self.feed_cost = feed_cost
        self.salt_cost = salt_cost
    
    def display(self):
        print(f"{self.name}: Fertilizer Cost:£{self.fertilizer_cost}/litre \nFeed Cost:£{self.feed_cost}/kg \nSalt Cost{self.salt_cost}/kg")