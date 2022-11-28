import common

def tie(state,board):
	return (state == common.constants.NONE) and (0 not in board)

def ab_max(board, a, b):
	v = float("-inf")
	bord, i = len(board), 0 
	while i < bord:
		if board[i] == common.constants.NONE:
			board[i] = common.constants.X
			v = max(v, prune(board, common.constants.O, a, b))
			board[i] = common.constants.NONE
			if v >= b: return v
			a = max(a, v)
		i+=1
	return v


def ab_min(board, a, b):
	v = float("inf")
	bord, i = len(board), 0 
	while i < bord:
		if board[i] == common.constants.NONE:
			board[i] = common.constants.O
			v = min(v, prune(board, common.constants.X, a, b))
			board[i] = common.constants.NONE
			if v <= a: return v
			b = min(b, v)
		i+=1
	return v



def prune(board, turn, a, b):
	state = common.game_status(board)
	if state == common.constants.X:return 1
	if state == common.constants.O:return -1
	if tie(state, board):return 0
	if turn == common.constants.X:
		return ab_max(board, a, b)
	if turn == common.constants.O:
		return ab_min(board, a, b)


def abprun_tictactoe(board, turn):
	win = prune(board, turn, float('-inf'), float('inf'))
	# common.print_board(board)
	if win == -1:
		return common.constants.O
	if win == 1:
		return common.constants.X
	if win == 0:
		return common.constants.NONE
	#put your code here:
	#it must return common.constants.X(1), common.constants.O(2) or common.constants.NONE(0) for tie.
	#use the function common.game_status(board), to evaluate a board
	#it returns common.constants.X(1) if X wins, common.constants.O(2) if O wins or common.constants.NONE(0) if tie or game is not finished
	#the program will keep track of the number of boards evaluated
	#result = common.game_status(board);



def max_mm(board):
	v = float("-inf")
	bord, i = len(board), 0 
	while i < bord:
		if board[i] == common.constants.NONE:
			board[i] = common.constants.X
			v = max(v, value_mm(board, common.constants.O))
			board[i] = common.constants.NONE
		i+=1
	return v


def min_mm(board):
	v = float("inf")
	bord, i = len(board), 0 
	while i < bord:
		if board[i] == common.constants.NONE:
			board[i] = common.constants.O
			v = min(v, value_mm(board, common.constants.X))
			board[i] = common.constants.NONE
		i+=1
	return v


def value_mm(board, turn):
	state = common.game_status(board)
	if state == common.constants.X:return 1
	if state == common.constants.O:return -1
	if tie(state, board):return 0 
	if turn == common.constants.X:
		return max_mm(board)
	if turn == common.constants.O:
		return min_mm(board)


def minmax_tictactoe(board, turn):
	win = value_mm(board, turn)
	# common.print_board(board)
	if win == -1:
		return common.constants.O
	if win == 1:
		return common.constants.X
	if win == 0:
		return common.constants.NONE
	#put your code here:
	#it must return common.constants.X(1), common.constants.O(2) or common.constants.NONE(0) for tie.
	#use the function common.game_status(board), to evaluate a board
	#it returns common.constants.X(1) if X wins, common.constants.O(2) if O wins or common.constants.NONE(0) if tie or game is not finished
	#the program will keep track of the number of boards evaluated
	#result = common.game_status(board);

