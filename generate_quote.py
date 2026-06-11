import random

def get_quote():
    with open("quotes.txt","r",encoding="utf-8") as f:
        quotes = f.readlines()

    return random.choice(quotes).strip()
