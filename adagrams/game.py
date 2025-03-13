from random import randint
LETTER_POOL = {
    'A': 9, 
    'B': 2, 
    'C': 2, 
    'D': 4, 
    'E': 12, 
    'F': 2, 
    'G': 3, 
    'H': 2, 
    'I': 9, 
    'J': 1, 
    'K': 1, 
    'L': 4, 
    'M': 2, 
    'N': 6, 
    'O': 8, 
    'P': 2, 
    'Q': 1, 
    'R': 6, 
    'S': 4, 
    'T': 6, 
    'U': 4, 
    'V': 2, 
    'W': 2, 
    'X': 1, 
    'Y': 2, 
    'Z': 1
}

def draw_letters():
    letter = []
    letter_count = 0
    key_list = list(LETTER_POOL.keys())
    value_list = list(LETTER_POOL.values())

    while letter_count < 10:
        letter_count += 1
        random_index = randint(0, 25)

        if value_list[random_index] > 0:
            letter.append(key_list[random_index])
            value_list[random_index] -= 1
        else:
            continue
        
        
    return letter

draw_letters()   


def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass