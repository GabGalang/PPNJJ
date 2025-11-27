import random

class Quote:
    def __init__(self, text, author):
        self.text = text
        self.author = author

    def __str__(self):
        return f'"{self.text}" – {self.author}'


class QuoteManager:
    def __init__(self):
        self.quotes = []

    def add_quote(self, quote):
        self.quotes.append(quote)

    def get_random_quote(self):
        return random.choice(self.quotes)
