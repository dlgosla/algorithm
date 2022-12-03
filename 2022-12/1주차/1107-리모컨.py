import sys

input = sys.stdin.readline


def is_possible_move_to(channel):
    global broken_numbers

    for number in str(channel):
        if number in broken_numbers:
            return False

    return True


def calculate_move_count(curr_channel):
    global target_channel

    return abs(target_channel - curr_channel) + len(str(curr_channel))


target_channel = int(input())
number_of_broken_buttons = int(input())

broken_numbers = []
if number_of_broken_buttons:
    broken_numbers = input().split()

up_channel = target_channel
down_channel = target_channel

init_count = abs(target_channel - 100)
min_move_count = init_count

if is_possible_move_to(target_channel):
    min_move_count = min(calculate_move_count(target_channel), min_move_count)

else:
    while True:
        up_channel += 1
        down_channel -= 1

        found = False

        up_channel_count = calculate_move_count(up_channel)
        down_channel_count = calculate_move_count(down_channel)

        if up_channel_count > init_count:
            break

        if is_possible_move_to(up_channel):
            min_move_count = min(up_channel_count, min_move_count)
            found = True

        if down_channel >= 0 and is_possible_move_to(down_channel):
            min_move_count = min(down_channel_count, min_move_count)
            found = True

        if found:
            break

print(min_move_count)
