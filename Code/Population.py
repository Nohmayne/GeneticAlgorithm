import Code.DNA as DNA
from random import *
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def createchild(indiv1, indiv2):
    ndna = DNA.DNA(len(indiv1.genome))
    if len(indiv1.genome) != len(indiv2.genome):
        #print('ERROR: incompatible individuals in createchild')
        return
    else:
        for i in range(0, len(indiv1.genome)):
            if randint(0, 100) < 50:
                ndna.genome[i] = indiv1.genome[i]
            else:
                ndna.genome[i] = indiv2.genome[i]
        return ndna


class Population:

    def __init__(self, target, mutationrate, popmax):
        #print('INFO: initializing population')
        self.matingpool = []
        self.cpopulation = []
        self.finished = False
        self.genNum = 0
        # ------------------------------------------------------------------------------------------------
        self.target = target
        self.mutationRate = mutationrate
        self.popMax = popmax
        # ------------------------------------------------------------------------------------------------
        self.scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        self.creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', self.scope)
        self.client = gspread.authorize(self.creds)
        # ------------------------------------------------------------------------------------------------
        self.sheet = self.client.open("Mutation Rate Data").sheet1

    def genfpopulation(self):
        for i in range(0, self.popMax):
            self.cpopulation.append(DNA.DNA(len(self.target)))

    def orderpop(self):
        for dna in self.cpopulation:
            dna.fitnesscalc(self.target)
        self.cpopulation.sort(key=lambda x: x.fitness, reverse=True)
        #print('INFO: Best Member of Population -- ' + ''.join(self.cpopulation[0].genome))

    def makepool(self, sortedpop):
        pool = []
        for i in range(0, len(sortedpop)):
            for j in range(0, int(sortedpop[i].fitness + 1.0)):
                pool.append(sortedpop[i])
        self.matingpool = pool
        shuffle(self.matingpool)

    def createchildren(self):
        self.cpopulation = []
        for i in range(0, self.popMax):
            inda = self.matingpool[randint(0, len(self.matingpool) - 1)]
            indb = self.matingpool[randint(0, len(self.matingpool) - 1)]
            newchild = createchild(inda, indb)
            self.cpopulation.append(newchild)

    def mutatepop(self):
        for indiv in self.cpopulation:
            indiv.mutate(self.mutationRate)

    def evaluate(self):
        for indiv in self.cpopulation:
            if ''.join(indiv.genome) == self.target:
                #print('INFO: Final Answer --')
                #print(''.join(indiv.genome))
                #print('INFO: Answer found in {} generations.'.format(self.genNum))
                # ------------------------------------------------------------------------------------------------
                self.finished = True
                break
            else:
                self.finished = False
        self.genNum += 1
