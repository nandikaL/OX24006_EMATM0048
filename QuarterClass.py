from FishClass import Fish
from WarehouseClass import Warehouse
from TechicianClass import Technician
from VendorClass import Vendor
from HatcheryClass import Hatchery

class Quarter:
    current_stock_dict = {'maint_time':0, 'fert':0, 'feed':0, 'salt':0, 'cash':0}

    def Current_stocks():
        Quarter.Current_stock_dict['maint_time']=len(Hatchery.current_techs)*45 #45 days of work per person

        #Adding sum of items in the warehouse 
        Quarter.current_stock_dict['feed'] = sum(Warehouse.Fert)
        Quarter.current_stock_dict['feed'] = sum(Warehouse.Feed)
        Quarter.current_stock_dict['feed'] = sum(Warehouse.Salt)
    

    def deplete_stocks():
    #ok so: fish have fert, feed, salt
    #1st type of fish: input number being sold:
    #function loop starts: number of fish * fert 
    #if enough fert in warehouses, move to next item, feed. 
    #if enough feed in warehouses, move to next item 
    #if enough salt in warehouses, move to next item
        pass
    
    def payments():
        standard = 1500
        tech_payments = len(Hatchery.current_techs)*4500 #500 mulitpled by 9 weeks 