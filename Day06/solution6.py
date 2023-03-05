with open('input6.txt') as f:
	input = f.read()
	
	def finder(idx):
			start = idx
			while True:
				marker = start- len(set(input[idx-start:idx]))
				if not marker:
					return idx
				idx+=marker
	print(finder(4))
	print(finder(14))