class Warehouse:
    def __init__(self, warehouse, fert_amount,fertilizer_capacity,feed_amount,feed_capacity,salt_amount,salt_capacity):
        self.warehouse = warehouse
        self.fert_amount = fert_amount
        self.fertilizer_capacity = fertilizer_capacity
        self.feed_amount = feed_amount
        self.feed_capacity = feed_capacity
        self.salt_amount = salt_amount
        self.salt_capacity = salt_capacity
        self.costs = self.Warehouse_Costs()
        # self.fertilizer_depreciation = 0.4
        # self.feed_depreciation = 0.1
        # self.salt_depreciation = 0.0
        # self.fertilizer_warehouse = 0.1 
        # self.feed_warehouse = 0.001
        # self.salt_warehouse = 0.001

    class Warehouse_Costs:
        def __init__(self):
            self.fertilizer_depreciation = 0.4
            self.feed_depreciation = 0.1
            self.salt_depreciation = 0.0
            self.fertilizer_warehouse = 0.1 #liters
            self.feed_warehouse = 0.001 #pounds per gram
            self.salt_warehouse = 0.001 #pounds per gram
#depreciation = cost x remainder