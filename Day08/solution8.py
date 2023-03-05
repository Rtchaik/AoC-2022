import numpy as np

with open('input8.txt') as f:
	input = [[int(l) for l in line.strip()] for line in f.readlines()]
	forest = np.array(input)
	vis = np.zeros(forest.shape, dtype = int)
	vis[0] = vis[-1] = vis[:,0] = vis[:,-1] = 1
	score = np.ones(forest.shape, dtype = int)
	score[0] = score[-1] = score[:,0] = score[:,-1] = 0
	for _ in range(4):
		for y in range(1,len(forest)-1):
			l = len(forest[0])
			max_h = forest[y,0]
			for x in range(1,l-1):
				current = forest[y,x]
				if current>max_h:
					max_h=current
					vis[y,x]=1
				for ss in range(1,l-x):
					if current <= forest[y, x+ss] or ss == l-x-1:
						score[y,x]*=ss
						break
			forest=np.rot90(forest)
			vis=np.rot90(vis)
			score=np.rot90(score)
	part1 = vis.sum()
	print(part1)
	part2 = score.max()
	print(part2)