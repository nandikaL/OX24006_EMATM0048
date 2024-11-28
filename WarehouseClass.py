"""OX24006, Nandika, This file contains the warehouse class"""

#Class - warehouse
class Warehouse:
    """Class contains these items"""
    def __init__(self, warehouse, fert_amount,fertilizer_capacity,feed_amount,feed_capacity,salt_amount,salt_capacity):
        self.warehouse = warehouse
        self.fert_amount = fert_amount
        self.fertilizer_capacity = fertilizer_capacity
        self.feed_amount = feed_amount
        self.feed_capacity = feed_capacity
        self.salt_amount = salt_amount
        self.salt_capacity = salt_capacity
        #contains self.warehouse_costs also
        self.costs = self.Warehouse_Costs()
      

    class Warehouse_Costs:
        #contains the parts of the warehouse costs that stay constant
        def __init__(self):
            self.fertilizer_depreciation = 0.4
            self.feed_depreciation = 0.1
            self.salt_depreciation = 0.0
            self.fertilizer_warehouse = 0.1 #liters
            self.feed_warehouse = 0.001 #pounds per gram
            self.salt_warehouse = 0.001 #pounds per gram
