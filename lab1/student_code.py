import common

def get_start(map):
	start_y, start_x = 0, 0
	for y in range(common.constants.MAP_HEIGHT - 1):
		for x in range(common.constants.MAP_WIDTH - 1):
			if map[y][x] == 2:
				start_y, start_x = y, x
	return start_y, start_x

def path_trace(map, parents, x, y):
    while parents[y][x] is not None:
        map[y][x] = 5
        x, y = parents[y][x][0], parents[y][x][1]
    map[y][x] = 5


def df_search(map):
	queue = []
	parents = [[None for i in range(common.constants.MAP_WIDTH)] for j in range(common.constants.MAP_HEIGHT)]
	found = False
	Y,X=get_start(map)
	queue.append([Y,X])
	while len(queue) !=0:
		pos = queue.pop(-1)
		y = pos[0]
		x = pos[1]

		if map[y][x] == 3:
			found = True
			end_y, end_x = y, x
			break
		map[y][x] = 4

		dir1 = map[y][x + 1] if x + 1 < common.constants.MAP_WIDTH else -1
		dir2 = map[y + 1][x] if y + 1 < common.constants.MAP_HEIGHT else -1
		dir3 = map[y][x - 1] if 0 <= x - 1  else -1
		dir4 = map[y - 1][x] if 0 <= y - 1 else -1

		if dir4 == 0 or dir4 == 3:
			queue.append([y-1, x])
			parents[y - 1][x] = [x, y]

		if dir3 == 0 or dir3 == 3:
			queue.append([y, x - 1])
			parents[y][x-1] = [x, y]

		if dir2 == 0 or dir2 == 3:
			queue.append([y+1, x])
			parents[y + 1][x] = [x, y]

		if dir1 == 0 or dir1 == 3:
			queue.append([y, x+1])
			parents[y][x+1] = [x, y]

	if found:
		path_trace(map,parents,end_x,end_y)

	# PUT YOUR CODE HERE
	# access the map using "map[y][x]"
	# y between 0 and common.constants.MAP_HEIGHT-1
	# x between 0 and common.constants.MAP_WIDTH-1
	return found

def bf_search(map):
	queue = []
	parents = [[None for i in range(common.constants.MAP_WIDTH)] for j in range(common.constants.MAP_HEIGHT)]
	found = False
	Y,X=get_start(map)
	queue.append([Y,X])
	while len(queue) !=0:
		pos = queue.pop(0)
		y = pos[0]
		x = pos[1]

		if map[y][x] == 3:
			found = True
			end_y, end_x = y, x
			break
		map[y][x] = 4

		dir1 = map[y][x + 1] if x + 1 < common.constants.MAP_WIDTH else 10
		dir2 = map[y + 1][x] if y + 1 < common.constants.MAP_HEIGHT else 10
		dir3 = map[y][x - 1] if 0 <= x - 1 else 10
		dir4 = map[y - 1][x] if 0 <= y - 1 else 10
		
		if dir1 == 0 or dir1 == 3:
			queue.append([y, x+1])
			parents[y][x+1] = [x, y]
			
		if dir2 == 0 or dir2 == 3:
			queue.append([y+1, x])
			parents[y + 1][x] = [x, y]

		if dir3 == 0 or dir3 == 3:
			queue.append([y, x - 1])
			parents[y][x-1] = [x, y]

		if dir4 == 0 or dir4 == 3:
			queue.append([y-1, x])
			parents[y - 1][x] = [x, y]

	if found:
		path_trace(map,parents,end_x,end_y)

	# PUT YOUR CODE HERE
	# access the map using "map[y][x]"
	# y between 0 and common.constants.MAP_HEIGHT-1
	# x between 0 and common.constants.MAP_WIDTH-1
	return found

