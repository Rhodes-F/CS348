import common
from common import constants as con


def find_start(map):
    for y in range(6):
        for x in range(6):
            if map[y][x] == con.PIZZA:
                return y, x


def  next_states(x,y,a,map):
	## Returns the three posible actions and probability of each in the form (P,x,y)
	map_width, map_height = len(map[0]), len(map)
	if a == con.SOFF:
		s1 = (.7, x, y + 1 if y + 1 < map_height else  y) #south
		s2 = (.15, x - 1 if x - 1 >= 0 else x, y) #west
		s3 =(.15, x + 1 if x + 1 < map_width else x, y) #east
		s4 = (0, x, y - 1 if y - 1 >= 0 else  y) #north
		return[s1,s2,s3,s4]
	if a == con.SON:
		s1 = (.8, x, y + 1 if y + 1 < map_height else  y) #south
		s2 = (.1, x - 1 if x - 1 >= 0 else x, y) #west
		s3 =(.1, x + 1 if x + 1 < map_width else x, y) #east
		s4 = (0, x, y - 1 if y - 1 >= 0 else  y) #north
		return[s1,s2,s3,s4]
	if a ==con.WOFF:
		s1 = (.15, x, y + 1 if y + 1 < map_height else  y) #south
		s2 = (.7, x - 1 if x - 1 >= 0 else x, y) #west
		s3 =(0, x + 1 if x + 1 < map_width else x, y) #east
		s4 = (.15, x, y - 1 if y - 1 >= 0 else  y) #north
		return[s1,s2,s3,s4]
	if a ==con.WON:
		s1 = (.1, x, y + 1 if y + 1 < map_height else  y) #south
		s2 = (.8, x - 1 if x - 1 >= 0 else x, y) #west
		s3 =(0, x + 1 if x + 1 < map_width else x, y) #east
		s4 = (.1, x, y - 1 if y - 1 >= 0 else  y) #north
		return[s1,s2,s3,s4]
	if a == con.NOFF :
		s1 = (0, x, y + 1 if y + 1 < map_height else  y) #south
		s2 = (.15, x - 1 if x - 1 >= 0 else x, y) #west
		s3 =(.15, x + 1 if x + 1 < map_width else x, y) #east
		s4 = (.7, x, y - 1 if y - 1 >= 0 else  y) #north
		return[s1,s2,s3,s4]
	if a == con.NON:
		s1 = (0, x, y + 1 if y + 1 < map_height else  y) #south
		s2 = (.1, x - 1 if x - 1 >= 0 else x, y) #west
		s3 =(.1, x + 1 if x + 1 < map_width else x, y) #east
		s4 = (.8, x, y - 1 if y - 1 >= 0 else  y) #north
		return[s1,s2,s3,s4]
	if a == con.EOFF:
		s1 = (.15, x, y + 1 if y + 1 < map_height else  y) #south
		s2 = (0, x - 1 if x - 1 >= 0 else x, y) #west
		s3 =(.7, x + 1 if x + 1 < map_width else x, y) #east
		s4 = (.15, x, y - 1 if y - 1 >= 0 else  y) #north
		return[s1,s2,s3,s4]
	if a == con.EON:
		s1 = (.1, x, y + 1 if y + 1 < map_height else  y) #south
		s2 = (0, x - 1 if x - 1 >= 0 else x, y) #west
		s3 =(.8, x + 1 if x + 1 < map_width else x, y) #east
		s4 = (.1, x, y - 1 if y - 1 >= 0 else  y) #north
		return[s1,s2,s3,s4]

def is_special(a):
    return a in [con.NON, con.EON, con.SON, con.WON]

def get_reward (x,y,a,values, battery_drop_cost, discount,map):
	reward = 0
	next_states_ = next_states(x,y,a,map)
	reward_this = 2 * -battery_drop_cost if is_special(a) else -battery_drop_cost
	for state in next_states_:
		reward += state[0]* (reward_this + discount * values[state[2]][state[1]])
	return reward


def drone_flight_planner (map,policies, values, delivery_fee, battery_drop_cost, dronerepair_cost, discount):
	sy ,sx = find_start(map)
	converge = False
	while not converge:
		converge = True
		new_value = [[float('-inf') for i in range(6)] for j in range(6)]
		for y in range(len(map)):
			for x in range(len(map[0])):
				if map[y][x] == common.constants.CUSTOMER:
					new_value[y][x]= delivery_fee
					policies[y][x] = common.constants.EXIT
				elif map[y][x] == common.constants.RIVAL:
					new_value[y][x]= - dronerepair_cost
					policies[y][x] = common.constants.EXIT
				else:
					for a in [con.SOFF, con.WOFF, con.NOFF, con.EOFF, con.SON, con.WON, con.NON, con.EON]:
						v = get_reward(x,y,a, values, battery_drop_cost, discount,map)
						if v > new_value [y][x]:
							new_value[y][x]= v
							policies[y][x]= a
				if abs(values[y][x] - new_value[y][x]) > 0.001:
					converge = False
				values[y][x]= new_value[y][x]

	return values[sy][sx]


