"""Wordle time !"""

__author__ = "730600257"


def main() -> None:
    """The start of the game and main loop"""
    secret_word = "codes"
    secret_length = len(secret_word)
    num_turns = 0
    game_won = False
    max_turns = 6

    while num_turns < max_turns and not game_won:
        num_turns += 1
        print(f"=== Turn {num_turns}/{max_turns} ===")
        user_guess = input_guess(secret_length)
        codified_result = emojified(user_guess, secret_word)
        print(codified_result)
        if user_guess == secret_word:
            game_won = True
    if game_won:
        print(f"You won in {num_turns}/{max_turns} turns!")
    else:
        print(f"{'X'}/{max_turns} - Sorry, try again tomorrow!")

def contains_char(first_string, single_char):
    """seeing if a character is in a string :))"""
    assert len(single_char) == 1
    return single_char in first_string

def emojified(guess_word, secret_word):
    assert len(guess_word) == len(secret_word)
    boxes: str = ""
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    for guess_char, secret_char in zip(guess_word, secret_word):
        if guess_char == secret_char:
            boxes += GREEN_BOX
        elif contains_char(secret_word, guess_char):
            boxes += YELLOW_BOX
        else:
            boxes += WHITE_BOX
        
    return boxes

def input_guess(expected_length):
    user_guess = str(input(f"Enter a {expected_length} character word: "))
    while len(user_guess) != expected_length:
       user_guess = str(input(f"That wasn't {expected_length} chars! Try again: "))
    while len(user_guess) == expected_length:
        return user_guess
    
if __name__ == "__main__":
    main()