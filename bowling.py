
def get_value(char):
    if char != '0' and char.isdigit():
        return int(char)
    elif char == 'X' or char == 'x':
        return 10
    elif char == '/':
        return 10
    elif char == '-':
        return 0
    else:
        raise ValueError()


def score(game):
    result = 0
    frame = 1
    in_first_roll = True
    max_value = 10
    max_frame = 10
    for i in range(len(game)):
        if game[i] == '/':
            result += max_value - last_score
        else:
            result += get_value(game[i])
        if frame < max_frame and get_value(game[i]) == max_value:
            if game[i] == '/':
                result += get_value(game[i+1])
            elif game[i] == 'X' or game[i] == 'x':
                result += get_value(game[i+1])
                if game[i+2] == '/':
                    result += max_value - get_value(game[i+1])
                else:
                    result += get_value(game[i+2])
        last_score = get_value(game[i])
        if not in_first_roll:
            in_first_roll = True
            frame += 1
        else:
            in_first_roll = False
        if game[i] == 'X' or game[i] == 'x':
            in_first_roll = True
            frame += 1
    return result

