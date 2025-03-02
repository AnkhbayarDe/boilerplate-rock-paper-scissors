import random

def player(prev_play, opponent_history=[]):
    if prev_play:
        opponent_history.append(prev_play)

    pattern_count = {}
    pattern_length = 3  


    if len(opponent_history) >= pattern_length:
        for i in range(len(opponent_history) - pattern_length):
            pattern = tuple(opponent_history[i:i + pattern_length])
            next_move = opponent_history[i + pattern_length]

            if pattern not in pattern_count:
                pattern_count[pattern] = {"R": 0, "P": 0, "S": 0}
            pattern_count[pattern][next_move] += 1


        last_pattern = tuple(opponent_history[-pattern_length:])
        if last_pattern in pattern_count:
            predicted_move = max(pattern_count[last_pattern], key=pattern_count[last_pattern].get)
        else:
            predicted_move = random.choice(["R", "P", "S"])
    else:
        predicted_move = random.choice(["R", "P", "S"])


    counter_move = {"R": "P", "P": "S", "S": "R"}
    return counter_move[predicted_move]
