
#Initiate the hatchery class
class Hatchery:
    """define the items inside - this to be initialized to play"""
    def __init__(self,supplies,cash):
        self.supplies = supplies
        
        self.cash = cash
        
        self.current_techs = []

        self.quarterly_payment = 1500

        #self.tech_info = self.Technician()

    #within it, technician class
    class Technician:
        """define the items inside the technician class"""
        def __init__(self,name,specialty):
            self.name = name
            self.specialty = specialty #specialty
            self.weeks_work = 9 
            self.weeks_pay = 500
            self.weeks_total = 12 #can adjsut weeks theyre paid for then
            self.day_week = 5
            self.total_pay = self.weeks_pay * self.weeks_total
            self.labourdays = self.weeks_work * self.day_week 
            self.labourtime = self.labourdays #ammendable time
    
    
    def Tech_display(self):
        """displaying the technicians for when they are hired """
        for tech in self.current_techs:
            print(f'Hired:{tech.name},They will work {tech.labourdays} days this quarter. Pay:£{tech.total_pay}')
    
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

        #checks for total number of techs there currently
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
                while num > 0:
                    #Let user know they may enter names one at a time
                    print('Please enter the name of the tech you want to hire:')
                    print('If more than one please enter one name at a time.')
                    #take in technician name, apply strip and lower to make it uniform
                    new_tech = input().strip().lower()
                    #check if tech is already hired or not.
                    #if hired:
                    if any(tech.name == new_tech for tech in self.current_techs):
                        #tell user they have already been hired, function will loop back
                        print('We already hired them')
                    #if tech is new: specialization
                    else:
                        #Ask about specialization
                        print("Does this Technician have a specialization?")
                        #numerical entry 
                        print("[0] for None \n[1] for Clef Fins \n[2] for Timpani Snapper \n[3] for Andalusian Brim \n[4] for Plagal Cod \n[5] for Fugue Flounder \n[6] for Modal Bass")
                        print("A specialized tech can maintain their fish at 2/3 the time ")
                        while True:
                            #try-except error handling
                            try: 
                                tech_spec = int(input().strip())
                                # if specialization = 0, user does not want to specialize
                                if tech_spec == 0:
                                    #let user know their choice not to specialize
                                    print('No specialization')
                                    #let user know who theyve hired
                                    print(f"{new_tech} Hired!")
                                    #initialize the technician into the Technician class
                                    #using its name, and specialization, 0 here for none
                                    new_tech_cl = self.Technician(new_tech,'0') 
                                    #add this instance into a list of instances. 
                                    #this will be how current techs are tracked
                                    self.current_techs.append(new_tech_cl)
                                    break
                                elif tech_spec == 1:
                                    #let user know who theyve hired
                                    print(f"{new_tech} Hired!")
                                    #initialize the technician into the Technician class
                                    #using its name, and specialization, 1 for clef fin
                                    new_tech_cl = self.Technician(new_tech,'Clef Fins') 
                                    #add this instance into a list of instances. 
                                    #this will be how current techs are tracked
                                    self.current_techs.append(new_tech_cl)
                                    break
                                elif tech_spec == 2: 
                                    print(f"{new_tech} Hired!")
                                    #initialize the technician into the Technician class
                                    #using its name, and specialization, 2 for Timpani Snapper
                                    new_tech_cl = self.Technician(new_tech,'Timpani Snapper') 
                                    #add this instance into a list of instances. 
                                    #this will be how current techs are tracked
                                    self.current_techs.append(new_tech_cl)
                                    break
                                elif tech_spec == 3:
                                    print(f"{new_tech} Hired!")
                                    #initialize the technician into the Technician class
                                    #using its name, and specialization, 
                                    new_tech_cl = self.Technician(new_tech,'Andalusian Brim') 
                                    self.current_techs.append(new_tech_cl)
                                    break
                                elif tech_spec == 4:
                                    print(f"{new_tech} Hired!")
                                    #initialize the technician into the Technician class
                                    #using its name, and specialization, 
                                    new_tech_cl = self.Technician(new_tech,'Plagal Cod') 
                                    #add this instance into a list of instances. 
                                    #this will be how current techs are tracked
                                    self.current_techs.append(new_tech_cl)
                                    break
                                elif tech_spec == 5:
                                    print(f"{new_tech} Hired!")
                                    #initialize the technician into the Technician class
                                    #using its name, and specialization, 
                                    new_tech_cl = self.Technician(new_tech,'Fugue Flounder') 
                                    #add this instance into a list of instances. 
                                    #this will be how current techs are tracked
                                    self.current_techs.append(new_tech_cl)
                                    break
                                elif tech_spec == 6:
                                    print(f"{new_tech} Hired!")
                                    #initialize the technician into the Technician class
                                    #using its name, and specialization, 
                                    new_tech_cl = self.Technician(new_tech,'Modal Bass') 
                                    #add this instance into a list of instances. 
                                    #this will be how current techs are tracked
                                    self.current_techs.append(new_tech_cl)
                                    break
                                #if the number is not within 0-6, tell user to do so
                                else:
                                    print('Please enter a valid number 0-6')
                            #if non-integer, loops back
                            except ValueError: 
                                print('Please enter a valid number')
                    #remove 1 from the number so that the while loop will end after the desired loops
                    num -= 1
            
             #if the user types negative, they want to fire a tech            
            elif num < 0:
                
                #same while loop but for negative
                while num < 0:
                    #tell user what to do
                    print('Please enter the name of the tech you want to fire:')
                    print('If more than one please enter one name at a time.')
                    #strip an lower to modify input taken in
                    fire_tech = input().strip().lower()
                    #initialize the variable
                    tech_to_remove = None
                    #loop through the list of techs to see if this tech has been hired
                    for tech in self.current_techs:
                        #if the name matches, this tech is there
                        if tech.name == fire_tech:
                            #assign tech to tech to remove
                            tech_to_remove = tech
                            break
                    #if tech to remove exists, remove from the list
                    if tech_to_remove:
                        #remove from list
                        self.current_techs.remove(tech_to_remove)
                        #allow user to know whats happened
                        print(f"{fire_tech} Fired!")
                        #add one so that when it gets to 0, loop will break
                        num += 1
                    else:
                        #if user typed the wrong name, let them know
                        print('We never hired this stranger')
            else:
                print('Invalid response')
    
    def Tech_Again(self):
        """simple if else to allow user to make changes to the technicians"""
        #as user if they want to make changes
        print('Do you want to make any more changes? Please type [1] for Yes and [2] for No')
        #only 1 and 2 options, will leave as string
        #strip trailing spaces
        ans = input().strip()
        #if 1, go back to tech roster
        if ans == '1':
            self.Tech_Roster()
        #if 2, exit
        elif ans == '2':
            return
        #is user types something else, repeat
        else:
            print('I do not understand.')
            self.Tech_Again()
    