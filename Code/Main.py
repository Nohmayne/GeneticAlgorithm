import Code.Population as Population


class GenAlg:

    def __init__(self):
        #print('INFO: initializing main')
        # ------------------------------------------------------------------------------------------------
        #self.targetPhrase = '=>w|Iy Bj*,Kdiw'
        self.targetPhrase = input('Input phrase: ')
        self.populationobj = Population.Population(self.targetPhrase, 0.3, 200)
        # ------------------------------------------------------------------------------------------------
        self.mutationrates = [0.9]
        self.row = 4
        self.column = 11

    def run(self):
        while not self.populationobj.finished:
            # ------------------------------------------------------------------------------------------------
            self.populationobj.genfpopulation()
            # ------------------------------------------------------------------------------------------------
            self.populationobj.orderpop()
            # ------------------------------------------------------------------------------------------------
            self.populationobj.makepool(self.populationobj.cpopulation)
            # ------------------------------------------------------------------------------------------------
            self.populationobj.createchildren()
            # ------------------------------------------------------------------------------------------------
            self.populationobj.mutatepop()
            # ------------------------------------------------------------------------------------------------
            self.populationobj.evaluate()
        # self.populationobj.finished:
            #self.populationobj.sheet.update_cell(self.row, self.column, self.populationobj.genNum)


genAlg = GenAlg()
genAlg.run()
"""
for i in range(0, len(genAlg.mutationrates)):
    for j in range(0, 204 - genAlg.row):
        genAlg.populationobj.__init__(genAlg.targetPhrase, genAlg.mutationrates[i], 200)
        genAlg.run()
        genAlg.row += 1
    genAlg.row = 4
    genAlg.column += 1
#"""
