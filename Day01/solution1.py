with open('input1.txt') as f:
	input = sorted(sum(int(item) for item in elf.split()) for elf in f.read().split('\n\n'))[-3:]
	print(input[-1])
	print(sum(input))