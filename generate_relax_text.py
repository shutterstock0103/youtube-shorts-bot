import random

texts = [
    "Relax.\nTake a deep breath.\nEverything will be okay.",
    "Slow down.\nEnjoy the moment.",
    "Peace begins with a calm mind.",
    "Breathe.\nRelax.\nSmile.",
    "Rest your mind and embrace the present."
]

def get_relax_text():
    return random.choice(texts)
