import re
from copy import deepcopy

with open('input5.txt') as f:
	stacks, proc = f.read().split('\n\n')
	stacks = [[box for box in reversed(line) if box != ' '] for line in zip(*[[item[idx] for idx in range(1,len(item),4)] for item in stacks.splitlines()[:-1]])]
	stacks2 = deepcopy(stacks)
	proc = [[int(num) for num in re.findall(r'\d+', line)] for line in proc.splitlines()]
	
	for move, st1,st2 in proc:
		stacks[st2-1].extend(reversed(stacks[st1-1][-move:]))
		del(stacks[st1-1][-move:])
	part1 = ''.join(st[-1] for st in stacks)
	print(part1)
	
	for move, st1,st2 in proc:
		stacks2[st2-1].extend(stacks2[st1-1][-move:])
		del(stacks2[st1-1][-move:])
	part2 = ''.join(st[-1] for st in stacks2)
	print(part2)