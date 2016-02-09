from Chromosome import Chromosome

c = Chromosome("12345")
c.displayRankString()
c.mutate()
c.displayRankString()
d = Chromosome("54321")
d.displayRankString()
e = Chromosome.crossover(c,d)
e[0].displayRankString()
e[1].displayRankString()

print Chromosome.distance(c,d)
