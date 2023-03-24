import random

class Dice:
    @staticmethod
    def roll():
        return random.randint(1, 6)

class DiceProbability:
    def __init__(self):
        self.n = 0
        
    def calcProbability(self, n):
        self.result_Dice = []
        self.count_Dice = [0]*6
        self.ratio_Dice = [0]*6
        
        for i in range(n):
            self.result_Dice.append(Dice.roll())
        
        for i in range(6):
            self.count_Dice[i] = self.result_Dice.count(i+1)
            self.ratio_Dice[i] = self.result_Dice.count(i+1) / n
        
        return self.count_Dice, self.ratio_Dice
        
    def printProbability(self):
        print(f'총 횟수:{self.n}')
        for i in range(6):
            print(f"주사위{i+1}:{self.count_Dice[i]} 비율:{self.ratio_Dice[i]:.3f}")
        print()