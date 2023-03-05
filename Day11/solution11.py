from dataclasses import dataclass
import re
from operator import mul
from functools import reduce
from copy import deepcopy

@dataclass
class Monkey:
	items: list
	func: str
	test: int
	throw: tuple
	count: int = 0
	
	def turn(self, wlevel,divis):
		res = ([],[])
		for item in self.items:
			item = eval(str(item) + self.func)//wlevel
			res[item%self.test==0].append(item%divis if divis else item)
			self.count+=1
		self.items = []
		return zip(self.throw,res)

with open('input11.txt') as f:
	input = [[re.findall(r'[\+\*]? \d+', mon) for mon in line.splitlines()[1:]] for line in f.read().split('\n\n')]
	monkeys1 = [Monkey([int(n) for n in x[0]], x[1][0] if x[1] else '**2', int(x[2][0]), (int(x[4][0]),int(x[3][0]))) for x in input]
	monkeys2 = deepcopy(monkeys1)
	def play_rounds(num,monkeys,part):
		wlev, divis = (3,0) if part==1 else (1,reduce(mul, (mon.test for mon in monkeys)))
		for _ in range(num):
			for monkey in monkeys:
				for mon, new_items in monkey.turn(wlev,divis):
					monkeys[mon].items.extend(new_items)
		return mul(*sorted(mon.count for mon in monkeys)[-2:])
	print(play_rounds(20, monkeys1, 1))
	print(play_rounds(10000, monkeys2, 2))