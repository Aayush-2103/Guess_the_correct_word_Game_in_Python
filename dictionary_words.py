from english_dictionary.scripts.read_pickle import get_dict
import random

def generate_random_word():
    english_dict = get_dict()
    random_word = random.choice(list(english_dict.keys()))
    meaning = english_dict[random_word]

    word_dict = {
        "word": random_word,
        "meaning": meaning
    }

    return word_dict

