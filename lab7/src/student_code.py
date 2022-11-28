import common
import math 
#note, for this lab only, your are allowed to import math

def detect_slope_intercept(image):
	votes = common.init_space(2000, 2000)
	for y in range(common.constants.HEIGHT):
		for x in range(common.constants.WIDTH):
			if image[y][x] == 0:
				for mcoun in range(2000):
					m = mcoun/100 - 10
					b = y - m * x
					if -1000 <= b < 1000:
						bcoun = int(b) + 1000
						votes[mcoun][bcoun] += 1
	return vote_max(votes)

def vote_max(votes):
	max_vote = float('-inf')
	b,m = 0,0
	line = common.Line()
	for y in range(2000):
		for x in range(2000):
			if votes[y][x] > max_vote:
				max_vote = votes[y][x]
				m = y
				b = x
	line.m = m/100 - 10
	line.b = b - 1000
	return line


def detect_circles(image):
	votes = common.init_space(200, 200)
	for y in range(common.constants.HEIGHT):
		for x in range(common.constants.WIDTH):
			if image[y][x] == 0:
				for a in range(y-50, y+50):
					for b in range(x-50, x+50):
						if (0<=b<200 and 0<=a<200):
							radius = math.sqrt((b-x)**2 + (a-y)**2)
							if abs(radius - 30)<= .5:
								votes[a][b] += 1
	
	circles = 0
	threshold = 50
	for y in range(200):
		for x in range(200):
			if votes[y][x] > threshold:
				circles += 1
	return circles/4

				

