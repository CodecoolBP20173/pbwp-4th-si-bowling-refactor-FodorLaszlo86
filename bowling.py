MAX_VALUE = 10
MAX_FRAME = 10


def get_value(char):
    try:
        if char != '0' and char.isdigit():
            return int(char)
        elif char == 'X' or char == 'x' or char == '/':
            return 10
        elif char == '-':
            return 0
    except ValueError:
        return "Not valid Value!"
    

def score(game):
    result = 0
    frame = 1
    in_first_roll = True
    for i in range(len(game)):
        if is_spare(game[i]):
            result += MAX_VALUE - last_score
        else:
            result += get_value(game[i])
        if frame < MAX_FRAME and get_value(game[i]) == MAX_VALUE:
            if is_spare(game[i]):
                result += get_value(game[i+1])
            elif is_strike(game[i]):
                result += get_value(game[i+1])
                if is_spare(game[i+2]):
                    result += MAX_VALUE - get_value(game[i+1])
                else:
                    result += get_value(game[i+2])
        last_score = get_value(game[i])
        if not in_first_roll:
            in_first_roll = True
            frame += 1
        else:
            in_first_roll = False
        if is_strike(game[i]):
            in_first_roll = True
            frame += 1
    return result


def is_strike(frame_result):
    if 'X' == frame_result or 'x' == frame_result:
        return True


def is_spare(frame_result):
    if '/' == frame_result:
        return True
