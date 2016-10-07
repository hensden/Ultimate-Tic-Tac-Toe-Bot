"""Testing module."""
import sys
# The possible combinations for capturing a block
win_orientation = [
        #diagonal
        ((0, 0), (1, 1), (2, 2)),
        ((2, 0), (1, 1), (0, 2)),

        #vertical
        ((0, 0), (1, 0), (2, 0)),
        ((0, 1), (1, 1), (2, 1)),
        ((0, 2), (1, 2), (2, 2)),

        #horizontal
        ((0, 0), (0, 1), (0, 2)),
        ((1, 0), (1, 1), (1, 2)),
        ((2, 0), (2, 1), (2, 2))
]

def determine_blocks_allowed(old_move, block_stat):
    """Function to test `get_valid_blocks` against."""
    blocks_allowed = []
    if old_move[0] % 3 == 0 and old_move[1] % 3 == 0:
        blocks_allowed = [1, 3]
    elif old_move[0] % 3 == 0 and old_move[1] % 3 == 2:
        blocks_allowed = [1, 5]
    elif old_move[0] % 3 == 2 and old_move[1] % 3 == 0:
        blocks_allowed = [3, 7]
    elif old_move[0] % 3 == 2 and old_move[1] % 3 == 2:
        blocks_allowed = [5, 7]
    elif old_move[0] % 3 == 0 and old_move[1] % 3 == 1:
        blocks_allowed = [0, 2]
    elif old_move[0] % 3 == 1 and old_move[1] % 3 == 0:
        blocks_allowed = [0, 6]
    elif old_move[0] % 3 == 2 and old_move[1] % 3 == 1:
        blocks_allowed = [6, 8]
    elif old_move[0] % 3 == 1 and old_move[1] % 3 == 2:
        blocks_allowed = [2, 8]
    elif old_move[0] % 3 == 1 and old_move[1] % 3 == 1:
        blocks_allowed = [4]
    else:
        sys.exit(1)
    final_blocks_allowed = []
    for i in blocks_allowed:
        if block_stat[i] == '-':
            final_blocks_allowed.append(i)
    return final_blocks_allowed

num_to_block = [
    [1, 3], [0, 2], [1, 5], [1, 3], [0, 2], [1, 5], [1, 3], [0, 2], [1, 5],
    [0, 6], [4], [2, 8], [0, 6], [4], [2, 8], [0, 6], [4], [2, 8],
    [3, 7], [6, 8], [5, 7], [3, 7], [6, 8], [5, 7], [3, 7], [6, 8], [5, 7],
    [1, 3], [0, 2], [1, 5], [1, 3], [0, 2], [1, 5], [1, 3], [0, 2], [1, 5],
    [0, 6], [4], [2, 8], [0, 6], [4], [2, 8], [0, 6], [4], [2, 8],
    [3, 7], [6, 8], [5, 7], [3, 7], [6, 8], [5, 7], [3, 7], [6, 8], [5, 7],
    [1, 3], [0, 2], [1, 5], [1, 3], [0, 2], [1, 5], [1, 3], [0, 2], [1, 5],
    [0, 6], [4], [2, 8], [0, 6], [4], [2, 8], [0, 6], [4], [2, 8],
    [3, 7], [6, 8], [5, 7], [3, 7], [6, 8], [5, 7], [3, 7], [6, 8], [5, 7]
]


def get_valid_blocks(old_move, block_stat):
    """Determine valid blocks."""
    if old_move == (-1, -1):
        return [x for x in xrange(9)]
    else:
        move_to_num = old_move[0] * 9 + old_move[1]
        if move_to_num >= 0 and move_to_num <= 80:
            final = []
            possible_blocks = num_to_block[move_to_num]
            for i in possible_blocks:
                if block_stat[i] == '-':
                    final.append(i)
            return final
        else:
            sys.exit(1)


def get_empty_out_of(gameb, blal, block_stat):
    """Function to test `get_playable_cells` against."""
    cells = []  # it will be list of tuples
    # Iterate over possible blocks and get empty cells
    for idb in blal:
        id1 = idb / 3
        id2 = idb % 3
        for i in range(id1 * 3, id1 * 3 + 3):
            for j in range(id2 * 3, id2 * 3 + 3):
                if gameb[i][j] == '-':
                    cells.append((i, j))

    # If all the possible blocks are full, you can move anywhere
    if cells == []:
        new_blal = []
        all_blal = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        for i in all_blal:
            if block_stat[i] == '-':
                new_blal.append(i)

        for idb in new_blal:
            id1 = idb / 3
            id2 = idb % 3
            for i in range(id1 * 3, id1 * 3 + 3):
                for j in range(id2 * 3, id2 * 3 + 3):
                    if gameb[i][j] == '-':
                        cells.append((i, j))
    return cells


def get_playable_cells(board, blocks_allowed, block_stat):
    """Get playable cells."""
    p_cells = []
    # First check the 'free' moves:
    for block in blocks_allowed:
            v = (int(block / 3)) * 3
            h = (block % 3) * 3
            for i in range(v, v + 3):
                for j in range(h, h + 3):
                    if board[i][j] == '-':
                        p_cells.append((i, j))
    if p_cells == []:
        for block in xrange(9):
            if block_stat[block] == '-':
                v = (int(block / 3)) * 3
                h = (block % 3) * 3
                for i in range(v, v + 3):
                    for j in range(h, h + 3):
                        if board[i][j] == '-':
                            p_cells.append((i, j))
    return p_cells

#Check win
def terminal_state_reached(block_stat):
	### we are now concerned only with block_stat
	bs = block_stat
	## Row win
	if (bs[0] == bs[1] and bs[1] == bs[2] and bs[1]!=0 and bs[1]!=3) or (bs[3]!=0 and bs[3]!=3 and bs[3] == bs[4] and bs[4] == bs[5]) or (bs[6]!=3 and bs[6]!=0 and bs[6] == bs[7] and bs[7] == bs[8]):
		return True
	## Col win
	elif (bs[0] == bs[3] and bs[3] == bs[6] and bs[0]!=0 and bs[0]!=3) or (bs[1] == bs[4] and bs[4] == bs[7] and bs[4]!=0 and bs[4]!=3) or (bs[2] == bs[5] and bs[5] == bs[8] and bs[5]!=0 and bs[5]!=3):
		return True
	## Diag win
	elif (bs[0] == bs[4] and bs[4] == bs[8] and bs[0]!=0 and bs[0]!=3) or (bs[2] == bs[4] and bs[4] == bs[6] and bs[2]!=0 and bs[2]!=3):
		return True
	else:
		for i in range(9):
			if block_stat[i] == 0:
                            return False
		
		else:
			point1,point2 = 0,0
			for i in bs:
				if i == 1:
					point1 += 1
				if i == 2:
					point2 += 1
				
			if point1>point2:
				return True
			elif point2>point1:
				return False
			else:
				return True

def is_terminal_state(block_stat, key):
    """Check if terminal state is reached"""
    bs = block_stat
    for setup in win_orientation:
        line = []
        for cell in setup:
            tmp1, tmp2 = cell[0], cell[1]
            tmp = tmp1 * 3 + tmp2
            line.append( bs[tmp] )
        if line[0] == line[1] == line[2] == key:
            return True

    for i in block_stat:
        if i == 0:
            return False

    p1, p2 = 0, 0
    for i in block_stat:
        if i == 1:
            p1 += 1
        elif i == 2:
            p2 += 1

    if p1 >= p2:
        return True

    else:
        return False

def update_block_state( board, old_move, block_stat, key ):
    """Check if block captured"""
    if old_move == (-1, -1):
        return block_stat

    old_x = old_move[0]
    old_y = old_move[1]

    board[old_x][old_y] = key

    block_x = old_move[0] / 3
    block_y = old_move[1] / 3

    hor = block_x * 3
    ver = block_y * 3
    block_num = hor + block_y


    for setup in win_orientation:
        #An auxilliary list to store a line of a 3x3 grid
        line = []
        #Check what lies in the possible win orientations
        for cell in setup:
            tmp1, tmp2 = hor + cell[0], ver + cell[1]
            line.append( board[tmp1][tmp2] )
        #declare winner of block, if one
        if line[0] == line[1] == line[2] != '-':
            block_stat[block_num] = key
            return block_stat

    for i in range(hor, hor + 3):
        for j in range(ver, ver + 3):
            if board[i][j] == '-':
                return block_stat

    block_stat[block_num] = 'D'
    return block_stat

gb = [
        [ 'x','x','o',  'x', 'x', 'o',  '-', '-', 'x'],
        [ 'o','x','x',  'x', 'x', '-',  '-', '-', 'x'],
        [ '-','o','o',  'o', '-', 'o',  'o', 'o', 'o'],

        [ 'x','x','-',  'o', 'x', '-',  '-', '-', '-'],
        [ 'o','x','-',  'x', 'o', 'o',  '-', '-', '-'],
        [ 'x','o','-',  'o', 'x', 'x',  '-', '-', '-'],

        [ '-','x','o',  'x', 'x', 'o',  'o', '-', 'x'],
        [ '-','-','x',  'x', '-', 'x',  'o', '-', 'x'],
        [ '-','-','o',  'x', '-', 'o',  'o', 'x', 'o'],
]
move_bs_o = {
        (2, 0) : [ 'o', '-', 'o',  '-', '-', '-', '-', 'x', 'o'],
        (3, 5) : [ '-', '-', 'o',  '-', 'o', '-', '-', 'x', 'o'],
        (7, 0) : [ '-', '-', 'o',  '-', '-', '-', '-', 'x', 'o'],
        (5, 7) : [ '-', '-', 'o',  '-', '-', '-', '-', 'x', 'o']
}

move_bs_x = {
        (2, 0) : [ 'D', '-', 'o',  '-', '-', '-', '-', 'x', 'o'],
        (3, 2) : [ '-', '-', 'o',  'x', '-', '-', '-', 'x', 'o'],
        (3, 5) : [ '-', '-', 'o',  '-', 'D', '-', '-', 'x', 'o'],
        (2, 4) : [ '-', 'x', 'o',  '-', '-', '-', '-', 'x', 'o']
}

block_stat_list = [
	[1,2,1,2,3,2,1,2,1],
	[1,0,0,2,1,0,2,2,1],
	[2,1,2,1,2,2,1,2,1],
	[0,0,1,2,2,1,1,1,2],
	[0,0,0,0,0,0,0,0,0],
	[1,1,1,2,2,1,0,2,2],
        [1,2,1,2,1,2,1,0,0],
]

# Test functions below this line


def test_bs_o():
    """Update bs when o moves."""
    for i in move_bs_o:
        bs = [ '-', '-', 'o',  '-', '-', '-', '-', 'x', 'o']
        assert update_block_state( gb, i, bs, 'o') == move_bs_o[i]

def test_bs_x():
    """Update bs when x moves."""
    for i in move_bs_x:
        bs = [ '-', '-', 'o',  '-', '-', '-', '-', 'x', 'o']
        assert update_block_state( gb, i, bs, 'x') == move_bs_x[i]

#Note that evaluator function given returns true for either 2 or 1, any one winning
def test_terminality():
    """Test if game over."""
    for i in block_stat_list:
	assert is_terminal_state(i,1) == terminal_state_reached(i)

def test_valid_blocks():
    """Test `get_valid_blocks`."""
    a = ['-'] * 9
    for ver in xrange(8):
        for hor in xrange(8):
            x = determine_blocks_allowed((ver, hor), a)
            y = get_valid_blocks((ver, hor), a)

            assert x == y


def test_playable_cells_bal():
    """Test `get_playable_cells` given allowed blocks."""
    row = ['-'] * 9
    board = []
    for i in xrange(9):
        board.append(row)
    b_stat = ['-'] * 9

    for b_al in num_to_block:
        assert get_playable_cells(board, b_al, b_stat) ==\
            get_empty_out_of(board, b_al, b_stat)


def test_playable_cells_not_bal():
    """Test `get_playable_cells` with allowed blocks empty."""
    row = ['-'] * 9
    board = []
    for i in xrange(9):
        board.append(row)
    b_stat = '-xoxoxoxo'
    b_al = []

    assert get_playable_cells(board, b_al, b_stat) == get_empty_out_of(board,
                                                                       b_al,
                                                                       b_stat)



"""
a = ['-'] * 9
ver = int(raw_input('v:'))
hor = int(raw_input('h:'))


x = determine_blocks_allowed((ver, hor), a)
y = get_valid_blocks((ver, hor), a)

print x
print y

"""

# class AITest(unittest.TestCase):
