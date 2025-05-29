from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base, Player, Game, Roll
from datetime import datetime
import random

engine = create_engine('sqlite:///dice_game.db')
Session = sessionmaker(bind=engine)
session = Session()

def roll_dice():
    return random.randint(1, 6), random.randint(1, 6)

def display_dice(d1, d2):
    dice_art = {
        1: ["│     │", "│  ●  │", "│     │"],
        2: ["│ ●   │", "│     │", "│   ● │"],
        3: ["│ ●   │", "│  ●  │", "│   ● │"],
        4: ["│ ● ● │", "│     │", "│ ● ● │"],
        5: ["│ ● ● │", "│  ●  │", "│ ● ● │"],
        6: ["│ ● ● │", "│ ● ● │", "│ ● ● │"],
    }

    print("┌─────┐   ┌─────┐")
    for i in range(3):
        print(f"{dice_art[d1][i]}   {dice_art[d2][i]}")
    print("└─────┘   └─────┘")

def main():
    print("Welcome to the Dice Game Roller!")
    name = input("Enter your name: ").strip()

    player = session.query(Player).filter_by(name=name).first()
    if not player:
        player = Player(name=name)
        session.add(player)
        session.commit()

    db_game = Game(player=player)
    session.add(db_game)
    session.commit()

    while True:
        input("Press Enter to roll dice...")
        d1, d2 = roll_dice()
        display_dice(d1, d2)
        total = d1 + d2
        print(f"You rolled: {d1} + {d2} = {total}")

        roll = Roll(game=db_game, die1=d1, die2=d2, total=total)
        session.add(roll)
        session.commit()

        again = input("Roll again? (y/n): ").strip().lower()
        if again != 'y':
            print("Thanks for playing!")
            break
