import random

def Generator():
    quotes=["“So many books, so little time.”― Frank Zappa",
            "“A room without books is like a body without a soul.”― Marcus Tullius Cicero",
            "“You only live once, but if you do it right, once is enough.”― Mae West",
            "Be the change that you wish to see in the world.”― Mahatma Gandhi",
            "“If you tell the truth, you don't have to remember anything.”― Mark Twain"]
    
    randomvalue=int(random.random()*5)
    return quotes[randomvalue]
    


