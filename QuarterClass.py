###remember to change all the quaters to QUARTER with and R. RRRRRR.
#### also reminder to edit and convert all the units afterwards 

from FishClass import Fish
from WarehouseClass import Warehouse
from TechicianClass import Technician
from VendorClass import Vendor
from HatcheryClass import Hatchery

class Quarter:
    current_stock_dict = {'maint_time':0, 'fert':0, 'feed':0, 'salt':0, 'cash':10000}

    def Current_stocks():
        Quarter.Current_stock_dict['maint_time']=len(Hatchery.current_techs)*45 #45 days of work per person

        #Adding sum of items in the warehouse 
        Quarter.current_stock_dict['fert'] = sum(Warehouse.Fert)
        Quarter.current_stock_dict['feed'] = sum(Warehouse.Feed)
        Quarter.current_stock_dict['salt'] = sum(Warehouse.Salt)

        #does anything happen with cash here?
    

    def deplete_stocks(fishy):
        
        for fish in fishy: 

            demand = Fish.demand
            
            fert_need = Fish.fertilizer * demand
            feed_need = Fish.feed * demand
            salt_need = Fish.salt * demand
            maint_need = Fish.maintenance_time * demand

            if Quarter.current_stock_dict['fert'] >= fert_need:
                print(f"{fish.species}: {fert_need}ml fertilizer used.")
            else:
                print(f"Not enough fertilizer for {fish.species}. {fert_need}ml needed, only {Quarter.current_stock_dict['fert']}ml available.")
                continue

            if Quarter.current_stock_dict['feed'] >= feed_need:
                print(f"{fish.species}: {feed_need}kg feed used.")
            else:
                print(f"Not enough feed for {fish.species}. {feed_need}kg needed, only {Quarter.current_stock_dict['feed']}kg available.")
                continue

            if Quarter.current_stock_dict['salt'] >= salt_need:
                print(f"{fish.species}: {salt_need}kg salt used.")
            else:
                print(f"Not enough salt for {fish.species}. {salt_need}kg needed, only {Quarter.current_stock_dict['salt']}kg available.")
                continue
            #####Maintenence 
            if Quarter.current_stock_dict['maint_time']>=maint_need:
                print(f"{maint_need} days of work taken")
            else:
                print(f"Not enough labour for {fish.species}. {maint_need} required, only {Quarter.current_stock_dict['maint_time']} available")
                continue

            new_fert_value = Quarter.current_stock_dict['fert'] - fert_need
            Quarter.current_stock_dict['fert'] = (new_fert_value)
            new_feed_value=Quarter.current_stock_dict['feed'] - feed_need
            Quarter.current_stock_dict['feed'] = (new_feed_value)
            new_salt_value= Quarter.current_stock_dict['salt'] - salt_need
            Quarter.current_stock_dict['salt'] = (new_salt_value)
            new_maint_value = Quarter.current_stock_dict['maint_time']-maint_need
            Quarter.current_stock_dict['maint_time'] = (new_maint_value)

            ##add money
            fish_rev = Fish.Price * demand 
            add_rev = Quarter.current_stock_dict['cash']+fish_rev
            Quarter.current_stock_dict['cash']+fish_rev

    #ok so: fish have fert, feed, salt
    #1st type of fish: input number being sold:
    #function loop starts: number of fish * fert 
    #if enough fert in warehouses, move to next item, feed. 
    #if enough feed in warehouses, move to next item 
    #if enough salt in warehouses, move to next item
    #must meet all variables before continue
    #then  do labour
    #the append everything
    #loopy loop
    

    def payments():
        standard = 1500
        tech_payments = len(Hatchery.current_techs)*4500 #500 mulitpled by 9 weeks
        depreciation_fert = Quarter.current_stock_dict['fert']-(Quarter.current_stock_dict['fert']*Warehouse.fertilizer_depreciation) #leftover-(leftover*fish.species.depreciation)
        depreciation_feed = Quarter.current_stock_dict['feed']-(Quarter.current_stock_dict['feed']*Warehouse.fertilizer_depreciation)
        depreciation_salt = Quarter.current_stock_dict['salt']-(Quarter.current_stock_dict['salt']*Warehouse.fertilizer_depreciation)
        total_depreciation = depreciation_fert + depreciation_feed + depreciation_salt
        #can i loop this through the classes?? 
        warehouse_fert = Quarter.current_stock_dict['fert']*Warehouse.fertilizer_warehouse 
        warehouse_feed = Quarter.current_stock_dict['fed']*Warehouse.feed_warehouse
        warehouse_salt = Quarter.current_stock_dict['salt']*Warehouse.salt_warehouse #leftover x fish.species.warehousecost
        #can be looped?? 
        total_warehouse = warehouse_fert + warehouse_feed + warehouse_salt
        total_payments = standard + tech_payments + total_depreciation + total_warehouse
        print(f"Quarterly warehouse fees: £{standard}\nTotal Technician Salary: £{tech_payments}\nTotal Depreciation: £{total_depreciation}\nTotal Warehouse Costs: £{total_warehouse}")
        
        new_cash_value = Quarter.current_stock_dict['cash'] - total_payments
        Quarter.current_stock_dict['cash'] = new_cash_value
        #loop through the current stocks dictionary to find the remaining supplies 