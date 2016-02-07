import random

crossoverprob = 0.30

def crossover(chrome1,chrome2):
	if(random.random() < crossoverprob):
		start = 1;
		end = len(chrome1)
		crossoverpt = random.randrange(start,end,1)
		offspr1 = chrome1[:-(end-crossoverpt)] + chrome2[(crossoverpt):]
		offspr2 = chrome2[:-(end-crossoverpt)] + chrome1[(crossoverpt):]
		print crossoverpt," ",offspr1," ",offspr2


crossover("12345","43212")
