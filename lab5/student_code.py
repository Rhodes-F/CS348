import common

#helpful, but not needed
class variables:
	counter=0


def sudoku_backtracking(sudoku):
	variables.counter = 0
	BT(sudoku)
	return variables.counter


def BT(sudoku):
	variables.counter +=1
	if is_complete(sudoku): 
		return True
	else:
		y, x = find_empty(sudoku)
		for v in range(1,10):
			if common.can_yx_be_z(sudoku, y, x, v):
				sudoku[y][x] = v
				R = BT(sudoku)
				if R == True:
					return True
				sudoku[y][x]=0
		return False



def sudoku_forwardchecking(sudoku):
	variables.counter = 0
	FC(sudoku)
	return variables.counter

def FC(sudoku):
	variables.counter +=1
	if is_complete(sudoku): 
		return True
	else:
		y, x = find_empty(sudoku)
		for v in range(1,10):
			if common.can_yx_be_z(sudoku, y, x, v):
				sudoku[y][x] = v
				if not empty_domain(sudoku):
					R = FC(sudoku)
					if R == True:
						return True
				sudoku[y][x]=0
		return False


def is_complete(sudoku):
	for y in range(9):
		for x in range(9):
			if sudoku[y][x]== 0: 
				return False	
	return True

def find_empty(sudoku):
	for y in range(9):
		for x in range(9):
			if sudoku[y][x]== 0: 
				return y,x	


# checking whole domine here, if fails tests might have to retry to build domain array
def empty_domain(sudoku):
	for y in range(9):
		for x in range(9):
			if sudoku[y][x] == 0:
				num_doms=0
				for v in range(1, 10):
					if common.can_yx_be_z(sudoku, y, x, v):
						num_doms+=1
				if num_doms ==0: 
					return True
	return False

# domain = [[[0 for i in range(9)] for j in range(9)] for k in range(9)]
# for y in range(9):
# 	for x in range (9):
# 		if sudoku[y][x] != 0:
# 			domain[y][x][]