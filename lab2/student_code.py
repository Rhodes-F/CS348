QUEENS = 10

def num_attacks(board):
	attacks = 0
	queen_pos=[]

	for i in range (10):
		for j in range (10):
			if board[j][i]==1:
				queen_pos.append([i,j])

	# print("length" ,len(queen_pos))
	for i in range(10):
		q1x= queen_pos[i][0]
		q1y = queen_pos[i][1]
		q1=queen_pos[i]
		for j in range(10):
			q2x = queen_pos[j][0]
			q2y = queen_pos[j][1]
			q2 = queen_pos[j]
			if q1 != q2:
				if q1y == q2y: 
					attacks+=1
				if (abs(q1y - q2y) == abs(q1x - q2x)) == 1:
					attacks +=1

	
	return attacks



def gradient_search(board):
    old_board = board
    best_board = old_board
    best_attacks = num_attacks(board)
    old_attacks = 10000
    while best_attacks<old_attacks:
        old_attacks = best_attacks
        for queen in range (10):
            for row in range (10):
                new_board = [row[:] for row in old_board]
                for i in range(10):
                    new_board[i][queen] = 0 
                new_board[row][queen]= 1
                attacks = num_attacks(new_board)
                if attacks < best_attacks:
                    best_board = new_board
                    best_attacks = attacks
        for i in range(QUEENS):
            for j in range(QUEENS):
                old_board[i][j] = best_board[i][j]
    for i in range(QUEENS):
        for j in range(QUEENS):
            board[i][j] = best_board[i][j]
    return best_attacks == 0

