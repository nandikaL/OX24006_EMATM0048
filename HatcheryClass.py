
class Hatchery:
    def __init__(self,supplies,cash):
        self.supplies = supplies
        
        self.cash = cash
        
        self.current_techs = []

        self.quarterly_payment = 1500

        #self.tech_info = self.Technician()

    
    class Technician:
        # weeks_work = 9 
        # weeks_pay = 500
        # weeks_total = 12 #can adjsut weeks theyre paid for then
        # day_week = 7
        # total_pay = weeks_pay * weeks_total
        # labourdays = weeks_total * day_week

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
        for tech in self.current_techs:
            print(f'Hired:{tech.name},They will work {tech.labourdays} days this quarter. Pay:£{tech.total_pay}')
    
    def Tech_names(self):
        if not self.current_techs:
            print('No Techincians Hired Yet')
        else:
            for tech in self.current_techs:
                print(f'Hired:{tech.name},Pay:£{tech.total_pay}')
            
    
    def Tech_Roster(self):
        print('First, lets pick your Techs! Current Technicians:')
        self.Tech_names()
        print('Please choose how many technicians you would like to add or remove')
        print('To add, please type a positive number. Example: To add 2, type 2')
        print('To remove, please type a negative number. Example: To remove 2, type -2')
        print('For no change type 0')
        print('Please note, there must be between 1 to 5 technicians')  

        while True:
            try: 
                num = int(input().strip())
                if num == 0 or num > 0 or num < 0:
                    break
                else:
                    print('Type a number!!')
            except ValueError:
                print('Please enter a valid number')

        total = (num+len(self.current_techs))
        
        if total < 1:
            print(f'There must be at least 1 technician If you remove {num} technicians, there will be {total}')
            return self.Tech_Roster()
        
        elif total > 5:
            print(f'There cannot be more than 5 technicians. If you add {num} technicians, there will be {total}')
            return self.Tech_Roster()
        
        else:
            
            if num == 0:
                print("No changes made")
            
            elif num > 0:
                while num > 0:
                    print('Please enter the name of the tech you want to hire:')
                    print('If more than one please enter one name at a time.')
                    new_tech = input().strip().lower()
                    if any(tech.name == new_tech for tech in self.current_techs):
                        print('We already hired them')
                    else:
                        print("Does this Technician have a specialization?")
                        print("[0] for None \n[1] for Clef Fins \n[2] for Timpani Snapper \n[3] for Andalusian Brim \n[4] for Plagal Cod \n[5] for Fugue Flounder \n[6] for Modal Bass")
                        print("A specialized tech can maintain their fish at 2/3 the time ")
                        while True:
                            try: 
                                tech_spec = int(input().strip())
                                if tech_spec == 0:
                                    print('No specialization')
                                    print(f"{new_tech} Hired!")
                                    new_tech_cl = self.Technician(new_tech,'0') #9x5 days
                                    self.current_techs.append(new_tech_cl)
                                    break
                                elif tech_spec == 1:
                                    print(f"{new_tech} Hired!")
                                    new_tech_cl = self.Technician(new_tech,'Clef Fins') #45?
                                    self.current_techs.append(new_tech_cl)
                                    break
                                elif tech_spec == 2: 
                                    print(f"{new_tech} Hired!")
                                    new_tech_cl = self.Technician(new_tech,'Timpani Snapper') #45?
                                    self.current_techs.append(new_tech_cl)
                                    break
                                elif tech_spec == 3:
                                    print(f"{new_tech} Hired!")
                                    new_tech_cl = self.Technician(new_tech,'Andalusian Brim') #45?
                                    self.current_techs.append(new_tech_cl)
                                    break
                                elif tech_spec == 4:
                                    print(f"{new_tech} Hired!")
                                    new_tech_cl = self.Technician(new_tech,'Plagal Cod') #45?
                                    self.current_techs.append(new_tech_cl)
                                    break
                                elif tech_spec == 5:
                                    print(f"{new_tech} Hired!")
                                    new_tech_cl = self.Technician(new_tech,'Fugue Flounder') #45?
                                    self.current_techs.append(new_tech_cl)
                                    break
                                elif tech_spec == 6:
                                    print(f"{new_tech} Hired!")
                                    new_tech_cl = self.Technician(new_tech,'Modal Bass') #45?
                                    self.current_techs.append(new_tech_cl)
                                    break
                                else:
                                    print('Please enter a valid number 0-6')
                            except ValueError:
                                print('Please enter a valid number')
                    num -= 1
            
                        
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
    