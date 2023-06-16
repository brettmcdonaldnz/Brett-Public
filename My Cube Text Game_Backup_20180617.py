# Cube Text Game by Brett McDonald, inspired the movie 'Cube'

##### START CODE #####

import random

### Architecture:

# starting energy is 72 hours (reference from the movie), 1 = 1 minute
starting_energy = 4320

# initiate status recovery counters:
confusion_recovery = 0
blind_recovery = 0
powder_recovery = 0

# Generate Starting Location:
# This roughly represents an 'inner cube' of possibility, where you are at least 7 moves from an edge
starting_loc = [random.randrange(8,18), random.randrange(8,18), random.randrange(8,18)]

tattoos = {}

trap_effects = {'red': 'laser', 'blue': 'flame', 'green': 'blade', 'amber': 'chemical', 'white': 'gas'}

trap_cooldown = {'laser': 0, 'flame': 0, 'blade': 0, 'chemical': 0, 'gas': 0}

trap_reserves = {'laser': 1, 'flame': 3, 'blade': 1000, 'chemical': 5, 'gas': 10}

laser_num = 0

prime_list = [
2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251,
257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431,
433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613,
617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811,
821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]

prime_powers_list = [4, 8, 9, 16, 25, 27, 32, 49, 64, 81, 121, 125, 128, 169, 243, 256, 289, 343, 361, 512, 529, 625, 729, 841, 961]

hatch_descriptions = {'north': 'north wall','east': 'east wall','south': 'south wall','west':'west wall','up':'ceiling','down':'floor'}

colours = ['green','amber','red','blue','white']

rooms = {}

global_time = 0

used_hash = []

hatch_movements = []

purple_seen = False

black_seen = False

gold_seen = False

red_seen = False

blue_seen = False

green_seen = False

amber_seen = False

white_seen = False

rooms_seen = []

bridge_room_time = 0

bridge_made_noise = False

last_heard_bridge = 0

### Player Parameters:

player = {'name': 'name', 'job': 'job','energy': starting_energy, 'first aid': 5, 'position': 'center', 'loc': starting_loc, 'cardinal': 'north'}

### Status System ###
# Status - Confusion:
# - Confusion may be also be automatically and permanently triggered when energy reaches a very low level.
# - There could be multiple states of confusion as energy depletes.
# Status - Bleeding: Inflicted by sharp traps. Energy depletion *2 for every action. Recover with first aid.
# Bleeding report (if True): 'The cut is still bleeding...'
# Bleeding report (if changed from True to False): 'The bleeding stopped'.
# Status - Blind: Inflicted by gas or acid traps. Can't use inspect number, not told colours of rooms, Fool Me Twice is disabled. Recover automatically after 60 minutes.
# Blind report (60-30 minutes): 'I can't see at all...'
# Blind report (30-1 minutes): 'Everything's black, but I'm starting to make out the shapes'
# Blind report (0 minutes): 'Finally, I can see again'.
# Status - Burned: Energy depletes * 2 for every action. Recover after 180 minutes.
# Burn report (180-120 minutes): 'The burn is extremely painful, every movement is hurting'.
# Burn report (119-60 minutes): 'The burn has stopped throbbing, but it still hurts to move'.
# Burn report (60-1 minutes): 'The burn isn't so painful anymore, it should stop hurting soon'.
# Burn report (0 minutes): 'The burn isn't hurting anymore' (set Burn to False).
# Status - Powdered: Covered in a chemical powder. You will instantly die if exposed to fire, bleeding or water. The powder will rub off eventually.

status_conditions = {'bleeding': False,'blind': False, 'burned': False, 'confused': False, 'powder': False}

action_cost = {'n': 0.1, 'e': 0.1, 's': 0.1, 'w': 0.1, 'u': 0.1, 'd': 0.1, 'm': 1, 'f': 5, 'o': 1, 'c': 1, '#': 0.5, 'i': 0.5, 'h': 0.1, 'r': 30, '?': 0.1}

### Math Functions:


def hash_id(location):
    """Generate a unique 9-digit serial."""
    global used_hash
    count = 0
    hash_fail = 9
    while count < hash_fail:
        count += 1
        room_id = ''
        for i in range(3):
            combination = []
            for a in range(location[i]+1):
                for b in range(location[i]+1):
                    for c in range(location[i]+1):
                        if a + b + c == location[i] and len('{}{}{}'.format(a,b,c)) == 3:
                            combination.append('{}{}{}'.format(a,b,c))
            if i != 2:
                room_id += random.choice(combination) + ' '
            else:
                room_id += random.choice(combination)
        if room_id not in used_hash:
            used_hash.append(room_id)
            return room_id
    return exit(ms_hash_id_termination)


def prime_test(room_id):
    """Check if there is a prime in the room id."""
    prime = False
    # check the first three digits:
    if room_id[0] != '0':
        if int('{}{}{}'.format(room_id[0],room_id[1],room_id[2])) in prime_list:
            prime = True
    elif room_id[0] == '0':
        if int('{}{}'.format(room_id[1],room_id[2])) in prime_list:
            prime = True
    elif room_id[0] == '0' and room_id[1] == '0':
        if int('{}'.format(room_id[2])) in prime_list:
            prime = True
    # check the second three digits:
    if room_id[4] != '0':
        if int('{}{}{}'.format(room_id[4],room_id[5],room_id[6])) in prime_list:
            prime = True
    elif room_id[4] == '0':
        if int('{}{}'.format(room_id[5],room_id[6])) in prime_list:
            prime = True
    elif room_id[4] == '0' and room_id[5] == '0':
        if int('{}'.format(room_id[6])) in prime_list:
            prime = True
    # check the last three digits:
    if room_id[8] != '0':
        if int('{}{}{}'.format(room_id[8],room_id[9],room_id[10])) in prime_list:
            prime = True
    elif room_id[8] == '0':
        if int('{}{}'.format(room_id[9],room_id[10])) in prime_list:
            prime = True
    elif room_id[8] == '0' and room_id[9] == '0':
        if int('{}'.format(room_id[10])) in prime_list:
            prime = True
    return prime


def prime_power_test(room_id):
    """Check if there is a prime power in the room id."""
    prime_power = False
    # check the first three digits:
    if room_id[0] != '0':
        if int('{}{}{}'.format(room_id[0],room_id[1],room_id[2])) in prime_powers_list:
            prime = True
    elif room_id[0] == '0':
        if int('{}{}'.format(room_id[1],room_id[2])) in prime_powers_list:
            prime = True
    elif room_id[0] == '0' and room_id[1] == '0':
        if int('{}'.format(room_id[2])) in prime_powers_list:
            prime = True
    # check the second three digits:
    if room_id[4] != '0':
        if int('{}{}{}'.format(room_id[4],room_id[5],room_id[6])) in prime_powers_list:
            prime = True
    elif room_id[4] == '0':
        if int('{}{}'.format(room_id[5],room_id[6])) in prime_powers_list:
            prime = True
    elif room_id[4] == '0' and room_id[5] == '0':
        if int('{}'.format(room_id[6])) in prime_powers_list:
            prime = True
    # check the last three digits:
    if room_id[8] != '0':
        if int('{}{}{}'.format(room_id[8],room_id[9],room_id[10])) in prime_powers_list:
            prime = True
    elif room_id[8] == '0':
        if int('{}{}'.format(room_id[9],room_id[10])) in prime_powers_list:
            prime = True
    elif room_id[8] == '0' and room_id[9] == '0':
        if int('{}'.format(room_id[10])) in prime_powers_list:
            prime = True
    return prime_power


def generate_room(loc):
    """Generate a new room at the location provided."""
    global rooms
    global global_time
    # trap status needs to be initiated before assignment in the rooms dictionary
    trap = False
    if '{}'.format(loc) not in rooms:
        room_id = hash_id(loc)
        # make sure that for the bridge extended position, the pre-existing id is used:
        if loc == bridge_extended_position:
            room_id = bridge_extended_position_id
        # the extended bridge is gold
        if loc == bridge_extended_position:
            colour = 'gold'
        # bridge docks are the only purple rooms
        elif loc in bridge_docks:
            colour = 'purple'
        else:
            colour = random.choice(colours)
        # don't put any traps in the first room, or rooms that are gold, purple or pitch black; only trap rooms that have primes or prime powers in their engraving (room_id):
        # check that the player is not in the first room:
        if global_time != 0:
            # check that the player is not in a safe room:
            if colour not in ['gold','purple','pitch black']:
                # check that the room is trapped:
                if prime_test(room_id) or prime_power_test(room_id):
                    trap = True
                    # set up the starting trap values:
                    if trap:
                        trap_effect = trap_effects[colour]
                        trap_reset = trap_cooldown[trap_effect]
                        trap_reserve = trap_reserves[trap_effect]
                        trap_trigger = random.choice(['time','sound','infra-red'])
                        trap = {'effect': trap_effect, 'reset': trap_reset, 'reserve': trap_reserve, 'trigger': trap_trigger}
        # create a sub-dictionary in the rooms dictionary with the loc as the key
        # Rooms use cardinal points as keys with hatch status open/closed as the values
        rooms['{}'.format(loc)] = {'id': room_id, 'trap': trap, 'colour': colour, 'north': 'closed', 'east': 'closed', 'south': 'closed', 'west': 'closed', 'up': 'closed', 'down': 'closed'}
        # the colour of the room will determine the kind of trap, the reset time, and the number of times it can activate:

        # the trigger will be randomly chosen from this set:
        # trap_triggers = ['time','sound','blood','pressure','infra-red','

def generate_room_trap(loc):
    """Generate a new room at the location provided. This function is used for the teletrap cheat code,
    it needs to match the minimal functionality of generate_room() to work properly."""
    colour = input('What colour? <red,blue,green,amber,white> ')
    global rooms
    global global_time
    # trap status needs to be initiated before assignment in the rooms dictionary
    trap = True
    if '{}'.format(loc) not in rooms:
        room_id = hash_id(loc)
        # make sure that for the bridge extended position, the pre-existing id is used:
        if loc == bridge_extended_position:
            room_id = bridge_extended_position_id
        # the extended bridge is gold
        # don't put any traps in the first room, or rooms that are gold, purple or pitch black; only trap rooms that have primes or prime powers in their engraving (room_id):
        # check that the player is not in the first room:
        if trap:
            trap_effect = trap_effects[colour]
            trap_reset = trap_cooldown[trap_effect]
            trap_reserve = trap_reserves[trap_effect]
            trap_trigger = random.choice(['time','sound','infra-red'])
            trap = {'effect': trap_effect, 'reset': trap_reset, 'reserve': trap_reserve, 'trigger': trap_trigger}
        # create a sub-dictionary in the rooms dictionary with the loc as the key
        rooms['{}'.format(loc)] = {'id': room_id, 'trap': trap, 'colour': colour, 'north': 'closed', 'east': 'closed', 'south': 'closed', 'west': 'closed', 'up': 'closed', 'down': 'closed'}
        # the colour of the room will determine the kind of trap, the reset time, and the number of times it can activate:

        # the trigger will be randomly chosen from this set:
        # trap_triggers = ['time','sound','blood','pressure','infra-red','

### Generate Rooms:

# Generate Bridge Room:
# Generate the six possible exit positions:
bridge_extended_positions = [[13,13,27],[27,13,13],[13,13,0],[13,0,13],[0,13,13],[13,27,13]]
# Choose one of the six possible exit positions:
bridge_extended_position = random.choice(bridge_extended_positions)
# Set an id for the bridge extended position (this will be used for the tattoo as a hint toward the exit)
bridge_extended_position_id = hash_id(bridge_extended_position)
# Generate the six bridge docks (they are part of the main cube, in the center of each face, and will be purple)
bridge_docks = [[13,13,26],[26,13,13],[13,13,1],[13,1,13],[1,13,13],[13,26,13]]
# Set up the total bridge positions, as bridge docks will be used separately for different purposes
bridge_positions = bridge_docks[:]
# Add the extended position to the six dock positions, for seven total positions (the bridge doesn't actually 'move' into any dock, the dock just turns black to
# represent that the bridge program is cycling through that position.
bridge_positions.append(bridge_extended_position)
# ensure the bridge moves in a logical order from dock to extended position (the bridge only actually moves into and out of the extended position, the other 'moves' are
# just the room changing colour
for x in bridge_positions:
    for y in x:
        if y == 0:
            bridge_positions.sort(reverse=True)
        elif y == 27:
            bridge_positions.sort()
# initiate a counter for moving the bridge through the seven positions:
bridge_cycle = 0
# move the bridge into the starting position:
bridge_current_position = bridge_positions[bridge_cycle]

# Initiate laser tattoo series:
lasers = {0: ['left wrist',bridge_extended_position_id], 1: ['right wrist','+FEAR+GOD+'], 2: ['left palm','+'], 3: ['right palm', '+'], 4: True}


### Message System:

def ms_looking_Call(request_message):
    """Prints a message corresponding to the request_message input."""
    # Confusion variants for cardinal awareness:
    if not status_conditions['confused']:
        looking_aroundD = {'ms_center_lookaround': '''\n*** You can look north, east, south, west, up or down <n,e,s,w,u,d>''',
                           'ms_wall_at_wall': '''\nYou are standing at the {} wall.'''.format(player['cardinal']),
                           'ms_wall_at_ceiling': '''\nYou are looking up at the ceiling.''',
                           'ms_wall_at_floor': '''\nYou are looking down at the floor.'''
                           }
    else:
        looking_aroundD = {'ms_center_lookaround': '''\n*** You can look this way, that way, the other way, another way, up or down <?,?,?,?,u,d>''',
                           'ms_wall_at_wall': '''\nYou are standing at a wall.''',
                           'ms_wall_at_ceiling': '''\nYou are looking up at the ceiling.''',
                           'ms_wall_at_floor': '''\nYou are looking down at the floor.'''
                           }
    return print(looking_aroundD[request_message])

# Exit Messages:

ms_energy_death = '''You have run out of energy. Your adventure ends here.'''

# Common Messages:

ms_engraving = '''\nThe hatch is engraved with the number '{}'.'''

ms_mulling = '''\n(Okay...)>> '''

ms_open_hatch = '''You opened the hatch.'''

ms_back_away_from_hatch = '''You backed away from the hatch.'''

ms_close_hatch = '''You closed the hatch.'''

# Function-Specific Messages:

ms_purple_impression = '''(This is the first purple room I've seen...it feels safe...)'''

ms_black_impression = '''(This is the first pitch black room I've seen...if feels ominous...)'''

ms_gold_impression = '''(This is the first gold room I've seen...this must be the end...)'''

ms_red_impression = '''(This is the first red room I've seen...it feels dangerous...)'''

ms_blue_impression = '''(This is the first blue room I've seen...it's blue like a hot flame...)'''

ms_green_impression = '''(This is the first green room I've seen...it feels unnerving...)'''

ms_amber_impression = '''(This is the first amber room I've seen...it reminds me of hazard lights...)'''

ms_white_impression = '''(This is the first white room I've seen...it feels too clinical...)'''

ms_number_impression_0 = '''I've seen this number before.'''

ms_edge_test_view_void = '''The hatch leads to a pitch black void.'''

ms_edge_test_view_outerwall = '''The hatch leads to a pitch black void. You can just make out an outer-wall about the length of one room away; it's too far to reach.'''

ms_hash_id_termination = '''Terminating system...(the room was engulfed in flames)'''

ms_time_estimate_1hr = '''I've been awake for about an hour.'''

ms_time_estimate_greater1 = '''I've been awake for about {:.0f} hours.'''

ms_time_estimate_0 = '''I haven't been awake for long.'''

ms_energy_estimate_0 = '''I'm feeling about {:.0f}%.'''

ms_status_estimate_healthy = '''I'm feeling healthy.'''

ms_noise_time_estimate_0 = '''I last heard that rumbling just a moment ago.'''

ms_noise_time_estimate_5 = '''I last heard that rumbling about 5 minutes ago.'''

ms_noise_time_estimate_10 = '''I last heard that rumbling about 10 minutes ago.'''

ms_noise_time_estimate_15 = '''I last heard that rumbling about 15 minutes ago.'''

ms_noise_time_estimate_20 = '''I last heard that rumbling about 20 minutes ago.'''

ms_noise_time_estimate_25 = '''I last heard that rumbling about 25 minutes ago.'''

ms_hatch_movement_memory_0 = '''I haven't moved anywhere.'''

ms_hatch_movement_memory_1 = '''The last hatch movements I can remember are {}.'''

ms_describe_room_black = '''You are standing in a pitch black room, you can't make out the hatches, but you still have a sense of direction'''

ms_describe_room_openclose = '''\nYou are standing in the centre of a {}, cube-like room.\nThere is a small hatch in the centre of the room's floor, ceiling and in each wall.\nThe {} hatches are open, the {} hatches are closed.'''

ms_describe_room_open = '''\nYou are standing in the centre of a {}, cube-like room.\nThere is a small hatch in the centre of the room's floor, ceiling and in each wall.\nAll of the hatches are open.'''

ms_describe_room_closed = '''\nYou are standing in the centre of a {}, cube-like room.\nThere is a small hatch in the centre of the room's floor, ceiling and in each wall.\nAll of the hatches are closed.'''

ms_center_baseskill = '''*** Or, choose a base skill:'''

ms_center_eachBaseSkill = '''*** {}, {}'''

ms_center_lookaround_react = '''\n(I should take a look around)>> '''

ms_wall_hatch_status = '(The hatch is {})'

ms_wall_open_or_return = '''\n*** You can open the hatch <o>, or go back to the centre of the room <h>'''

ms_wall_close_center_number = '''\n*** You can close the hatch <c>, go back to the centre of the room <h>, or inspect the hatch number <#> ***'''

ms_wall_close_number_center_crawlInto = '''\n*** You can close the hatch <c>, inspect the hatch number <#>, go back to the center of the room <h>, or crawl into the hatch <i> ***'''

ms_wall_close_number_center_climbUp = '''\n*** You can close the hatch <c>, inspect the hatch number <#>, go back to the center of the room <h>, or climb up into the hatch <i> ***'''

ms_wall_hatch_number_center_climbDown = '''\n*** You can close the hatch <c>, inspect the hatch number <#>, go back to the center of the room <h>, or climb down into the hatch <i> ***'''

ms_wall_crawl_into_hatch = '''You crawled into the hatch.'''

ms_wall_climb_up_into_hatch = '''You climbed up into the hatch.'''

ms_wall_climb_down_into_hatch = '''You climbed down into the hatch.'''

ms_in_hatch_open_number_crawlBackOut = '''\n*** You can open the external hatch <o>, inspect the external hatch number <#>, or crawl back out of the hatch <h>  ***'''

ms_in_hatch_open_number_crawlDownOut = '''\n*** You can open the external hatch <o>, inspect the external hatch number <#>, or crawl down out of the hatch <h> ***'''

ms_in_hatch_open_number_climbUpOut = '''\n*** You can open the external hatch <o>, inspect the external hatch number <#>, or climb up out of the hatch <h> ***'''

ms_in_hatch_crawlBackOut = '''You crawled back out of the hatch.'''

ms_in_hatch_climbDown = '''You climbed back down from the hatch.'''

ms_in_hatch_climbBackOut = '''You climbed back out of the hatch.'''

ms_in_hatch_external_engraving = '''\nThe external hatch is engraved with the number '{}'.'''

ms_in_hatch_close_number_crawlOut_crawlInto = '''\n*** You can close the external hatch <c>, inspect the external hatch number <#>, crawl back out of the hatch <h>, or crawl into the next room <i> ***'''

ms_in_hatch_close_number_climeDown_climbUp = '''\n*** You can close the external hatch <c>, inspect the external hatch number <#>, climb down out of the hatch <h>, or climb up into the next room <i> ***'''

ms_in_hatch_close_number_climbUp_climbDown = '''\n*** You can close the external hatch <c>, inspect the external hatch number <#>, climb up out of the hatch <h>, or climb down into the next room <i> ***'''

ms_in_hatch_nextRoom = '''You moved out of the hatch and into the next room.'''

ms_time_update_fadeToBlack = '''\nThe room became pitch black'''

ms_time_update_backToPurple = '''\nYou hear an electrical hum... the room became purple'''

ms_time_update_noise1 = '''You hear a deafening screech, and the room rattles violently. The noise was very close.'''

ms_time_update_noise4 = '''You hear the squealing of brakes, and the room shudders like a bus coming to a halt. The noise was close by.'''

ms_time_update_noise7 = '''You hear a high-pitched squeal, and the room rattles. The noise was somewhat distant.'''

ms_time_update_noise10 = '''You hear a squeal, and the room vibrates as if a truck had passed by. The noise was distant.'''

ms_time_update_noise13 = '''You hear a quiet squeal, and the room vibrates slightly. The noise was very distant.'''

ms_introduction_wakeUpDrank = '''You wake up in a {}, six-sided room... a cube\nYou have a pounding headache.\nYou can't remember your own name...'''

ms_introduction_OhNaNaWhatsMyName = '''\n(What's my name again?)>> '''

ms_introduction_details_returning = '''\nThe details are starting to come back, your name is {}, but you don't remember your job...'''

ms_introduction_something_important = '''It was something important like...\n'''

ms_introduction_dont_tell_me = '''Don't tell me i was a {}...'''

ms_introduction_job_react = '''\n(What was my job?)>> '''

ms_introduction_former_job = '''You were a talented {}, but it's not clear how that will help in here.'''

ms_introduction_wrong_job = '''\n(No, that wasn't it...)'''

ms_introduction_think_of_something = '''\n(I need to think of something...)'''

ms_in_hatch_lightAhead = '''There is an overwhelming bright light ahead'''

ms_in_hatch_goToTheLight = '''*** You can advance towards the light <i>, or move back out of the hatch <h>'''

ms_in_hatch_lightReact = '''(This is it...)'''


### Trap System:

def trap(noise=False):
    """Run a trap."""
    global laser_num
    global tattoos
    # get the trap effect:
    effect = rooms['{}'.format(player['loc'])]['trap']['effect']
    # get the trap reset:
    reset = rooms['{}'.format(player['loc'])]['trap']['reset']
    # get the trap reserve:
    reserve = rooms['{}'.format(player['loc'])]['trap']['reserve']
    # get the trap trigger:
    trigger = rooms['{}'.format(player['loc'])]['trap']['trigger']
    # if the trap has reset, and it has reserve, run it:
    if reset == 0:
        if reserve > 0:
            if effect == 'laser':
                if trigger == 'infra-red' or (trigger == 'sound' and noise):
                    # laser trap does not have a cooldown; each laser only activates once
                    # the first four tattoos will be added to your tattoo collection:
                    if laser_num in [0,1,2,3]:
                        print('''A laser emerges from the ceiling and burns a mark into your {}'''.format(lasers[laser_num][0]))
                        tattoos[laser_num] = '''The blistered mark on your {} says "{}"'''.format(lasers[laser_num][0],lasers[laser_num][1])
                        # the first two lasers do a little bit of damage:
                        if laser_num in [0,1]:
                            player['energy'] -= 30
                            print('''(That didn't hurt too much...)''')
                        # the third and fourth lasers halve your remaining life:
                        if laser_num in [2,3]:
                            player['energy'] //= 2
                            print('''(That hurt like hell...)''')
                    elif laser_num == 4:
                        exit('''A laser pierces through the right side of your chest...you feel a hot, sharp pain, then nothing...''')
                    # prepare the next laser activation to run the next laser tattoo:
                    laser_num += 1
                    # Traumatic traps remove confusion:
                    status_conditions['confused'] = False
            if effect == 'flame':
                if trigger == 'infra-red':
                    if not status_conditions['powder']:
                        print('''Hot blue flame engulfs the room''')
                        # it does a lot of damage (24 hours worth):
                        player['energy'] -= 1440
                        print('''(That hurt like hell...)''')
                        # flame trap takes 30 minutes to reset (gotta cool those jets):
                        rooms['{}'.format(player['loc'])]['trap']['reset'] += 30
                        # Traumatic traps remove confusion:
                        status_conditions['confused'] = False
                        # Fire burns...
                        status_conditions['burned'] = True
                        # If the player is powdered, the fire will ignite the powder and kill the player:
                    else:
                        exit('''Hot blue flame engulfs the room\nThe powder ignites, and your entire body is consumed by fire''')
            if effect == 'blade':
                if trigger == 'infra-red':
                    if not status_conditions['powder']:
                        # blades do not have a cooldown, and can activate infinite times
                        print('''You see a glint in the air...razer-thin wires lacerate your body''')
                        # it does a lot of damage (24 hours worth), add bleeding effects later:
                        player['energy'] -= 1440
                        print('''(That hurt like hell...)''')
                        # Traumatic traps remove confusion:
                        status_conditions['confused'] = False
                        status_conditions['bleeding'] = True
                        # If the player is powdered, the blood will ignite the powder and kill the player:
                    else:
                        exit('''You see a glint in the air...razer-thin wires lacerate your body\nThe blood from your cuts starts reacting with the powder on your skin...\nThe powder ignites, and your entire body is consumed by fire''')
            if effect == 'chemical':
                if trigger == 'infra-red':
                    # this will be a random choice between flash powder and blinding acid; they don't do any immediate harm:
                    chemical_effect = random.choice([1,2])
                    if chemical_effect == 1:
                        if not status_conditions['bleeding']:
                            print('''You hear a loud pop, and a fine white powder fills the room...it settles all over your skin and clothes''')
                            print('''(It doesn't hurt...but I don't trust it)''')
                            status_conditions['powder'] = True
                        else:
                            exit('''You hear a loud pop, and a fine white powder fills the room\nThe powder immediately reacts with blood from your cuts, and starts to sizzle...\nThe powder ignites, and your entire body is consumed by fire''')
                    elif chemical_effect == 2:
                        print('''A hidden nozzle sprays something directly into your eyes...''')
                        print('''(My eyes feel like they're on fire, I can't see anything...''')
                        status_conditions['blind'] = True
                    rooms['{}'.format(player['loc'])]['trap']['reset'] += 10
            if effect == 'gas':
                if trigger == 'infra-red':
                    # set confusion to True
                    print('''You feel a breeze and hear a whirring, like an air pump''')
                    print('''(Something is happening...I don't want to stay to find out what it is...)''')
                    status_conditions['confused'] = True
                    rooms['{}'.format(player['loc'])]['trap']['reset'] += 5
            # subtract one from the trap reserve after running it (all traps will spend one reserve per activation, some traps have more reserve than others):
            rooms['{}'.format(player['loc'])]['trap']['reserve'] -= 1
    return

### Mind Map System:


def time_estimate():
    """Get a string of a rough approximation of global time spent in the maze."""
    time_approximation = global_time // 60
    # if the player is not confused:
    if not status_conditions['confused']:
        if time_approximation == 1:
            time_approximation = ms_time_estimate_1hr
        elif time_approximation > 1:
            time_approximation = ms_time_estimate_greater1.format(global_time // 60)
        else:
            time_approximation = ms_time_estimate_0
    else:
        time_approximation = '''I have no idea how long I've been here.'''
    return time_approximation


def energy_estimate():
    """Get a string of a rough approximation of remaining energy."""
    # if the player is not confused:
    if not status_conditions['confused']:
        energy_approximation = ms_energy_estimate_0.format(player['energy'] / 4320 * 100)
    else:
        energy_approximation = '''I feel like I'm floating.'''
    return energy_approximation


def status_estimate():
    """Get a string of a rough approximation of status ailments."""
    status_report = ""
    # If the player is healthy:
    if True not in status_conditions.values():
        status_report = ms_status_estimate_healthy
    # For all conditions that are True:
    if status_conditions['bleeding']:
        status_report += '''I'm bleeding...\n'''
    if status_conditions['burned']:
        status_report += '''I'm burned...\n'''
    if status_conditions['blind']:
        status_report += '''I'm blind...\n'''
    if status_conditions['confused']:
        status_report += '''My head is spinning...\n'''
    if status_conditions['powder']:
        status_report += '''There is a fine white powder on my skin and clothes...\n'''
    return status_report


def noise_time_estimate():
    """Get a string of a rough approximation of the last bridge noise."""
    # the bridge only makes a noise when it extends into and out of the extended position, which is handled in time_update()
    global last_heard_bridge
    global bridge_made_noise
    # if the player is not confused:
    if not status_conditions['confused']:
        noise_report = '''It's quiet.'''
        # adjust the time estimates to automatically calculate the actual time since a noise was made
        if bridge_made_noise:
            # if noise was heard less than 5 minutes ago:
            if 0 <= last_heard_bridge <= 5:
                noise_report = '''I just heard something a moment ago.'''
            # if noise was heard less than an hour ago, and more than 5 minutes ago:
            elif 6 <= last_heard_bridge <= 59:
                nearest_fiveMinutes = (last_heard_bridge // 5) * 5
                noise_report = '''It's been about {:.0f} minutes since I last heard something.'''.format(nearest_fiveMinutes)
            # if noise was heard about an hour ago:
            elif 60 <= last_heard_bridge <= 90:
                noise_report = '''It's been about an hour since I last heard something.'''
            # if noise was heard about two or more hours ago:
            elif 91 <= last_heard_bridge:
                noise_report = '''It's been more than an hour since I last heard something.'''
    else:
        noise_report = '''There is a high pitched ringing in my ears, I can hardly hear myself think.'''
    return noise_report


def hatch_movement_memory():
    """Display the last few hatch movements."""
    global hatch_movements
    hatch_report = ms_hatch_movement_memory_0
    # memory range may be affected by job, status and energy
    memory_range = 5
    if player['job'] == 'Architect':
        memory_range = 20
    remembered_movements = []
    if hatch_movements:
        # if the player is not confused:
        if not status_conditions['confused']:
            if len(hatch_movements) < memory_range:
                for i in range(len(hatch_movements)):
                    remembered_movements.append(hatch_movements[i])
            else:
                for i in range(len(hatch_movements)-memory_range,len(hatch_movements)):
                    remembered_movements.append(hatch_movements[i])
            hatch_report = ms_hatch_movement_memory_1.format(remembered_movements)
        else:
            hatch_report = '''How did I get here?'''
    return hatch_report


def tattoo():
    """Display the tattoo on your left wrist (if you still have a left wrist)."""
    tattoo_report = None
    # if the player has tattoos:
    if tattoos:
        tattoo_report = ""
        for key in tattoos:
            tattoo_report += '''{}...\n'''.format(tattoos[key])
    return tattoo_report


def first_aid_report():
    """Report the number of bandages left"""
    bandages = player['first aid']
    report = ""
    if bandages == 0:
        report = '''I'm all out of bandages.'''
    elif bandages == 1:
        report = '''I only have one bandage left.'''
    elif bandages > 1:
        report = '''I have {} bandages left.'''.format(bandages)
    return report


### Skill System:
# Skill availability is based on location and job
base_skills_center = {'mental map': '<m>', 'first aid': '<f>', 'rest': '<r>'}

# Job skill availability is based on job (to be implemented in future)
job_skills = {'X': {}, 'Architect': {}, 'Soldier': {}, 'Mathematician': {}, 'Doctor': {}, 'Magician': {}}


def mental_map():
    """Display mental deductions about your situation."""
    # standard reports are only one line
    standard_reports = [time_estimate(),energy_estimate(),noise_time_estimate(),hatch_movement_memory(),first_aid_report()]
    # special reports may already contain multiple lines
    special_reports = [tattoo(),status_estimate()]
    evaluation = '\n'
    # standard reports have line breaks added to them
    for report in standard_reports:
        # the tattoo reports already have \n and '...', so don't add those to the tattoo reports
        evaluation += '{}..\n'.format(report)
    # special reports are added to the evaluation 'as is'
    for report in special_reports:
        # use a try block, because error will be caused while report is None
        try:
            evaluation += report
        except:
            pass
    return evaluation


def first_aid():
    """Use first aid to recover from bleeding or burned"""
    # use first aid, if available:
    if player['first aid'] > 0:
        # if you are not bleeding or burned, there is no need for first aid:
        if not status_conditions['bleeding'] and not status_conditions['burned']:
            print('''(I'm feeling fine, there's no need for first aid)''')
        # Stop the bleeding:
        elif status_conditions['bleeding'] and not status_conditions['burned']:
            print('''(That should stop the bleeding)''')
            status_conditions['bleeding'] = False
            player['first aid'] -= 1
        # Soothe the burn:
        elif status_conditions['burned'] and not status_conditions['bleeding']:
            print('''(That will soothe the burn)''')
            status_conditions['burned'] = False
            player['first aid'] -= 1
        # Stop bleeding and soothe burn:
        elif status_conditions['burned'] and status_conditions['bleeding']:
            print('''(That will stop the bleeding and soothe the burn)''')
            status_conditions['burned'] = False
            status_conditions['bleeding'] = False
            player['first aid'] -= 1
    # if no first aid is available, print the 'no bandages' message
    elif player['first aid'] == 0:
        print('''(I'm all out of bandages)''')


# Passive Skills:


def colour_impression():
    """Display first impressions when seeing new colours. Nest this function in describe_room()."""
    global purple_seen
    global black_seen
    global gold_seen
    global red_seen
    global blue_seen
    global green_seen
    global amber_seen
    global white_seen
    # get the colour of the room the player is in:
    colour = rooms['{}'.format(player['loc'])]['colour']
    # check first impressions for each colour:
    if not purple_seen and colour == 'purple':
        print(ms_purple_impression)
        purple_seen = True
    if not gold_seen and colour == 'gold':
        print(ms_gold_impression)
        gold_seen = True
    if not red_seen and colour == 'red':
        print(ms_red_impression)
        red_seen = True
    if not blue_seen and colour == 'blue':
        print(ms_blue_impression)
        blue_seen = True
    if not green_seen and colour == 'green':
        print(ms_green_impression)
        green_seen = True
    if not amber_seen and colour == 'amber':
        print(ms_amber_impression)
        amber_seen = True
    if not white_seen and colour == 'white':
        print(ms_white_impression)
        white_seen = True
    if not green_seen and colour == 'green':
        print(ms_green_impression)
        green_seen = True


def number_impression():
    """Display an extra sentence if the room number has been seen before. Call this function with every number inspection."""
    global rooms_seen
    room = rooms['{}'.format(player['loc'])]['id']
    if room in rooms_seen:
        print(ms_number_impression_0)
    else:
        rooms_seen.append(room)


### Position updates:


def edge_test():
    """Test if a hatch leads to a view of of the outer-wall."""
    edge = False
    # test if you are in the extended bridge position, then test for its appropriate views.
    if player['loc'] == bridge_extended_position:
        # check for Penthouse views:
        if bridge_extended_position[2] == 27:
            if player['cardinal'] in ['north','south','east','west']:
                if status_conditions['blind']:
                    print('''You reach into the hatch, but it is just a void''')
                else:
                    print(ms_edge_test_view_void)
                edge = True
        # check for Basement views:
        elif bridge_extended_position[2] == 0:
            if player['cardinal'] in ['north','south','east','west']:
                if status_conditions['blind']:
                    print('''You reach into the hatch, but it is just a void''')
                else:
                    print(ms_edge_test_view_void)
                edge = True
        # check for North Balcony views:
        elif bridge_extended_position[1] == 0:
            if player['cardinal'] in ['up','down','east','west']:
                if status_conditions['blind']:
                    print('''You reach into the hatch, but it is just a void''')
                else:
                    print(ms_edge_test_view_void)
                edge = True
        # check for South Balcony views:
        elif bridge_extended_position[1] == 27:
            if player['cardinal'] in ['up','down','east','west']:
                if status_conditions['blind']:
                    print('''You reach into the hatch, but it is just a void''')
                else:
                    print(ms_edge_test_view_void)
                edge = True
        # check for East Balcony views:
        elif bridge_extended_position[0] == 27:
            if player['cardinal'] in ['up','down','north','south']:
                if status_conditions['blind']:
                    print('''You reach into the hatch, but it is just a void''')
                else:
                    print(ms_edge_test_view_void)
                edge = True
        # check for West Balcony views:
        elif bridge_extended_position[0] == 0:
            if player['cardinal'] in ['up','down','north','south']:
                if status_conditions['blind']:
                    print('''You reach into the hatch, but it is just a void''')
                else:
                    print(ms_edge_test_view_void)
                edge = True
    # check if the player is in a bridge dock and the bridge is extended adjacent to that dock. There will be no edge views, so pass:
    elif player['loc'] in bridge_docks and bridge_current_position == bridge_extended_position and -1 <= player['loc'][0] - bridge_extended_position[0] <= 1 and -1 <= player['loc'][1] - bridge_extended_position[1] <= 1 and -1 <= player['loc'][2] - bridge_extended_position[2] <= 1 :
        pass
    else:
    # Check for edges:
        # check for x1 views:
        if player['loc'][0] == 1:
            if player['cardinal'] == 'west':
                if status_conditions['blind']:
                    print('''You reach into the hatch, but it is just a void''')
                else:
                    print(ms_edge_test_view_outerwall)
                edge = True
        # check for x26 views:
        if player['loc'][0] == 26:
            if player['cardinal'] == 'east':
                if status_conditions['blind']:
                    print('''You reach into the hatch, but it is just a void''')
                else:
                    print(ms_edge_test_view_outerwall)
                edge = True
        # check for y1 views:
        if player['loc'][1] == 1:
            if player['cardinal'] == 'north':
                if status_conditions['blind']:
                    print('''You reach into the hatch, but it is just a void''')
                else:
                    print(ms_edge_test_view_outerwall)
                edge = True
        # check for y26 views:
        if player['loc'][1] == 26:
            if player['cardinal'] == 'south':
                if status_conditions['blind']:
                    print('''You reach into the hatch, but it is just a void''')
                else:
                    print(ms_edge_test_view_outerwall)
                edge = True
        # check for z1 views:
        if player['loc'][2] == 1:
            if player['cardinal'] == 'down':
                if status_conditions['blind']:
                    print('''You reach into the hatch, but it is just a void''')
                else:
                    print(ms_edge_test_view_outerwall)
                edge = True
        # check for z26 views:
        if player['loc'][2] == 26:
            if player['cardinal'] == 'up':
                if status_conditions['blind']:
                    print('''You reach into the hatch, but it is just a void''')
                else:
                    print(ms_edge_test_view_outerwall)
                edge = True
    return edge


def describe_room():
    """Describe the room's colour and the status of hatches; this is nested in the center() function."""
    open_hatches = []
    closed_hatches = []
    # If the player is in a black room (bridge extended, or dock while bridge is extended), they won't be able to see the hatch status:
    if rooms['{}'.format(player['loc'])]['colour'] == 'pitch black':
        print(ms_describe_room_black)
        return
    else:
        for key in rooms['{}'.format(player['loc'])]:
            if rooms['{}'.format(player['loc'])][key] == 'open':
                open_hatches.append(key)
            elif rooms['{}'.format(player['loc'])][key] == 'closed':
                closed_hatches.append(key)
        if open_hatches and closed_hatches:
            print(ms_describe_room_openclose.format(rooms['{}'.format(player['loc'])]['colour'],open_hatches,closed_hatches))
        elif open_hatches and not closed_hatches:
            print(ms_describe_room_open.format(rooms['{}'.format(player['loc'])]['colour']))
        elif closed_hatches and not open_hatches:
            print(ms_describe_room_closed.format(rooms['{}'.format(player['loc'])]['colour']))
        colour_impression()
        return


### Action Positions ###


def center():
    """Define actions available while in the center of a room."""
    # From the center, the player can look around (approach a wall, floor or ceiling), or use a skill
    # Run the trap function in the rooms that might be trapped:
    if rooms['{}'.format(player['loc'])]['trap']:
        trap()
    if not status_conditions['blind']:
        describe_room()
    elif status_conditions['blind']:
        '''(I can't see anything, but I still have a sense of direction, and I'm roughly in the middle of a room)'''
    while True:
        ms_looking_Call('ms_center_lookaround')
        print(ms_center_baseskill)
        for key in base_skills_center:
            print(ms_center_eachBaseSkill.format(key, base_skills_center[key]))
        response = input(ms_center_lookaround_react)
        # 'teleport' for location bug testing
        if player['job'] == 'X' and response == 'tele':
            destX = int(input('Enter xx:'))
            destY = int(input('Enter yy:'))
            destZ = int(input('Enter zz:'))
            newLoc = [destX,destY,destZ]
            generate_room(newLoc)
            player['loc'] = newLoc
            return
        # 'trap' for trap bug testing
        elif player['job'] == 'X' and response == 'trap':
            print(rooms['{}'.format(player['loc'])]['trap'])
        # 'exit' for the exit hash
        elif player['job'] == 'X' and response == 'exit':
            print(bridge_extended_position_id)
        # 'teletrap' for teleporting to a new room, then choosing the room colour, and the room will be trapped based on that colour
        elif player['job'] == 'X' and response == 'teletrap':
            destX = int(input('Enter xx:'))
            destY = int(input('Enter yy:'))
            destZ = int(input('Enter zz:'))
            newLoc = [destX,destY,destZ]
            generate_room_trap(newLoc)
            player['loc'] = newLoc
            return
        # 'play' for player stats
        elif player['job'] == 'X' and response == 'play':
            print(player)
        # 'hurt' to damage yourself
        elif player['job'] == 'X' and response == 'hurt':
            player['energy'] -= int(input('How much?: '))
            time_update(1)
        elif player['job'] == 'X' and response == 'conf':
            status_conditions['confused'] = True
        # cardinal point responses:
        if response.strip().lower() in ['n','e','s','w', '?']:
            # update the player cardinal and position based on the selection
            if response.strip().lower() == 'n':
                player['cardinal'] = 'north'
                player['position'] = 'wall'
                if player['loc'] != bridge_extended_position:
                    time_update(action_cost[response.strip().lower()])
                return
            elif response.strip().lower() == 'e':
                player['cardinal'] = 'east'
                player['position'] = 'wall'
                if player['loc'] != bridge_extended_position:
                    time_update(action_cost[response.strip().lower()])
                return
            elif response.strip().lower() == 's':
                player['cardinal'] = 'south'
                player['position'] = 'wall'
                if player['loc'] != bridge_extended_position:
                    time_update(action_cost[response.strip().lower()])
                return
            elif response.strip().lower() == 'w':
                player['cardinal'] = 'west'
                player['position'] = 'wall'
                if player['loc'] != bridge_extended_position:
                    time_update(action_cost[response.strip().lower()])
                return
            elif response.strip() == '?':
                player['cardinal'] = random.choice(['north','east','south','west'])
                player['position'] = 'wall'
                if player['loc'] != bridge_extended_position:
                    time_update(action_cost[response.strip().lower()])
                return
        elif response.strip().lower() == 'u':
            player['cardinal'] = 'up'
            player['position'] = 'wall'
            if player['loc'] != bridge_extended_position:
                time_update(action_cost[response.strip().lower()])
            return
        elif response.strip().lower() == 'd':
            player['cardinal'] = 'down'
            player['position'] = 'wall'
            if player['loc'] != bridge_extended_position:
                time_update(action_cost[response.strip().lower()])
            return
        # mind map:
        elif response.strip().lower() == 'm':
            print(mental_map())
            if player['loc'] != bridge_extended_position:
                time_update(action_cost[response.strip().lower()])
        # rest: (needs update to be a function that heals rather than just time passing)
        elif response.strip().lower() == 'r':
            if player['loc'] != bridge_extended_position:
                print('''You dozed off for about half an hour''')
                time_update(action_cost[response.strip().lower()])
            # if you are in the bridge extended position, you won't be able to rest (too excited):
            else:
                print('''(I can't rest at a time like this...)''')
        # first aid:
        elif response.strip().lower() == 'f':
            first_aid()
            if player['loc'] != bridge_extended_position:
                time_update(action_cost[response.strip().lower()])



def wall():
    """Describe actions available while standing at a wall, lookup at a ceiling or looking down at the floor."""
    # If the player is in the extended bridge, time will stop passing (to prevent the bridge from moving while the player is in the bridge)
    # From a wall, the player can inspect a hatch, open/close a hatch, enter a hatch, or return to the center
    global powder_recovery
    if player['cardinal'] in ['north','east','south','west']:
        ms_looking_Call('ms_wall_at_wall')
    elif player['cardinal'] == 'up':
        ms_looking_Call('ms_wall_at_ceiling')
    elif player['cardinal'] == 'down':
        ms_looking_Call('ms_wall_at_floor')
    while True:
        print(ms_wall_hatch_status.format(rooms['{}'.format(player['loc'])][player['cardinal']]))
        # if the hatch is closed...
        if rooms['{}'.format(player['loc'])][player['cardinal']] == 'closed':
            # open hatch, or go back to centre
            while True:
                print(ms_wall_open_or_return)
                response = input(ms_mulling)
                if response.strip().lower() == 'o':
                    rooms['{}'.format(player['loc'])][player['cardinal']] = 'open'
                    print(ms_open_hatch)
                    if player['loc'] != bridge_extended_position:
                        time_update(action_cost[response.strip().lower()])
                    break
                elif response.strip().lower() == 'h':
                    player['position'] = 'center'
                    print(ms_back_away_from_hatch)
                    if player['loc'] != bridge_extended_position:
                        time_update(action_cost[response.strip().lower()])
                    return
        else:
            # If the hatch is open...
            # If the hatch leads to a void: print the appropriate void message (handled by edge_test()), then: close the hatch, go back to centre, or inspect the hatch number.
            edge = edge_test()
            if edge:
                while True:
                    print(ms_wall_close_center_number)
                    response = input(ms_mulling)
                    if response.strip().lower() == 'c':
                        rooms['{}'.format(player['loc'])][player['cardinal']] = 'closed'
                        print(ms_close_hatch)
                        if player['loc'] != bridge_extended_position:
                            time_update(action_cost[response.strip().lower()])
                        break
                    elif response.strip().lower() == 'h':
                        player['position'] = 'center'
                        print(ms_back_away_from_hatch)
                        if player['loc'] != bridge_extended_position:
                            time_update(action_cost[response.strip().lower()])
                        return
                    elif response.strip().lower() == '#':
                        print(ms_engraving.format(rooms['{}'.format(player['loc'])]['id']))
                        number_impression()
                        if player['loc'] != bridge_extended_position:
                            time_update(action_cost[response.strip().lower()])
                        return
            # Else if the hatch does not lead to a void: close the hatch, go back to centre, inspect the hatch number, or crawl into the hatch
            else:
                ## Colour Preview System
                # Get the destination...
                direction = player['cardinal']
                destination = player['loc'][:]
                if direction == 'north':
                    destination[1] -= 1
                elif direction == 'east':
                    destination[0] += 1
                elif direction == 'south':
                    destination[1]  += 1
                elif direction == 'west':
                    destination[0] -= 1
                elif direction == 'up':
                    destination[2] += 1
                elif direction == 'down':
                    destination[2] -= 1
                # Get the external hatch...
                external_hatch = None
                if player['cardinal'] == 'north':
                    external_hatch = 'south'
                elif player['cardinal'] == 'south':
                    external_hatch = 'north'
                elif player['cardinal'] == 'east':
                    external_hatch = 'west'
                elif player['cardinal'] == 'west':
                    external_hatch = 'east'
                elif player['cardinal'] == 'up':
                    external_hatch = 'down'
                elif player['cardinal'] == 'down':
                    external_hatch = 'up'
                # if hatch you're in front of, and the next hatch in that direction are both open, then get a preview of the room colour:
                # Try, because it will fail if the destination room hasn't been generated yet:
                try:
                    if rooms['{}'.format(player['loc'])][player['cardinal']] == 'open' and rooms['{}'.format(destination)][external_hatch] == 'open':
                        print('''(Both the hatches are open, and there's a {} room through the other side)'''.format(rooms['{}'.format(destination)]['colour']))
                except:
                    pass
                while True:
                    if player['cardinal'] in ['north','east','south','west']:
                        print(ms_wall_close_number_center_crawlInto)
                    elif player['cardinal'] == 'up':
                        print(ms_wall_close_number_center_climbUp)
                    elif player['cardinal'] == 'down':
                        print(ms_wall_hatch_number_center_climbDown)
                    response = input('''\n(Okay...)>> ''')
                    if response.strip().lower() == 'c':
                        rooms['{}'.format(player['loc'])][player['cardinal']] = 'closed'
                        print(ms_close_hatch)
                        if player['loc'] != bridge_extended_position:
                            time_update(action_cost[response.strip().lower()])
                        break
                    elif response.strip().lower() == 'h':
                        player['position'] = 'center'
                        print(ms_back_away_from_hatch)
                        if player['loc'] != bridge_extended_position:
                            time_update(action_cost[response.strip().lower()])
                        return
                    elif response.strip().lower() == '#':
                        print(ms_engraving.format(rooms['{}'.format(player['loc'])]['id']))
                        number_impression()
                        if player['loc'] != bridge_extended_position:
                            time_update(action_cost[response.strip().lower()])
                    elif response.strip().lower() == 'i':
                        player['position'] = 'in hatch'
                        if player['cardinal'] in ['north','east','south','west']:
                            print(ms_wall_crawl_into_hatch)
                        elif player['cardinal'] == 'up':
                            print(ms_wall_climb_up_into_hatch)
                        elif player['cardinal'] == 'down':
                            print(ms_wall_climb_down_into_hatch)
                        if player['loc'] != bridge_extended_position:
                            time_update(action_cost[response.strip().lower()])
                        # If the player is powdered, increment the powder recovery counter:
                        if status_conditions['powder']:
                            powder_recovery += 1
                            # if the powder recovery counter reaches 10, recover from powder, and reset the counter:
                            if powder_recovery >= 10:
                                status_conditions['powder'] = False
                                print('''(The powder has finally rubbed off...)''')
                                powder_recovery = 0
                        # If the player is not powdered, reset the powder recovery counter:
                        else:
                            powder_recovery = 0
                        return


def in_hatch():
    """Describe actions available while in a hatch."""
    # While in a hatch, the player can exit back from the hatch, inspect the hatch, open/close the external hatch, or advance to the next room.
    # If the player is in the extended bridge, time will stop passing (to prevent the bridge from moving while the player is in the bridge)
    # This is the only position from which the player may enter the sanctum (the solution), if they are in the bridge extended position and moving in the right direction.
    # check what direction the player came from, and generate a room in the direction they are going (unless they are going into the sanctum) (edge testing is already handled within edge_test() and wall()).
    global powder_recovery
    global hatch_movements

    sanctum_hatch = False

    # check if the player is in the bridge while it is extended:
    if player['loc'] == bridge_extended_position:
    # check each of the bridge extended positions to see what hatch leads to the sanctum:
        # check for Penthouse:
        if bridge_extended_position[2] == 27:
            if player['cardinal'] == 'up':
                sanctum_hatch = True
        # check for Basement views:
        elif bridge_extended_position[2] == 0:
            if player['cardinal'] == 'down':
                sanctum_hatch = True
        # check for North Balcony views:
        elif bridge_extended_position[1] == 0:
            if player['cardinal'] == 'north':
                sanctum_hatch = True
        # check for South Balcony views:
        elif bridge_extended_position[1] == 27:
            if player['cardinal'] == 'south':
                sanctum_hatch = True
        # check for East Balcony views:
        elif bridge_extended_position[0] == 27:
            if player['cardinal'] == 'east':
                sanctum_hatch = True
        # check for West Balcony views:
        elif bridge_extended_position[0] == 0:
            if player['cardinal'] == 'west':
                sanctum_hatch = True

    # if the player is in the sanctum hatch, advancing in their current direction will trigger the sanctum end-game event.
    # time does not advance while in the sanctum hatch
    # The player can crawl back to the center, or advance to the sanctum (there is no external hatch)
    if sanctum_hatch:
        while True:
            print(ms_in_hatch_lightAhead)
            print(ms_in_hatch_goToTheLight)
            response = input(ms_in_hatch_lightReact)
            if response.strip().lower() == 'i':
                player['position'] = 'sanctum'
                return
            elif response.strip().lower() == 'h':
                player['position'] = 'center'
                if player['cardinal'] in ['north','west','east','south']:
                    print(ms_in_hatch_crawlBackOut)
                elif player['cardinal'] == 'up':
                    print(ms_in_hatch_climbDown)
                elif player['cardinal'] == 'down':
                    print(ms_in_hatch_climbBackOut)
                # If the player is powdered, increment the powder recovery counter:
                if status_conditions['powder']:
                    powder_recovery += 1
                    # if the powder recovery counter reaches 10, recover from powder, and reset the counter:
                    if powder_recovery >= 10:
                        status_conditions['powder'] = False
                        print('''(The powder has finally rubbed off...)''')
                        powder_recovery = 0
                # If the player is not powdered, reset the powder recovery counter:
                else:
                    powder_recovery = 0
                return

    external_hatch = None
    # set the external_hatch orientation as the opposite of the player's current direction
    if player['cardinal'] == 'north':
        external_hatch = 'south'
    elif player['cardinal'] == 'south':
        external_hatch = 'north'
    elif player['cardinal'] == 'east':
        external_hatch = 'west'
    elif player['cardinal'] == 'west':
        external_hatch = 'east'
    elif player['cardinal'] == 'up':
        external_hatch = 'down'
    elif player['cardinal'] == 'down':
        external_hatch = 'up'

    direction = player['cardinal']
    # make a copy of the player's location
    destination = player['loc'][:]
    # increment the destination based on the player's direction of movement
    if direction == 'north':
        destination[1] -= 1
    elif direction == 'east':
        destination[0] += 1
    elif direction == 'south':
        destination[1]  += 1
    elif direction == 'west':
        destination[0] -= 1
    elif direction == 'up':
        destination[2] += 1
    elif direction == 'down':
        destination[2] -= 1
    # generate a new room at the destination
    generate_room(destination)

    # If the external hatch is closed: crawl back to the room you started in, inspect the external hatch number, or open the external hatch
    if rooms['{}'.format(destination)][external_hatch] == 'closed':
        while True:
            if player['cardinal'] in ['north','east','south','west']:
                print(ms_in_hatch_open_number_crawlBackOut)
            elif player['cardinal'] == 'up':
                print(ms_in_hatch_open_number_crawlDownOut)
            elif player['cardinal'] == 'down':
                print(ms_in_hatch_open_number_climbUpOut)
            response = input(ms_mulling)
            if response.strip().lower() == 'o':
                rooms['{}'.format(destination)][external_hatch] = 'open'
                print(ms_open_hatch)
                if player['loc'] != bridge_extended_position:
                    time_update(action_cost[response.strip().lower()])
                break
            elif response.strip().lower() == 'h':
                player['position'] = 'center'
                if player['cardinal'] in ['north','west','east','south']:
                    print(ms_in_hatch_crawlBackOut)
                elif player['cardinal'] == 'up':
                    print(ms_in_hatch_climbDown)
                elif player['cardinal'] == 'down':
                    print(ms_in_hatch_climbBackOut)
                if player['loc'] != bridge_extended_position:
                    time_update(action_cost[response.strip().lower()])
                # If the player is powdered, increment the powder recovery counter:
                if status_conditions['powder']:
                    powder_recovery += 1
                    # if the powder recovery counter reaches 10, recover from powder, and reset the counter:
                    if powder_recovery >= 10:
                        status_conditions['powder'] = False
                        print('''(The powder has finally rubbed off...)''')
                        powder_recovery = 0
                # If the player is not powdered, reset the powder recovery counter:
                else:
                    powder_recovery = 0
                return
            elif response.strip().lower() == '#':
                print(ms_in_hatch_external_engraving.format(rooms['{}'.format(destination)]['id']))
                number_impression()
                if player['loc'] != bridge_extended_position:
                    time_update(action_cost[response.strip().lower()])

    # If the external hatch is open: crawl back to the room you started in, inspect the external hatch number, or crawl through the external hatch to the centre of the next room
    elif rooms['{}'.format(destination)][external_hatch] == 'open':
        while True:
            if player['cardinal'] in ['north','east','south','west']:
                print(ms_in_hatch_close_number_crawlOut_crawlInto)
            elif player['cardinal'] == 'up':
                print(ms_in_hatch_close_number_climeDown_climbUp)
            elif player['cardinal'] == 'down':
                print(ms_in_hatch_close_number_climbUp_climbDown)
            response = input(ms_mulling)
            if response.strip().lower() == 'c':
                rooms['{}'.format(destination)][external_hatch] = 'closed'
                print(ms_close_hatch)
                if player['loc'] != bridge_extended_position:
                    time_update(action_cost[response.strip().lower()])
                break
            elif response.strip().lower() == 'h':
                player['position'] = 'center'
                if player['cardinal'] in ['north','west','east','south']:
                    print(ms_in_hatch_crawlBackOut)
                elif player['cardinal'] == 'up':
                    print(ms_in_hatch_climbDown)
                elif player['cardinal'] == 'down':
                    print(ms_in_hatch_climbBackOut)
                if player['loc'] != bridge_extended_position:
                    time_update(action_cost[response.strip().lower()])
                # If the player is powdered, increment the powder recovery counter:
                if status_conditions['powder']:
                    powder_recovery += 1
                    # if the powder recovery counter reaches 10, recover from powder, and reset the counter:
                    if powder_recovery >= 10:
                        status_conditions['powder'] = False
                        print('''(The powder has finally rubbed off...)''')
                        powder_recovery = 0
                # If the player is not powdered, reset the powder recovery counter:
                else:
                    powder_recovery = 0
                return
            elif response.strip().lower() == '#':
                print(ms_in_hatch_external_engraving.format(rooms['{}'.format(destination)]['id']))
                number_impression()
                if player['loc'] != bridge_extended_position:
                    time_update(action_cost[response.strip().lower()])
            elif response.strip().lower() == 'i':
                player['loc'] = destination
                player['position'] = 'center'
                hatch_movements.append(player['cardinal'])
                print(ms_in_hatch_nextRoom)
                if player['loc'] != bridge_extended_position:
                    time_update(action_cost[response.strip().lower()])
                # If the player is powdered, increment the powder recovery counter:
                if status_conditions['powder']:
                    powder_recovery += 1
                    # if the powder recovery counter reaches 10, recover from powder, and reset the counter:
                    if powder_recovery >= 10:
                        status_conditions['powder'] = False
                        print('''(The powder has finally rubbed off...)''')
                        powder_recovery = 0
                # If the player is not powdered, reset the powder recovery counter:
                else:
                    powder_recovery = 0
                return


def sanctum():
    '''This is the final room of the game, there is no returning from this point'''
    # Only one character can enter this room, then a hidden hatch shuts behind them:
    fail = False
    print('''You advanced into the light...\nYou stagger forward, unable to see anything except for the blinding light ahead, like staring into the sun...''')
    print('''A hatch slams shut behind you...\n''')
    # A booming voice asks for your name:
    print('''WHAT IS YOUR NAME?''')
    name_response = input('''(My name is...)>> ''')
    if name_response.strip().title() != player['name']:
        exit('''YOU LIED TO GOD, YOU WILL BURN FOR YOUR SINS (the room was engulfed in flames)''')
    else:
        print('''DO YOU BELIEVE IN GOD?''')
    god_response = input('''(The voice expects a firm yes <y> or no <n>...''')
    if god_response.strip().lower() not in ['yes','y']:
        exit('''YOU DENIED GOD, YOU WILL BURN FOR YOUR SINS (the room was engulfed in flames)''')
    else:
        print('''YOU WILL SERVE GOD''')
        print('''The blinding light faded, you are in a room surrounded by monitors, each with a view of a coloured, cube-like room...''')
    exit('''Thank you, {}, for playing Cube Part 1!'''.format(player['name']))


### Time updates:


def time_update(time):
    """Update global time and trigger all time-based events. Call this function whenever time should pass."""
    global global_time
    global bridge_room_time
    global bridge_made_noise
    global last_heard_bridge
    global bridge_cycle
    global bridge_current_position
    global bridge_positions
    global black_seen
    global confusion_recovery
    global blind_recovery
    global powder_recovery
    global_time += time

    # if the bridge has made a noise, then the 'last heard bridge' will increment by the time that just passed:
    if bridge_made_noise:
        last_heard_bridge += time

    ## Bridge Movement System (the bridge only actually moves into and out of the extended position, the other 'moves' are virtual and are represented by colour change to pitch black:
    bridge_room_time += time
    # whenever the bridge room time reaches or exceeds 30...
    if bridge_room_time >= 30:
        # reset the bridge movement counter by subtracting 30 from it
        bridge_room_time -= 30
        # then, if the bridge is not in position 6 (the last position), then increment its position
        if bridge_cycle < 6:
            bridge_cycle += 1
        # if the bridge is in position 6, then move it back to the starting position (position 0)
        else:
            bridge_cycle = 0
        # move the bridge into the next position in the cycle
        bridge_current_position = bridge_positions[bridge_cycle]
        # the room turns black when it moves into the player's position (the room only changes to black if they player is present)
        if player['loc'] == bridge_current_position and bridge_current_position != bridge_extended_position:
            # if the room has not already become pitch black:
            if rooms['{}'.format(player['loc'])]['colour'] != 'pitch black':
                print(ms_time_update_fadeToBlack)
                # change the room colour to pitch black
                rooms['{}'.format(player['loc'])]['colour'] = 'pitch black'
                # activate the black impression:
                if not black_seen:
                    print(ms_black_impression)
                black_seen = True
        # if the player is in a pitch black room and the virtual bridge moves away from that room, the room will return to purple:
        if rooms['{}'.format(player['loc'])]['colour'] == 'pitch black' and player['loc'] != bridge_current_position:
            rooms['{}'.format(player['loc'])]['colour'] = 'purple'
            print(ms_time_update_backToPurple)

        ## Bridge Noise System (The bridge will make noise when it arrives at the extended position, and leaves the extended position)
        # The 'last heard bridge' will reset to 1 whenever the bridge noise is heard:
        noise_intensity = False
        bridge_arrived = False
        bridge_departed = False
        # Check if the bridge has just moved into the extended position:
        if bridge_current_position == bridge_extended_position:
            last_heard_bridge = 1
            bridge_made_noise = True
            noise_intensity = True
            bridge_arrived = True
        # Check if the bridge has just moved from the extended position to the next point in the cycle:
        # First, check if the bridge cycle is at the start, and the bridge extended position is position six:
        elif bridge_cycle == 0 and bridge_positions.index(bridge_extended_position) == 6:
            last_heard_bridge = 1
            bridge_made_noise = True
            noise_intensity = True
            bridge_departed = True
        # Then, check if the bridge cycle is one position ahead of the bridge extened position:
        elif bridge_cycle - bridge_positions.index(bridge_extended_position) == 1:
            last_heard_bridge = 1
            bridge_made_noise = True
            noise_intensity = True
            bridge_departed = True
        # if any of the noise conditions are triggered, the noise intensity will be checked:
        if noise_intensity:
            # The noise intensity is based on proximity to the player (measured as difference in each of x[0],y[1],z[2] values from bridge position)
            # if the player is within one room of the bridge extended position:
            if -1 <= player['loc'][0] - bridge_extended_position[0] <= 1 and -1 <= player['loc'][1] - bridge_extended_position[1] <= 1 and -1 <= player['loc'][2] - bridge_extended_position[2] <= 1:
                print(ms_time_update_noise1)
                if bridge_arrived:
                    print('''It sounded like the noise was getting closer''')
                elif bridge_departed:
                    print('''It sounded like the noise was moving further away''')
            # if the player is within four rooms of the bridge extended position:
            elif -4 <= player['loc'][0] - bridge_extended_position[0] <= 4 and -4 <= player['loc'][1] - bridge_extended_position[1] <= 4 and -4 <= player['loc'][2] - bridge_extended_position[2] <= 4:
                print(ms_time_update_noise4)
                if bridge_arrived:
                    print('''It sounded like the noise was getting closer''')
                elif bridge_departed:
                    print('''It sounded like the noise was moving further away''')
            # if the player is within seven rooms of the bridge extended position:
            elif -7 <= player['loc'][0] - bridge_extended_position[0] <= 7 and -7 <= player['loc'][1] - bridge_extended_position[1] <= 7 and -7 <= player['loc'][2] - bridge_extended_position[2] <= 7:
                print(ms_time_update_noise7)
                if bridge_arrived:
                    print('''It sounded like the noise was getting closer''')
                elif bridge_departed:
                    print('''It sounded like the noise was moving further away''')
                # Noise that is at lease this intense will trigger sound-activated traps:
                if rooms['{}'.format(player['loc'])]['trap']['trigger'] == 'sound':
                    xxx
            # if the player is within ten rooms of the bridge extended position:
            elif -10 <= player['loc'][0] - bridge_extended_position[0] <= 10 and -10 <= player['loc'][1] - bridge_extended_position[1] <= 10 and -10 <= player['loc'][2] - bridge_extended_position[2] <= 10:
                print(ms_time_update_noise10)
                if bridge_arrived:
                    print('''It sounded like the noise was getting closer''')
                elif bridge_departed:
                    print('''It sounded like the noise was moving further away''')
            # if the player is within thirteen rooms of the bridge extended position:
            elif -13 <= player['loc'][0] - bridge_extended_position[0] <= 13 and -13 <= player['loc'][1] - bridge_extended_position[1] <= 13 and -13 <= player['loc'][2] - bridge_extended_position[2] <= 13:
                print(ms_time_update_noise13)
                if bridge_arrived:
                    print('''It sounded like the noise was getting closer''')
                elif bridge_departed:
                    print('''It sounded like the noise was moving further away''')

    ## Trap Timed Reset System
    # For every room that exists so far:
    for room in rooms:
        # if it is not a safe room:
        if rooms['{}'.format(room)]['trap']:
            # check if that room's trap has not already reset:
            if rooms['{}'.format(room)]['trap']['reset'] > 0:
                # reduce the reset time by the time that just passed:
                rooms['{}'.format(room)]['trap']['reset'] -= time
                # if the reset time ends up below zero, reset it to zero:
                if rooms['{}'.format(room)]['trap']['reset'] < 0:
                    rooms['{}'.format(room)]['trap']['reset'] = 0

    ## Status Recovery System
    # Confusion:
    # If the player is confused, increment the confusion recovery counter:
    if status_conditions['confused']:
        confusion_recovery += time
        # if the confusion recovery counter reaches two hours, recover from confusion, and reset the counter:
        if confusion_recovery >= 120:
            status_conditions['confused'] = False
            print('''(The fog in my mind has cleared...)''')
            confusion_recovery = 0
    # If the player is not confused, reset the confusion recovery counter:
    else:
        confusion_recovery = 0
    # Blindness:
    # If the player is blind, increment the blind recovery counter:
    if status_conditions['blind']:
        blind_recovery += time
        # if the blind recovery counter reaches two hours, recover from blindness, and reset the counter:
        if blind_recovery >= 120:
            status_conditions['blind'] = False
            print('''(My eyes have stopped burning, I can see again...)''')
            blind_recovery = 0
    # If the player is not blind, reset the blind recovery counter:
    else:
        blind_recovery = 0
    # Powder:
    # Handled by movement hatch to center, or wall to hatch


    ## Fatigue System
    #  Calculate Ailment Factor:
    ailment_factor = 1
    if status_conditions['bleeding']:
        ailment_factor += 1
    if status_conditions['burned']:
        ailment_factor += 1
    # Check if player is resting: (time == 30), only reduce energy by 15 (ignore Ailment Factor)
    if time == 30:
        player['energy'] -= 15
    # Apply fatigue (player energy decreases with every action; every action causes time to pass)
    else:
        player['energy'] = player['energy'] - time * ailment_factor
    # Apply Confusion if energy is below 10% of starting value:
    if player['energy'] < starting_energy / 10:
        status_conditions['confused'] = True
    # Player dies if energy reaches zero:
    if player['energy'] <= 0:
        exit(ms_energy_death)


### Introduction message:


def introduction():
    print(ms_introduction_wakeUpDrank.format(rooms['{}'.format(player['loc'])]['colour']))
    while True:
        name = input(ms_introduction_OhNaNaWhatsMyName)
        name = name.strip().title()
        if name:
            player['name'] = name
            print(ms_introduction_details_returning.format(player['name']))
            print(ms_introduction_something_important)
            job_list = []
            for key in job_skills:
                job_list.append(key)
            for i in range(0,len(job_list)-1):
                if job_list[i] != 'X':
                    print('''{}?...'''.format(job_list[i]))
            print(ms_introduction_dont_tell_me.format(job_list[~0]))
            while True:
                job = input(ms_introduction_job_react)
                job = job.strip().title()
                if job in job_skills:
                    player['job'] = job
                    if player['job'] != 'X':
                        print(ms_introduction_former_job.format(player['job']))
                    # If x is entered, print the Researcher message (this is a cheat confirmation, it should be made more difficult to access when the game is released)
                    else:
                        print('''Welcome, Researcher {}'''.format(player['name']))
                    if player['job'] == 'Police Officer':
                        player['energy'] = 5760
                    else:
                        player['energy'] = 4320
                    time_update(5)
                    return
                else:
                    print(ms_introduction_wrong_job)
        else:
            print(ms_introduction_think_of_something)


##### START GAME #####


while True:
    if global_time == 0:
        player['loc'] = starting_loc
        generate_room(player['loc'])
        introduction()
    if player['position'] == 'center':
        center()
    elif player['position'] == 'wall':
        wall()
    elif player['position'] == 'in hatch':
        in_hatch()
    elif player['position'] == 'sanctum':
        sanctum()
