import random

class Chromosome:
    'Representation of any Cloud Service Provider'

    Count = 0
    MutateProbability = 0.30
    CrossOverProbability = 0.30

    def __init__(self,rankString):
        self.rankString = rankString
        Chromosome.Count += 1
        print "Chromosome created!"

    def displayRankString(self):
        print "My Rank String is " ,self.rankString

    def mutate(self):
        print "Mutating Chromosome with probability ", Chromosome.MutateProbability
        start  = 0
        end    = len(self.rankString)
        mutate = (random.random() < Chromosome.MutateProbability)
        if(mutate):
            mutateIndexCount = random.randrange(start,(end+1)/2,1)+1
            print mutateIndexCount ," changes expected!"
            for i in range(mutateIndexCount):
                index = random.randrange(start,end,1)
                print "Mutating index ", index
                self.rankString = self.rankString[:index] + str((int(self.rankString[index])+random.randrange(0,100,1))%(end-start)+start) + self.rankString[index+1:]
