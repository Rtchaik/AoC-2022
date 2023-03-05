import numpy as np

with open('input12.txt') as f:
	input = np.array([[ord(sq) for sq in line.strip()] for line in f.readlines()])
	st = tuple(x[0] for x in np.where(input==83))
	fin = tuple(x[0] for x in np.where(input==69))
	input[st]=ord('a')
	input[fin]=ord('z')
	def bfs_steps(start, finish, mode=0):
		visited = {start}
		steps = 0
		bfs = {start}
		dirs = [(0,1), (0,-1),(1,0),(-1,0)]
		while bfs and finish not in visited:
			bfs = set.union(*[{item for item in (tuple(sum(x) for x in zip(dir,sq)) for dir in dirs) if 0<=item[0]<len(input) and 0<=item[1]<len(input[0]) and mode*(input[item]-input[sq])<2} for sq in bfs]) - visited
			visited |= bfs
			steps += 1
			if mode == -1 and any((input[sq] == 97 for sq in bfs)):
				break
		return steps
	print(bfs_steps(st, fin, 1))	
	print(bfs_steps(fin,st,-1))