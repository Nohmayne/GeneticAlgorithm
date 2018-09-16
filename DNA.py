import random
import string

class DNA:

    def __init__(self, genomelength):
        self.fitness = 0.0
        self.genome = []
        self.genomelength = genomelength
        self.choosablechars = ' ' + string.ascii_letters + string.punctuation

        for i in range(0, self.genomelength):
            self.genome.append(self.choosablechars[random.randint(0, len(self.choosablechars) - 1)])

    def fitnesscalc(self, target):
        if len(self.genome) != len(target):
            #print('ERROR: invalid input in fitnesscalc')
            return
        else:
            score = 0
            for i in range(0, len(target)):
                if self.genome[i] == target[i]:
                    score += 1
            self.fitness = (score / len(target)) * 100
    def mutate(self, mutationrate):
        for i in range(0, len(self.genome)):
            randnum = random.random()*100
            #print(randnum)
            if randnum < mutationrate:
                self.genome[i] = self.choosablechars[random.randint(0, len(self.choosablechars) - 1)]
