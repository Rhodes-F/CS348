import common

def get_start(map):
	start_y, start_x = 0, 0
	for y in range(common.constants.MAP_HEIGHT):
		for x in range(common.constants.MAP_WIDTH):
			if map[y][x] == 2:
				start_y, start_x = y, x
	return start_y, start_x

def get_end(map):
	end_y, end_x = 0, 0
	for y in range(common.constants.MAP_HEIGHT):
		for x in range(common.constants.MAP_WIDTH):
			if map[y][x] == 3:
				end_y, end_x = y, x
	return end_y, end_x

def path_trace(map, parents, x, y):
	while parents[y][x] is not None:
		map[y][x] = 5
		x, y = parents[y][x][0], parents[y][x][1]
	map[y][x] = 5

def dist_count(parents, x, y):	
	num =0
	while parents[y][x] is not None:
		num+=1
		x, y = parents[y][x][0], parents[y][x][1]
	return num 

def manhattan_dist(start_y, start_x, end_y, end_x):
	dist_y = abs(start_y- end_y)
	dist_x = abs(start_x-end_x)
	dist = dist_x+dist_y
	return dist


def astar_search(map):
	queue = []
	parents = [[None for i in range(common.constants.MAP_WIDTH)] for j in range(common.constants.MAP_HEIGHT)]
	found = False
	Y,X=get_start(map)
	eY,eX= get_end(map)
	queue.append([Y,X,manhattan_dist(Y,X,eY,eX)])
	while len(queue) !=0:
		queue.sort(key = lambda i:(i[2],i[1],i[0]))
		# print(queue)
		pos = queue.pop(0)
		# print(pos)
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
			mand = manhattan_dist(y,x+1,eY,eX)
			dtrav = dist_count(parents, x,y)
			huer = mand+dtrav
			queue.append([y, x+1, huer])
			parents[y][x+1] = [x, y]
			
		if dir2 == 0 or dir2 == 3:
			mand = manhattan_dist(y+1,x,eY,eX)
			dtrav = dist_count(parents, x,y)
			huer = mand+dtrav
			queue.append([y+1, x,huer])
			parents[y + 1][x] = [x, y]

		if dir3 == 0 or dir3 == 3:
			mand = manhattan_dist(y,x-1,eY,eX)
			dtrav = dist_count(parents, x,y)
			huer = mand+dtrav
			queue.append([y, x - 1,huer])
			parents[y][x-1] = [x, y]

		if dir4 == 0 or dir4 == 3:
			mand = manhattan_dist(y-1,x,eY,eX)
			dtrav = dist_count(parents, x,y)
			huer = mand+dtrav
			queue.append([y-1, x, huer])
			parents[y - 1][x] = [x, y]

	if found:
		path_trace(map,parents,end_x,end_y)

	# PUT YOUR CODE HERE
	# access the map using "map[y][x]"
	# y between 0 and common.constants.MAP_HEIGHT-1
	# x between 0 and common.constants.MAP_WIDTH-1
	return found

