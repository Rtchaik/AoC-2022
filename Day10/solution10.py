with open('input10.txt') as f:
    data = [line.strip().split() for line in f.readlines()]
    xs = [1,1]
    for ins in data:
        xs.append(xs[-1])
        if ins[0] != 'noop':
            xs.append(xs[-1] + int(ins[1]))
    part1 = sum(xs[idx]*idx for idx in range(20,250,40))
    print(part1)
    screen = [list(line) for line in ['.'*40]*6]
    for idx,x in enumerate(xs[1:241]):
        row, col = divmod(idx,40)
        if abs(x-col)<2:
            screen[row][col]='#'
    for line in screen:
        print(''.join(line))