from dataclasses import dataclass

@dataclass(frozen=True)
class Vec:
	row: int
	col: int
	
	def __add__(self, other):
		return Vec(self.row+other.row,self.col+other.col)
		
	def is_near(self, other):
		return abs(self.row-other.row)<2 and abs(self.col-other.col)<2
		
	def move_to(self, other):
		def move(c1, c2):
			diff=c1-c2
			return c1-abs(diff)//diff if diff else c1
		return Vec(move(self.row,other.row),move(self.col,other.col))

with open('input9.txt') as f:
	input = [line.split() for line in f.readlines()]
	dirs = {'U':Vec(1,0), 'D':Vec(-1,0), 'R':Vec(0,1), 'L':Vec(0,-1)}
	def motions(num):
		vis={Vec(0,0)}
		knots = [Vec(0,0)]*num
		for com,steps in input:
			for _ in range(int(steps)):
				knots[0]+=dirs[com]
				for idx, tail in enumerate(knots[1:]):
					if not tail.is_near(knots[idx]):
						tail=tail.move_to(knots[idx])
					knots[idx+1] = tail
				vis|={knots[-1]}
		return vis
	part1 = len(motions(2))
	print(part1)
	part2 = len(motions(10))
	print(part2)