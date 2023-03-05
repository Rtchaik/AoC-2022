with open('input3.txt') as f:
	input = [line.strip() for line in f.readlines()]
	common = ((set(item[:(l:=len(item)//2)]) & set(item[l:])).pop() for item in input)
	part1 = sum((ord(item)-96 if item.islower() else ord(item)-38) for item in common)
	print(part1)
	common2 = ((set(input[idx])&set(input[idx+1])&set(input[idx+2])).pop() for idx in range(0,len(input),3))
	part2 = sum((ord(item)-96 if item.islower() else ord(item)-38) for item in common2)
	print(part2)