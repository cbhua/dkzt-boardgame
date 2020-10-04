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


def status_show(turn, passengers):
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
        status_table.add_row([i, association_temp, profession_temp, passengers[i].num_object()])

    print(status_table)


def objects_show(passenger):
    object_table = PrettyTable()
    object_table.title = 'Your Objects'
    object_table.field_names = ['Index', 'Name of Object', 'Describe']

    for i in range(len(passenger.object)):
        object_table.add_row([i, passenger.object[i].get_name(), passenger.object[i].get_description()])
    
    print(object_table)


def objects_get(passenger, objects):
    passenger.object.append(objects[-1])
    objects.pop()


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


def trade_query(turn, passenger_choose, object_choose, passengers):
    print('[Ask passenger', passenger_choose, '] \nPassenger', turn, 'want to trade with you by', passengers[turn].object[object_choose].get_name(), '.Do you agree? [y/n]')
    trade_accept = input()

    if (trade_accept == 'y'):
        print('Here is what you have, which one do you want to give back? [Object Number]')
        objects_show(passengers[passenger_choose])
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


def duel_initiate():
    print('You are going to duel with someone, who are you want to duel with? [Passenger Number]')
    passenger_choose = int(input())
    return passenger_choose


def duel(duel_attacker, duel_defender, passnegers):
    print('Passenger {} is going to duel with passenger {}'.format(duel_attacker, duel_defender))
    attack = 1
    defend = 1
    if(duel_attacker != len(passnegers)):
        for i in range(duel_attacker, len(passnegers)):
            if (i == duel_defender): continue
            vote = duel_vote(i)
            if (vote == 1):
                attack += 1
            elif (vote == 2):
                defend += 1
            else:
                pass
    for i in range (0, duel_attacker):
        if (i == duel_defender): continue
        vote = duel_vote(i)
        if (vote == 1):
            attack += 1
        elif (vote == 2):
            defend += 1
        else:
            pass
    if (attack > defend):
        return 1
    elif (attack < defend):
        return 2
    else:
        return 0


def duel_vote(passenger):
    print('Ask passenger {}.Who are you going to fight for? [1 - Attacker; 2 - Defender; 0 - Skip]'.format(passenger))
    vote = int(input())
    return vote
    

def duel_victory(duel_winner, duel_losser, passengers):
    associations_map = ['Red', 'Blue']
    print('The winner is {}, what are you going to do? [1 - Check the association and profession; 2 - Get an object]'.format(duel_winner))
    victory_choose = int(input())
    if (victory_choose == 1):
        print('Passenger {}\'s association is {}'.format(duel_losser, associations_map[passengers[duel_losser].association]))
        print('Passenger {}\'s profession is {}'.format(duel_losser, passengers[duel_losser].profession))
        passengers[duel_winner].check_association(duel_losser)
        passengers[duel_winner].check_profession(duel_losser)
    if (victory_choose == 2):
        print('Passenger {} have such objects, which do you want? [Object Number]'.format(duel_losser))
        objects_show(passengers[duel_losser])
        object_choose = int(input())
        passengers[duel_winner].object.append(passengers[duel_losser].object[object_choose])
        del passengers[duel_losser].object[object_choose]


def victory_initiate():
    print('You are going to proclaim the victory. Which type of victory do you want to proclaim? [1 - Positive Victory; 2 - Negative Victory]')
    victory_type = int(input())
    return victory_type


def victory_check(victory_association, passengers, associations):
    print('Choose passengers you think they will win. [Passengers index without split]')
    victory_passengers = input()
    for i in range(len(victory_passengers)):
        i = int(i)
        if passengers[i].association != victory_association:
            print('FALIED TO PRECLIME THE SUCCESS! THE PASSENGER {} IS IN YOUR ASSOCIATION!'.format(i))
            return False
        if (victory_association == 0):
            ralics += passengers[i].object.count(SecretBagKey())
        else:
            ralics += passengers[i].object.count(SecretBagGoblet())
    if (victory_association != associations[5]):
        if (ralics >= 3):
            return True
        else:
            return False
    else:
        if (ralics >= 2):
            return True
        else:
            return False


def main():
    num_round = 0
    victory = False

    passengers, associations, professions, objects = game_initialization()

    while(not victory):
        turn = num_round % 5
        print('Now is the turn for Passenger', (turn + 1))

        status_show(turn, passengers)
        objects_show(passengers[turn])

        print('What are you going to do? [1 - Trade; 2 - Duel; 3 - Proclaim the victory; 0 - Skip]')
        choose = input_check(input(), ['1', '2', '3', '0'])

        if (choose == '1'):
            passenger_choose, object_choose = trade_initiate()
            trade_accpet, trade_choose, active_choose = trade_query(turn, passenger_choose, object_choose, passengers)
            if (trade_accpet == 'y'):
                print('Your trade query has been accepted.')
                trade(turn, passenger_choose - 1, object_choose - 1, trade_choose - 1, passengers)
                # TODO: Active the effect
            else:
                print('Your trade query has been rejected.')

        elif (choose == '2'):
            passenger_choose = duel_initiate()
            duel_result = duel(turn, passenger_choose, passengers)
            if (duel_result == 1):
                duel_victory(turn, passenger_choose, passengers)
            elif (duel_result == 2):
                duel_victory(passenger_choose, turn, passengers)
            else:
                objects_get(passengers[turn], objects)
                
        elif (choose == '3'):
            victory_choose = victory_initiate()
            if (victory_choose == 1):
                victory_result = victory_check(passengers[turn].association, passengers, associations)
            else:
                victory_result = victory_check(~passengers[turn].association, passengers, associations)
            if (victory_result):
                print('You Win')
                return
            else:
                print('You Loss')
                return

        else:
            pass

        num_round += 1


main()