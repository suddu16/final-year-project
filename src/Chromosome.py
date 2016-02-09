import random
import math

class Chromosome:
    'Representation of any Cloud Service Provider'

    Count = 0
    MutateProbability = 0.30
    CrossOverProbability = 0.60

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
        mutateIndexCount = (int)(Chromosome.MutateProbability * len(self.rankString))
        print mutateIndexCount ," changes expected!"
        for i in range(mutateIndexCount):
            index = random.randrange(start,end,1)
            print "Mutating index ", index
            self.rankString = self.rankString[:index] + str((int(self.rankString[index])+random.randrange(0,100,1))%(end-start)+start) + self.rankString[index+1:]

    @staticmethod
    def crossover(chrome1,chrome2):
        if(random.random() < Chromosome.CrossOverProbability):
            print "Crossing Over"
            start = 0
            end = len(chrome1.rankString)
            crossoverpt = random.randrange(start,end,1)
            offspr1 = chrome1.rankString[:-(end-crossoverpt)] + chrome2.rankString[(crossoverpt):]
            offspr2 = chrome2.rankString[:-(end-crossoverpt)] + chrome1.rankString[(crossoverpt):]
            return [Chromosome(offspr1),Chromosome(offspr2)]
        else:
            return [chrome1,chrome2]

    @staticmethod
    def distance(chrome1,chrome2):
        print "Finding Distance between given chromosomes ",chrome1.rankString," and ",chrome2.rankString
        total = 0
        count = 0
        for i in range(len(chrome1.rankString)):
            count = (int(chrome1.rankString[i]) - int(chrome2.rankString[i]))**2
            total = count+total
        dist = math.sqrt(total)
        return dist
