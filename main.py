import Dice

a = Dice.DiceProbability()
a.n = int(input('횟수 입력: '))
a.calcProbability(a.n)
a.printProbability()