import random

def roll_dice():
    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1, 6)
    total = dice_1 + dice_2
    return dice_1, dice_2, total

class DiceGame:
    def __init__(self, player_name):
        self.player_name = player_name
        self.rolls = []
        self.is_over = False
        self.result = None

    def play_turn(self):
        dice_1, dice_2, total = roll_dice()
        self.rolls.append((dice_1, dice_2, total))
        
        # Basic game logic example: 
        
        if len(self.rolls) == 1:
            if total in (7, 11):
                self.is_over = True
                self.result = "win"
            elif total in (2, 3, 12):
                self.is_over = True
                self.result = "lose"
        else:
           
            # if total is 7 -> lose
            first_total = self.rolls[0][2]
            if total == first_total:
                self.is_over = True
                self.result = "win"
            elif total == 7:
                self.is_over = True
                self.result = "lose"
        
        return dice_1, dice_2, total
