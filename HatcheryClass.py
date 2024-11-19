from TechicianClass import Technician

class Hatchery:
    def __init__(self,supplies,cash,techs):
        self.supplies = supplies
        self.cash = cash
        self.techs = techs
        self.current_techs = []

    def tech_display(self):
        for item in self.current_techs:
            print(f'Hired:{item},Pay:£{self.pay}')
    
    def Tech_Roster(self):
        print('Please choose how many technicians you would like to add or remove')
        print('To add, please type a positive number. Example: To add 2, type 2')
        print('To remove, please type a negative number. Example: To remove 2, type -2')
        print('For no change type 0')
        print('Please note, there must be between 1 to 5 technicians')  
        print('Current Technicians:')
        print(self.current_techs)
        num = int(input().strip())
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
                print(self.current_techs)
            elif num > 0:
                while num > 0:
                    print('Please enter the name of the tech you want to hire:')
                    print('If more than one please enter one name at a time.')
                    new_tech = input().strip().lower()
                    if new_tech in self.current_techs:
                        print('We already hired them')
                    else:
                        num -= 1
                        self.current_techs.append(new_tech)
                        new_tech = Technician(new_tech)
                        print(self.current_techs)
            elif num < 0:
                while num < 0:
                    print('Please enter the name of the tech you want to fire:')
                    print('If more than one please enter one name at a time.')
                    fire_tech = input().strip().lower()
                    if fire_tech in self.current_techs:
                        self.current_techs.remove(fire_tech)
                        num += 1
                    else:
                        print('We never hired this stranger')
            else:
                print('Invalid response')
    
    def Tech_Again(self):
        print('Do you want to make any more changes? Please type [1] for Yes and [2] for No')
        ans = int(input().strip().lower())
        if ans == 1:
            self.Tech_Roster()
        elif ans == 2:
            return
        else:
            print('I do not understand.')
            self.Tech_Again()
    