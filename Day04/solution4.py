with open('input4.txt') as f:
	input = [sorted([int(num) for num in pair.split('-')] for pair in line.strip().split(',')) for line in f.readlines()]
	part1 = sum(x[0]==y[0] or (x[0]<y[0] and x[1]>=y[1]) for x,y in input)
	print(part1)
	part2 = sum(x[0]<=y[0]<=x[1] for x,y in input)
	print(part2)