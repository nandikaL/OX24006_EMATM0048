"""OX24006, Nandika, This file contains the hatchery class", the technicans are handed here and moving information is stored here """
#define class
class Hatchery:
    def __init__(self,supplies,cash):
        """define the items inside - this to be initialized to play"""
        self.supplies = supplies
        
        self.cash = cash
        
        self.current_techs = []

        self.quarterly_payment = 1500

        #self.tech_info = self.Technician()

    #within it, technician class
    class Technician:
        """define the items inside the technician class"""
        def __init__(self,name):
            self.name = name
            self.weeks_work = 9 
            self.weeks_pay = 500
            self.weeks_total = 12 #can adjsut weeks theyre paid for then
            self.day_week = 5
            self.total_pay = self.weeks_pay * self.weeks_total
            self.labourdays = self.weeks_work * self.day_week
    
    def Tech_display(self):
        """displaying the technicians for when they are hired """
        for tech in self.current_techs:
            print(f'Hired:{tech.name},They will work {tech.labourdays} this quarter. Pay:£{tech.total_pay}')
    
    def Tech_names(self):
        """display at the start of quarter"""
        if not self.current_techs:
            print('No Techincians Hired Yet')
        else:
            for tech in self.current_techs:
                print(f'Hired:{tech.name},Pay:£{tech.total_pay}')
            
    
    def Tech_Roster(self):
        """To hire technicians and add them into technician list"""
        #Tell user what is happening
        print('First, lets pick your Techs! Current Technicians:')
        #Let user know who is hired right now
        self.Tech_names()
        #Let user know the rules 
        print('Please choose how many technicians you would like to add or remove')
        print('To add, please type a positive number. Example: To add 2, type 2')
        print('To remove, please type a negative number. Example: To remove 2, type -2')
        print('For no change type 0')
        print('Please note, there must be between 1 to 5 technicians') 
        
        #error handling
        while True:
            try: 
                #if the value is an integer, break loop
                num = int(input().strip())
                if num == 0 or num > 0 or num < 0:
                    break
                #else, reminds user to type a number
                else:
                    print('Type a number!!')
            except ValueError:
                print('Please enter a valid number')

         #checks for total number of techs there currentl
        total = (num+len(self.current_techs))
        
        #if there is not even 1 present, repeat function
        if total < 1:
            print(f'There must be at least 1 technician If you remove {num} technicians, there will be {total}')
            return self.Tech_Roster()
        
        #if there are more than 5, repeat function
        elif total > 5:
            print(f'There cannot be more than 5 technicians. If you add {num} technicians, there will be {total}')
            return self.Tech_Roster()
        
        #else statement: if the number is acceptable
        else:
            
            #user is allowed to not change anything
            if num == 0:
                print("No changes made")
            
            #if above 1, asks user who they want to hire
            elif num > 0:
                #loop as long as num is positive
                while num > 0:
                    #Let user know they may enter names one at a time
                    print('Please enter the name of the tech you want to hire:')
                    print('If more than one please enter one name at a time.')
                    new_tech = input().strip().lower()
                    if any(tech.name == new_tech for tech in self.current_techs):
                        print('We already hired them')
                    else:
                        num -= 1
                        print(f"{new_tech} Hired!")
                        new_tech = self.Technician(new_tech)
                        self.current_techs.append(new_tech)
                        
            elif num < 0:
                
                while num < 0:
                    print('Please enter the name of the tech you want to fire:')
                    print('If more than one please enter one name at a time.')
                    fire_tech = input().strip().lower()
                    tech_to_remove = None
                    for tech in self.current_techs:
                        if tech.name == fire_tech:
                            tech_to_remove = tech
                            break
                    if tech_to_remove:
                        self.current_techs.remove(tech_to_remove)
                        print(f"{fire_tech} Fired!")
                        num += 1
                    else:
                        print('We never hired this stranger')
            else:
                print('Invalid response')
    
    def Tech_Again(self):
        print('Do you want to make any more changes? Please type [1] for Yes and [2] for No')
        ans = input().strip()
        if ans == '1':
            self.Tech_Roster()
        elif ans == '2':
            return
        else:
            print('I do not understand.')
            self.Tech_Again()
    