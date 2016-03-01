import random
from Chromosome import Chromosome

totalPopulation = 30
maxRank = 40
userString = [1,2,3,4,5]
userChromosome = Chromosome(userString)
print len(userChromosome.rankString)
initialPopulation = [];
print "Initializing Population"
for i in range(totalPopulation):
    initialPopulation.append(Chromosome(Chromosome.randomChromosomeString(maxRank,len(userChromosome.rankString))))

print "Initial Population"
Chromosome.printPopulation(initialPopulation)
for i in range(50):

    print "ITERATION ",i
    nextPopulation = []
    initialPopulation = Chromosome.rouletteSelection(initialPopulation,userChromosome)
    print "Undergoing Elitism"

    print "Best Four Chromosomes in Gen",i+1
    for i in range(4):
        index = Chromosome.getFittestChromosome(initialPopulation)
        nextPopulation.append(initialPopulation[index])
        print initialPopulation[index].rankString
        initialPopulation.pop(index)

    print "Undergoing Crossover and Mutation"

    for i in range(totalPopulation/2 - 2):

        firstParentIndex = random.randrange(0,len(initialPopulation),1)
        firstParent = initialPopulation[firstParentIndex]
        initialPopulation.pop(firstParentIndex)

        secondParentIndex = random.randrange(0,len(initialPopulation),1)
        secondParent = initialPopulation[secondParentIndex]
        initialPopulation.pop(secondParentIndex)

        result = Chromosome.crossover(firstParent,secondParent)
        result[0].mutate(maxRank)
        result[1].mutate(maxRank)

        nextPopulation = nextPopulation + result
    initialPopulation = nextPopulation
finalPopulation = Chromosome.calculateProbability(initialPopulation,userChromosome)
print "Final Population"
Chromosome.printPopulation(finalPopulation)
print "--------"
print "Best Chromosome : ", finalPopulation[Chromosome.getFittestChromosome(finalPopulation)].rankString
