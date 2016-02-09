import random
from Chromosome import Chromosome

totalPopulation = 30
print "Enter user chromosome string"
userString = raw_input()
userChromosome = Chromosome(userString)
initialPopulation = [];
print "Initializing Population"
for i in range(totalPopulation):
    initialPopulation.append(Chromosome(Chromosome.randomChromosomeString(10,len(userChromosome.rankString))))

print "Initial Population"
Chromosome.printPopulation(initialPopulation)
for i in range(10):

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
        result[0].mutate()
        result[1].mutate()

        nextPopulation = nextPopulation + result
    initialPopulation = nextPopulation
finalPopulation = Chromosome.calculateProbability(initialPopulation,userChromosome)
print "Final Population"
Chromosome.printPopulation(finalPopulation)
print "--------"
print "Best Chromosome : ", finalPopulation[Chromosome.getFittestChromosome(finalPopulation)].rankString
