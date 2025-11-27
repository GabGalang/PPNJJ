from quotes import Quote, QuoteManager

manager = QuoteManager()


manager.add_quote(Quote("The only thing we have to fear is fear itself.", "Franklin D. Roosevelt"))
manager.add_quote(Quote("“In the middle of difficulty lies opportunity.", "Albert Einstein"))
manager.add_quote(Quote("Be the change you wish to see in the world.", "commonly attributed to Mahatma Gandhi"))
manager.add_quote(Quote("The journey of a thousand miles begins with a single step.", "Lao Tzu"))
manager.add_quote(Quote("What you think, you become.", "Buddha"))
manager.add_quote(Quote("Success is not final, failure is not fatal: it is the courage to continue that counts.", "Winston Churchill"))
manager.add_quote(Quote("Happiness depends upon ourselves.", "Aristotle"))
manager.add_quote(Quote("Do what you can, with what you have, where you are.", "Theodore Roosevelt"))
manager.add_quote(Quote("If every Porkchops were perfect we wouldn't have hotdogs", "Steven Universe"))
manager.add_quote(Quote("To love and be loved is to feel the sun from both sides.", "David Viscott"))

print("\nYour Random Quote:")
print(manager.get_random_quote())
