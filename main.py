import random
from prettytable import PrettyTable

from profession import Profession
from passenger import Passenger
from object import Object, SecretBagGoblet, SecretBagKey

def main():
    professions = []
    passengers = []
    objects = []
    associations = [1, 1, 1, 0, 0, 0]
    associations_map = ["Red", "Blue"]

    # Create all the objects and professions and shuffle them
    for sub_profession in Profession.__subclasses__():
        professions.append(sub_profession())

    for sub_object in Object.__subclasses__():
        if (sub_object.__name__ == "SecretBagKey" or sub_object.__name__ == "SecretBagGoblet"):
            continue
        objects.append(sub_object())

    random.shuffle(professions)
    random.shuffle(objects)
    random.shuffle(associations)

    # Make sure two secret bags within the first five objects
    objects.insert(random.randint(14, 18), SecretBagGoblet())
    objects.insert(random.randint(15, 19), SecretBagKey())

    # Create passengers for players
    for i in range(5):
        passengers.append(Passenger(associations[i], professions[-1], objects[-1]))
        professions.pop()
        objects.pop()

    num_round = 0
    victory = 0
    while(not victory):
        turn = num_round % 5
        print("Now is the choose for passenger: ", (turn + 1))

        print("Status for passengers:")
        status_table = PrettyTable()
        status_table.field_names = ["Passenger", "Association", "Profession", "Number of objects"]
        for i in range(len(passengers)):
            if (i in passengers[turn].association_checked):
                association_temp = associations_map[passengers[i].association]
            else:
                association_temp = "Unknown"
            if (i in passengers[turn].profession_checked):
                profession_temp = passengers[i].profession.get_name()
            else:
                profession_temp = "Unknown"
            status_table.add_row([i + 1, association_temp, profession_temp, passengers[i].num_object()])
        print(status_table)

        print("Your object:")
        object_table = PrettyTable()
        object_table.field_names = ["Index", "Name of Object", "Describe"]
        for i in range(len(passengers[turn].object)):
            object_table.add_row([i + 1, passengers[turn].object[i].get_name(), passengers[turn].object[i].get_describe()])
        print(status_table)

        print("What going to do:\n1 - Trade\n2 - Duel\n3 - Proclaim the victory\n0 - Skip")
        choose = int(input())
        while (choose not in [1, 2, 3, 0]): 
            print("Wrong input, please input again: ")
            choose = int(input())

        if (choose == 1):
            # Trade
            print("You are going to make a trade, who are you want to trade with? ( Please input 1 ~ 5 )")
            passenger_choose = int(input())
            print("What are you want to trade? ( Please input 1 ~", len(passengers[turn].object) + 1, ")")
            object_choose = int(input())

            # This part is for the reciver 
            print("Ask passenger ", passenger_choose, ": \nPassenger", turn, "want to trade with you by", passengers[turn].object[object_choose - 1].get_name(), "Do you agree? [y/n]")
            accept_choose = input()
            trade_choose = 0
            active_choose = "n"
            if (accept_choose == "y"):
                print("Here is what you have, which one do you want to give back?")
                object_table = PrettyTable()
                object_table.field_names = ["Index", "Name of Object", "Describe"]
                for i in range(len(passengers[passenger_choose - 1].object)):
                    object_table.add_row([i + 1, passengers[passenger_choose - 1].object[i].get_name(), passengers[passenger_choose - 1].object[i].get_describe()])
                print(status_table)
                
                trade_choose = int(input())

                print("Do you want to active the object's effect? [y/n]")
                active_choose = input()          
            # Reciver part end
            
            if (accept_choose == "y"):
                print("The passenger accepted your trade, you got: ", passengers[passenger_choose - 1].object[trade_choose - 1].get_name()) 
                if (active_choose == "y"):
                    print("The passenger will active the effect of it")
                    # Active function
                print("Are you going to active your object's effect? [y/n]")
                active_choose = input()
                if (active_choose == "y"):
                    print("You are going to active your object's effect.")
                    # Active function
                passengers[turn].object.append(passengers[passenger_choose - 1].object[trade_choose - 1])       
                passengers[passenger_choose - 1].object.append(passengers[turn].object[object_choose - 1])
                del passengers[turn].object[object_choose - 1]
                del passengers[passenger_choose - 1].object[trade_choose - 1]
                continue
            else:
                print("Your trade request is rejected by the passenger. ")
                continue

        elif (choose == 2):
            # Duel
            print("You are going to duel with someone, who are you want to duel with? ( Please input 1 ~ 5 )")
            passenger_choose = int(input())

            # This part is for public
            print("Passenger", turn + 1, "is going to duel with Passenger", passenger_choose)
            attack = 1
            defend = 1
            for i in range(turn, 5):
                if(i == passenger_choose - 1):
                    continue
                print("Passenger", i, "Who will you fight for? [ 1 - attack; 2 - defend; 0 - give up ]")
                stand_by = int(input())
                if(stand_by == 1):
                    print("Passenger", i, "Will fight for the attacker.")
                    attack += 1
                elif(stand_by == 2):
                    print("Passenger", i, "Will fight for the defender.")
                    defend += 1
                else:
                    print("Passenger", i, "Give up.")
                print("Now the situation is attack:", attack, "; defend:", defend)
            for i in range(0, turn):
                if(i == passenger_choose - 1):
                    continue
                print("Passenger", i, "Who will you fight for? [ 1 - attack; 2 - defend; 0 - give up ]")
                stand_by = int(input())
                if(stand_by == 1):
                    print("Passenger", i, "Will fight for the attacker.")
                    attack += 1
                elif(stand_by == 2):
                    print("Passenger", i, "Will fight for the defender.")
                    defend += 1
                else:
                    print("Passenger", i, "Give up.")
                print("Now the situation is attack:", attack, "; defend:", defend)
            print("Anyone can use your weapons to help them.")
            # TODO: use weapon

            print("The duel result is attack:", attack, "v.s. defend:", defend)
            if (attack > defend):
                print("Attacker WIN! Enjoy your victory!")

                # This part is for the attacker
                print("What are you going to do? [ 0 - Check the association and profession; 1 - Get an object]")
                # TODO: add a check for only one object
                victor_choose = int(input())
                if (victor_choose):
                    print("The passenger's objects are as following")
                    object_table = PrettyTable()
                    object_table.field_names = ["Index", "Name of Object", "Describe"]
                    for i in range(len(passengers[passenger_choose - 1].object)):
                        object_table.add_row([i + 1, passengers[passenger_choose - 1].object[i].get_name(), passengers[passenger_choose - 1].object[i].get_describe()])
                    print(status_table)
                    print("Which one you want to get? [ index ]")
                    rub_choose = int(input())
                    passengers[turn].object.append(passengers[passenger_choose - 1].object[rub_choose - 1])  
                    del passengers[passenger_choose - 1].object[rub_choose - 1]
                else:
                    print("The passenger's association is:", associations_map[passengers[passenger_choose - 1].association])
                    print("The passenger's profession is:", passengers[passenger_choose - 1].profession)
                    passengers[turn].check_association(passenger_choose - 1)
                    passengers[turn].check_profession(passenger_choose - 1)
            elif (attack < defend):
                print("Defender WIN! Enjoy your victory!")
                # This part is for the defender
                # TODO: the same with the formar
            else:
                print("DRAW! The attacker can get a object.")
                passengers[turn].object.append(objects[-1])
                objects.pop()

        elif (choose == 3):
            # Proclaim the victory 
            print("Passenger", turn, "is going to preclaim the victory!")

            # This part is for the passenger turn
            print("Which type of victory do you want to preclaim? [0 - Positive victory; 1 - Negative victory]")
            victory_choose = int(input())
            if (victor_choose):
                # Negative victory
                print("Choose passengers you think they will win: [ index without split ]")
                win_passengers = input()
                



        num_round += 1

#TODO: exchange function
#TODO: rob function
# Declear the public part and passenger part