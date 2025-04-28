import random

def block_1(context: dict) -> dict:
    context['random_number'] = random.randint(1, 6)
    return context