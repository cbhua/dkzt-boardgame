import random
from prettytable import PrettyTable
from profession import Profession
from passenger import Passenger
from object import Object, SecretBagGoblet, SecretBagKey


def game_initialization():
    passengers = []
    associations = [1, 1, 1, 0, 0, 0]
    professions = []
    objects = []

    for sub_profession in Profession.__subclasses__(): # Create professions
        professions.append(sub_profession())
    for sub_object in Object.__subclasses__(): # Create objects
        if (sub_object.__name__ == 'SecretBagKey' or sub_object.__name__ == 'SecretBagGoblet'): # Skip the Golbet bag and Key bag
            continue
        objects.append(sub_object())

    random.shuffle(associations)
    random.shuffle(professions)
    random.shuffle(objects)

    objects.insert(random.randint(14, 18), SecretBagGoblet())
    objects.insert(random.randint(15, 19), SecretBagKey())

    for i in range(5): # Create passengers
        new_passenger = Passenger(i, associations[i], professions[-1], objects[-1])
        passengers.append(new_passenger)
        professions.pop()
        objects.pop()

    return passengers, associations, professions, objects


def show_status(turn, passengers):
    status_table = PrettyTable()
    status_table.title = 'Status for Passengers'
    status_table.field_names = ['Passenger', 'Association', 'Profession', 'Number of objects']

    for i in range(len(passengers)):
        if (i in passengers[turn].association_checked):
            association_temp = 'Red' if passengers[i].association == 0 else 'Blue'
        else:
            association_temp = 'Unknown'
        if (i in passengers[turn].profession_checked):
            profession_temp = passengers[i].profession.get_name()
        else:
            profession_temp = 'Unknown'
        status_table.add_row([i + 1, association_temp, profession_temp, passengers[i].num_object()])

    print(status_table)


def show_objects(passenger):
    object_table = PrettyTable()
    object_table.title = 'Your Objects'
    object_table.field_names = ['Index', 'Name of Object', 'Describe']

    for i in range(len(passenger.object)):
        object_table.add_row([i + 1, passenger.object[i].get_name(), passenger.object[i].get_description()])
    
    print(object_table)


def input_check(input_content, input_space):
    while (input_content not in input_space):
        print("Wrong input, please input again.")
        input_content = input()
    return input_content


def trade_initiate():
    print('You are going to make a trade, who are you want to trade with? [Passenger Number]')
    passenger_choose = int(input())
    print('Which object are you going to trade? [Object Number]')
    object_choose = int(input())
    return passenger_choose, object_choose

def trade_query(turn, passenger_choose, passengers):
    print('[Ask passenger', passenger_choose, '] \nPassenger', turn + 1, 'want to trade with you by', passengers[turn].object[object_choose - 1].get_name(), '.Do you agree? [y/n]')
    trade_accept = input()

    if (trade_accept == 'y'):
        print('Here is what you have, which one do you want to give back? [Object Number]')
        show_objects(passengers[passenger_choose])
        trade_choose = int(input())
        print('Do you want to active the effect? [y/n]')
        active_choose = input()
    else: 
        trade_accept = 'n'
        trade_choose = 0

    return trade_accept, trade_choose, active_choose
    

def trade(trade_initiator, trade_recipient, initiator_object_num, recipient_object_num, passengers):
    passengers[trade_initiator].object.append(passengers[trade_recipient].object[recipient_object_num])       
    passengers[trade_recipient].object.append(passengers[trade_initiator].object[initiator_object_num])
    del passengers[trade_initiator].object[initiator_object_num]
    del passengers[trade_recipient].object[recipient_object_num]

    # if (accept_choose == 'y'):
    #     print('[Back to passenger] \nThe passenger accepted your trade, you got: ', passengers[passenger_choose - 1].object[trade_choose - 1].get_name()) 
    #     if (active_choose == 'y'):
    #         print('The passenger will active the effect of it')
    #         # Active function
    #     print('Are you going to active your object's effect? [y/n]')
    #     active_choose = input()
    #     if (active_choose == 'y'):
    #         print('You are going to active your object's effect.')
    #         # Active function
        
    # else:
    #     print('Your trade request is rejected by the passenger. ')



def main():
    num_round = 0
    victory = False

    passengers, associations, professions, objects = game_initialization()

    while(not victory):
        turn = num_round % 5
        print('Now is the turn for Passenger', (turn + 1))

        show_status(turn, passengers)
        show_objects(passengers[turn])

        print('What are you going to do? [1 - Trade; 2 - Duel; 3 - Proclaim the victory; 0 - Skip]')
        choose = input_check(input(), ['1', '2', '3', '0'])

        if (choose == '1'):
            passenger_choose, object_choose = trade_initiate()
            trade_accpet, trade_choose, active_choose = trade_query(trun, passenger_choose, passengers)
            if (trade_accpet == 'y'):
                print('Your trade query has been accepted.')
                trade(trun, passenger_choose - 1, object_choose - 1, trade_choose - 1, passengers)
                # TODO: Active the effect
            else:
                print('Your trade query has been rejected.')

        elif (choose == '2'):
            # Duel
            print('You are going to duel with someone, who are you want to duel with? ( Please input 1 ~ 5 )')
            passenger_choose = int(input())

            # This part is for public
            print('Passenger', turn + 1, 'is going to duel with Passenger', passenger_choose)
            attack = 1
            defend = 1
            for i in range(turn, 5):
                if(i == passenger_choose - 1):
                    continue
                print('Passenger', i, 'Who will you fight for? [ 1 - attack; 2 - defend; 0 - give up ]')
                stand_by = int(input())
                if(stand_by == 1):
                    print('Passenger', i, 'Will fight for the attacker.')
                    attack += 1
                elif(stand_by == 2):
                    print('Passenger', i, 'Will fight for the defender.')
                    defend += 1
                else:
                    print('Passenger', i, 'Give up.')
                print('Now the situation is attack:', attack, '; defend:', defend)
            for i in range(0, turn):
                if(i == passenger_choose - 1):
                    continue
                print('Passenger', i, 'Who will you fight for? [ 1 - attack; 2 - defend; 0 - give up ]')
                stand_by = int(input())
                if(stand_by == 1):
                    print('Passenger', i, 'Will fight for the attacker.')
                    attack += 1
                elif(stand_by == 2):
                    print('Passenger', i, 'Will fight for the defender.')
                    defend += 1
                else:
                    print('Passenger', i, 'Give up.')
                print('Now the situation is attack:', attack, '; defend:', defend)
            print('Anyone can use your weapons to help them.')
            # TODO: use weapon

            print('The duel result is attack:', attack, 'v.s. defend:', defend)
            if (attack > defend):
                print('Attacker WIN! Enjoy your victory!')

                # This part is for the attacker
                print('What are you going to do? [ 0 - Check the association and profession; 1 - Get an object]')
                # TODO: add a check for only one object
                victor_choose = int(input())
                if (victor_choose):
                    print('The passenger's objects are as following')
                    object_table = PrettyTable()
                    object_table.field_names = ['Index', 'Name of Object', 'Describe']
                    for i in range(len(passengers[passenger_choose - 1].object)):
                        object_table.add_row([i + 1, passengers[passenger_choose - 1].object[i].get_name(), passengers[passenger_choose - 1].object[i].get_description()])
                    print(status_table)
                    print('Which one you want to get? [ index ]')
                    rub_choose = int(input())
                    passengers[turn].object.append(passengers[passenger_choose - 1].object[rub_choose - 1])  
                    del passengers[passenger_choose - 1].object[rub_choose - 1]
                else:
                    print('The passenger's association is:', associations_map[passengers[passenger_choose - 1].association])
                    print('The passenger's profession is:', passengers[passenger_choose - 1].profession)
                    passengers[turn].check_association(passenger_choose - 1)
                    passengers[turn].check_profession(passenger_choose - 1)
            elif (attack < defend):
                print('Defender WIN! Enjoy your victory!')
                # This part is for the defender
                # TODO: the same with the formar
            else:
                print('DRAW! The attacker can get a object.')
                passengers[turn].object.append(objects[-1])
                objects.pop()

        elif (choose == '3'):
            # Proclaim the victory 
            print('Passenger', turn + 1, 'is going to preclaim the victory!')

            # This part is for the passenger turn
            print('Which type of victory do you want to preclaim? [0 - Positive victory; 1 - Negative victory]')
            victory_choose = int(input())
            if (victory_choose == 1):
                # Negative victory
                print('Choose passengers you think they will win: [ index without split ]')
                win_passengers = input()
                
                ralics = 0
                for i in range(len(win_passengers)):
                    i = int(i)
                    if passengers[win_passengers[i]].association == passengers[turn].association:
                        print('FALIED TO PRECLIME THE SUCCESS! THE PASSENGER', i+1, 'IS IN YOUR ASSOCIATION!')
                        print('THE ASSOCIATION', associations_map[passengers[turn].association], 'LOST!')
                        break
                    if (passengers[turn].association == 0):
                        ralics += passengers[win_passengers[i]].object.count(SecretBagKey())
                    else:
                        ralics += passengers[win_passengers[i]].object.count(SecretBagGoblet())
                if (passengers[turn].association == associations[5]):
                    if (ralics >= 3):
                        print('SUCCESS TO PRECLIME THE SUCCESS! THE ASSOCIATION', associations_map[passengers[turn].association], 'WIN!')
                    else:
                        print('FAILED TO PRECLIME THE SUCCESS! THE ASSOCIATION', associations_map[passengers[turn].association], 'LOST!')
                else:
                    if (ralics >= 2):
                        print('SUCCESS TO PRECLIME THE SUCCESS! THE ASSOCIATION', associations_map[passengers[turn].association], 'WIN!')
                    else:
                        print('FAILED TO PRECLIME THE SUCCESS! THE ASSOCIATION', associations_map[passengers[turn].association], 'LOST!')
            else:
                # Positive victory
                print('Choose passengers you think they will be your partner: [ index without split ]')
                win_passengers = input()

                ralics = 0
                for i in range(len(win_passengers)):
                    i = int(i)
                    if passengers[win_passengers[i]].association != passengers[turn].association:
                        print('FALIED TO PRECLIME THE SUCCESS! THE PASSENGER', i+1, 'IS NOT YOUR ASSOCIATION!')
                        print('THE ASSOCIATION', associations_map[passengers[turn].association], 'LOST!')
                        break
                    if (passengers[turn].association == 0):
                        ralics += passengers[win_passengers[i]].object.count(SecretBagGoblet())
                    else:
                        ralics += passengers[win_passengers[i]].object.count(SecretBagKey())
                if (passengers[turn].association == associations[5]):
                    if (ralics >= 2):
                        print('SUCCESS TO PRECLIME THE SUCCESS! THE ASSOCIATION', associations_map[passengers[turn].association], 'WIN!')
                    else:
                        print('FAILED TO PRECLIME THE SUCCESS! THE ASSOCIATION', associations_map[passengers[turn].association], 'LOST!')
                else:
                    if (ralics >= 3):
                        print('SUCCESS TO PRECLIME THE SUCCESS! THE ASSOCIATION', associations_map[passengers[turn].association], 'WIN!')
                    else:
                        print('FAILED TO PRECLIME THE SUCCESS! THE ASSOCIATION', associations_map[passengers[turn].association], 'LOST!')

        else:
            pass

        num_round += 1

#TODO: exchange function
#TODO: rob function
main()