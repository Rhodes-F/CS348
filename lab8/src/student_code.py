import common

def classify(data, weights):
	dp = 0
	for i in range(2):
		dp += weights[i]*data[i]
	dp += weights[2]
	if dp > 0 :
		return 1
	else:
		return 0


def part_one_classifier(data_train, data_test):
	weights = [0 for _ in range(3)]
	correct_class = False
	while not correct_class:
		correct_class = True
		for data in data_train:
			c = classify(data, weights)
			if c != data[2]:
				if c != 1:
					for i in range(2):
						weights[i] += data[i]
					weights[2] += 1
				if c ==1 :
					for i in range(2):
						weights[i] -= data[i]
					weights[2] -= 1
				correct_class = False
	for data in data_test:
		c = classify(data, weights)
		data[2] = c
	return


def part_two_classifier(data_train, data_test):
	weights = [[0 for x in range(3)] for x in range(10)]
	correct_class = False
	L_R = 1
	while not correct_class:
		correct_class = True
		for data in data_train:
			c = classify_2(data, weights)
			if c != data[2]:
				correct_class = False
				corr_class = int(data[2])
				for i in range(common.constants.DATA_DIM):
					weights[corr_class][i] += L_R*data[i]
					weights[c][i] -= L_R*data[i]
				weights[corr_class][2] += 1
				weights[c][2] -= 1
	for data in data_test:
		c = classify_2(data, weights)
		data[2] = c

	return

def classify_2_dot (data,weights):
	dp = 0
	for i in range(2):
		dp += weights[i]*data[i]
	dp += weights[2]
	return dp

def classify_2(data, weights):
	dots = []
	dot = 0
	for weight in weights:
		dot = classify_2_dot(data, weight)
		dots.append(dot)
	ind = dots.index(max(dots))
	return ind

