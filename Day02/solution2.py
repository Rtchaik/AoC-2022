with open('input2.txt') as f:
	input = [line.strip() for line in f.readlines()]
	draw = ['A X', 'B Y', 'C Z']
	win = ['C X', 'A Y', 'B Z']
	score = {'X':1, 'Y':2, 'Z':3}
	
	def round(shapes):
		winner = 0
		if shapes in win:
			winner = 6
		elif shapes in draw:
			winner = 3
		return winner + score[shapes[-1]]
	
	part1 = sum(round(line) for line in input)
	print(part1)
	
	moves = 'ABC'
	def round2(shapes):
		move = moves.index(shapes[0])
		if shapes[-1]=='X':
			return (move+2)%3+1
		elif shapes[-1]=='Y':
			return 4 + move
		else:
			return 7 + (move+1)%3
	
	part2 = sum(round2(line) for line in input)
	print(part2)