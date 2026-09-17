screen_precision = 0
console_precision = 0
FWD = Event()
LT = Event()
RT = Event()
current_space_number = 0
dice1 = 0
dice2 = 0
Spaces_to_move = 0
properties_visited = 0
turn_counter = 0
in_jail = 0
jail_turns = 0
money = 0

def roll_dice():
    global FWD, LT, RT, my_event, current_space_number, dice1, dice2, Spaces_to_move, properties_visited, turn_counter, in_jail, jail_turns, money, screen_precision, console_precision
    if jail_turns == 3:
        in_jail = 0
        money = money + -50
    if in_jail == 1:
        jail_turns = jail_turns + 1
    turn_counter = turn_counter + 1
    dice1 = int(round(urandom.uniform(1, 4), 2))
    brain.screen.print(str("Rolled a:") + str(dice1))
    brain.screen.next_row()
    dice2 = int(round(urandom.uniform(1, 4), 2))
    brain.screen.print(str("Rolled a:") + str(dice2))
    brain.screen.next_row()
    if dice1 == dice2:
        in_jail = 0
    Spaces_to_move = dice1 + dice2
    brain.screen.print(str("Turn ") + str(turn_counter))
    brain.screen.next_row()

def play_game():
    global FWD, LT, RT, my_event, current_space_number, dice1, dice2, Spaces_to_move, properties_visited, turn_counter, in_jail, jail_turns, money, screen_precision, console_precision
    while True:
        roll_dice()
        move()
        complete_task()
        wait(1, SECONDS)
        brain.screen.clear_screen()
        brain.screen.set_cursor(1, 1)
        wait(5, MSEC)

def move():
    global FWD, LT, RT, my_event, current_space_number, dice1, dice2, Spaces_to_move, properties_visited, turn_counter, in_jail, jail_turns, money, screen_precision, console_precision
    brain.screen.print(str("Moving ") + str(str(Spaces_to_move) + str(" spaces!")))
    brain.screen.next_row()
    if in_jail == 0:
        for repeat_count in range(int(Spaces_to_move)):
            FWD.broadcast_and_wait()
            current_space_number = current_space_number + 1
            if current_space_number > 12:
                current_space_number = 1
            if current_space_number == 1:
                RT.broadcast_and_wait()
            if current_space_number == 4:
                RT.broadcast_and_wait()
            if current_space_number == 7:
                RT.broadcast_and_wait()
            if current_space_number == 10:
                RT.broadcast_and_wait()
            wait(5, MSEC)

def complete_task():
    global FWD, LT, RT, my_event, current_space_number, dice1, dice2, Spaces_to_move, properties_visited, turn_counter, in_jail, jail_turns, money, screen_precision, console_precision
    brain.screen.print(str("Landed on space") + str(current_space_number))
    brain.screen.next_row()
    wait(1, SECONDS)
    if current_space_number == 1:
        # Space = GO
        for repeat_count2 in range(4):
            LT.broadcast_and_wait()
            wait(5, MSEC)
    elif current_space_number == 4:
        # Space = Jail
        wait(3, SECONDS)
    elif current_space_number == 7:
        # Space = Free Parking
        wait(5, SECONDS)
    elif current_space_number == 10:
        # Space = Go to Jail
        in_jail = 1
        turn_counter = turn_counter + 3
        RT.broadcast_and_wait()
        for repeat_count3 in range(3):
            FWD.broadcast_and_wait()
            wait(5, MSEC)
        LT.broadcast_and_wait()
        for repeat_count4 in range(3):
            FWD.broadcast_and_wait()
            wait(5, MSEC)
        for repeat_count5 in range(2):
            RT.broadcast_and_wait()
            wait(5, MSEC)
        current_space_number = 4
        wait(1, SECONDS)
    else:
        # Space = Blue 1 or 2, Green 1 or 2, Yellow 1 or 2, or Red 1 or 2
        RT.broadcast_and_wait()
        FWD.broadcast_and_wait()
        for repeat_count6 in range(2):
            LT.broadcast_and_wait()
            wait(5, MSEC)
        FWD.broadcast_and_wait()
        RT.broadcast_and_wait()

def when_started1():
    global FWD, LT, RT, my_event, current_space_number, dice1, dice2, Spaces_to_move, properties_visited, turn_counter, in_jail, jail_turns, money, screen_precision, console_precision
    current_space_number = 1
    play_game()
    turn_counter = 0
    in_jail = 0
    money = 800

def FWD_callback_0():
    global FWD, LT, RT, my_event, current_space_number, dice1, dice2, Spaces_to_move, properties_visited, turn_counter, in_jail, jail_turns, money, screen_precision, console_precision
    motor_1.spin_for(FORWARD, 400, DEGREES)

def FWD_callback_1():
    global FWD, LT, RT, my_event, current_space_number, dice1, dice2, Spaces_to_move, properties_visited, turn_counter, in_jail, jail_turns, money, screen_precision, console_precision
    motor_5.spin_for(REVERSE, -400, DEGREES)

def RT_callback_0():
    global FWD, LT, RT, my_event, current_space_number, dice1, dice2, Spaces_to_move, properties_visited, turn_counter, in_jail, jail_turns, money, screen_precision, console_precision
    motor_1.spin_for(FORWARD, 220, DEGREES)

def RT_callback_1():
    global FWD, LT, RT, my_event, current_space_number, dice1, dice2, Spaces_to_move, properties_visited, turn_counter, in_jail, jail_turns, money, screen_precision, console_precision
    motor_5.spin_for(REVERSE, 220, DEGREES)

def LT_callback_0():
    global FWD, LT, RT, my_event, current_space_number, dice1, dice2, Spaces_to_move, properties_visited, turn_counter, in_jail, jail_turns, money, screen_precision, console_precision
    motor_1.spin_for(FORWARD, -220, DEGREES)

def LT_callback_1():
    global FWD, LT, RT, my_event, current_space_number, dice1, dice2, Spaces_to_move, properties_visited, turn_counter, in_jail, jail_turns, money, screen_precision, console_precision
    motor_5.spin_for(REVERSE, -220, DEGREES)

# system event handlers
FWD(FWD_callback_0)
FWD(FWD_callback_1)
RT(RT_callback_0)
RT(RT_callback_1)
LT(LT_callback_0)
LT(LT_callback_1)
# add 15ms delay to make sure events are registered correctly.
wait(15, MSEC)

when_started1()