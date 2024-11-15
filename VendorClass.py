class Vendor:
    def __init__(self,name,fertilizer_cost,feed_cost,salt_cost):
        self.name = name
        self.fertilizer_cost = fertilizer_cost
        self.feed_cost = feed_cost
        self.salt_cost = salt_cost
    
    def display(self):
        print(f"{self.name}: Fertilizer Cost:£{self.fertilizer_cost}/litre \nFeed Cost:£{self.feed_cost}/g \nSalt Cost{self.salt_cost}/g")

# Slippery Lakes £0.30/litre £0.10/g £0.05/g
# Scaly Wholesaler £0.20/litre £0.40/g £0.25/g

Slippery = Vendor('Slippery Lakes',0.30,0.10,0.05)
Scaly = Vendor('Scaly_Wholesaler',0.20,0.40,0.25)

print(Slippery.__dict__)
print(Scaly.__dict__)
Slippery.display()