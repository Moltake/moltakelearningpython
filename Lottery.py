import random

def menu():
    #ask player
    user_num = get_player_num()
    
    #get lottery numbers
    lotto_num = create_lotto_num()
    
    #print out winnings
    matched_num = user_num.intersection(create_lotto_num())
    print('You matched {}. You won ${}!'.format(matched_num, 100 ** len(matched_num)))

#User imputs 6 numbers
def get_player_num():
    number_csv = input('Enter your 6 numbers, seperated by commas: ') #csv is comma seperated value
    number_list = number_csv.split(',')
    interger_set = {int(number) for number in number_list}
    return interger_set

#App gets 6 'winning' numbers
def create_lotto_num():
    values = set() #can't make empty set with '{}', cause it means something else in python
    while len(values) <6:
        values.add(random.randint(1, 20)) #Need to make is somewhat doable, unlike real life
    return values

menu()

