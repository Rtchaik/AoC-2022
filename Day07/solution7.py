from dataclasses import dataclass, field
from functools import cached_property

@dataclass
class Dirs:
	name: str
	parent: str
	childs: list = field(default_factory=list)
	
	@cached_property
	def calc_size(self):
			return sum(it.calc_size if type(it) != list else int(it[0]) for it in self.childs)
	
with open('input7.txt') as f:
	input = [line.strip().split() for line in f.readlines()]
	current = Dirs('/','/')
	all_dirs = {current.name : current}
	for com in input[1:]:
		if com[0] == '$':
			if com[1] == 'cd':
				current = all_dirs[current.name + com[2]] if com[2]!='..' else all_dirs[current.parent]
		elif com[0]=='dir':
			new = Dirs(current.name+com[1], current.name)
			all_dirs[current.name + com[1]] = new
			current.childs.append(new)
		else:
			current.childs.append(com)
	sizes = sorted(v.calc_size for _,v in all_dirs.items())
	part1 = sum(s for s in sizes if s<=100000)
	print(part1)
	used = sizes[-1]-40000000
	print(next(x for x in sizes if x>used))