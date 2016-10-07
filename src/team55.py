"""Team 55 module."""
import random
# import datetime

# generated using `modules/gen_block_map.py`

# Obviously not hand coded. Used another program to generate these.
num_to_valid = [
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

# The possible combinations for capturing a block
win_orientation = [
    # diagonal
    ((0, 0), (1, 1), (2, 2)),
    ((2, 0), (1, 1), (0, 2)),

    # vertical
    ((0, 0), (1, 0), (2, 0)),
    ((0, 1), (1, 1), (2, 1)),
    ((0, 2), (1, 2), (2, 2)),

    # horizontal
    ((0, 0), (0, 1), (0, 2)),
    ((1, 0), (1, 1), (1, 2)),
    ((2, 0), (2, 1), (2, 2))
]

block_map = [
    [0, 0, 0, 1, 0, 2, 1, 0, 1, 1, 1, 2, 2, 0, 2, 1, 2, 2],
    [0, 3, 0, 4, 0, 5, 1, 3, 1, 4, 1, 5, 2, 3, 2, 4, 2, 5],
    [0, 6, 0, 7, 0, 8, 1, 6, 1, 7, 1, 8, 2, 6, 2, 7, 2, 8],
    [3, 0, 3, 1, 3, 2, 4, 0, 4, 1, 4, 2, 5, 0, 5, 1, 5, 2],
    [3, 3, 3, 4, 3, 5, 4, 3, 4, 4, 4, 5, 5, 3, 5, 4, 5, 5],
    [3, 6, 3, 7, 3, 8, 4, 6, 4, 7, 4, 8, 5, 6, 5, 7, 5, 8],
    [6, 0, 6, 1, 6, 2, 7, 0, 7, 1, 7, 2, 8, 0, 8, 1, 8, 2],
    [6, 3, 6, 4, 6, 5, 7, 3, 7, 4, 7, 5, 8, 3, 8, 4, 8, 5],
    [6, 6, 6, 7, 6, 8, 7, 6, 7, 7, 7, 8, 8, 6, 8, 7, 8, 8]
]


def flatten_board(board):
    """Turn 2d board representation into 1d."""
    b = []
    for i in xrange(9):
        for j in xrange(9):
            b[i * 9 + j] = board[i][j]
    return b


class Player5:
    """AI Bot class."""

    def __init__(self):
        """Constructor."""
        self.valid_moves = []
        self.cells = []

    def move(self, board, blocks_state, old_move, flag):
        """Make a move."""
        # k, m = adv_alphabeta(board, blocks_state, old_move, flag,
        #                     advanced_utility, 0, -12000, 12000)
        # m = adv_search(board, blocks_state, old_move, flag,
        #               self.advanced_utility)
        # return m


class Player55:
    """AI Bot class."""

    def __init__(self):
        """Constructor."""
        self.board = []
        self.blocks_state = []
        self.flag = ''

        self.valid_moves = []
        self.cells = []
        self.moves = 0
        self.ply = 0
        self.ply_factor = 6
        self.good_terminal = False
        self.util = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    def is_good_terminal(self, blocks):
        """Check if a good terminal state is reached."""
        flag = self.flag
        if blocks[0] == blocks[1] == blocks[2] == flag:
            self.good_terminal = True
            return True
        if blocks[3] == blocks[4] == blocks[5] == flag:
            self.good_terminal = True
            return True
        if blocks[6] == blocks[2] == blocks[8] == flag:
            self.good_terminal = True
            return True
        if blocks[0] == blocks[3] == blocks[6] == flag:
            self.good_terminal = True
            return True
        if blocks[1] == blocks[4] == blocks[7] == flag:
            self.good_terminal = True
            return True
        if blocks[2] == blocks[5] == blocks[8] == flag:
            self.good_terminal = True
            return True
        if blocks[2] == blocks[4] == blocks[6] == flag:
            self.good_terminal = True
            return True
        if blocks[0] == blocks[4] == blocks[8] == flag:
            self.good_terminal = True
            return True

    def is_bad_terminal(self, blocks):
        """Check if a good terminal state is reached."""
        flag = 'x' if self.flag == 'o' else 'o'
        if blocks[0] == blocks[1] == blocks[2] == flag:
            return True
        if blocks[3] == blocks[4] == blocks[5] == flag:
            return True
        if blocks[6] == blocks[2] == blocks[8] == flag:
            return True
        if blocks[0] == blocks[3] == blocks[6] == flag:
            return True
        if blocks[1] == blocks[4] == blocks[7] == flag:
            return True
        if blocks[2] == blocks[5] == blocks[8] == flag:
            return True
        if blocks[2] == blocks[4] == blocks[6] == flag:
            return True
        if blocks[0] == blocks[4] == blocks[8] == flag:
            return True

    def gpc(self, board, blocks_allowed):
        """Get playable cells."""
        p_cells = []
        for block in blocks_allowed:
                v = (int(block / 3)) * 3
                h = (block % 3) * 3
                for i in range(v, v + 3):
                    for j in range(h, h + 3):
                        if board[i][j] == '-':
                            p_cells.append((i, j))
        return p_cells

    def gvb(self, old_move, blocks_state):
        """Determine valid blocks."""
        if old_move == (-1, -1):
            return [x for x in xrange(9)]
        else:
            move_to_num = old_move[0] * 9 + old_move[1]
            final = []
            possible_blocks = num_to_valid[move_to_num]
            for i in possible_blocks:
                if blocks_state[i] == '-':
                    final.append(i)
            if not final:
                for i, block in enumerate(blocks_state):
                    if block == '-':
                        final.append(i)
            return final

    def move(self, board, blocks_state, old_move, flag):
        """Make a move."""
        self.board = board
        self.blocks_state = blocks_state
        self.flag = flag

        num_of_cells = 0
        self.moves += 1
        self.ply = 0
        if self.moves > 6:
            self.ply = 1
        if self.moves > 25:
            self.ply = 2
        """
        if self.moves >= self.ply_factor:
            self.ply_factor = 45
            self.ply = 1

        if self.moves > 6:
            self.ply = 1
            num_of_cells = len(self.gpc(board, self.gvb(old_move,
                                        blocks_state)))
            num_of_cells = num_of_cells ** 4
            if num_of_cells < 10000 and self.moves > 17:
                self.ply = 0
            if num_of_cells < 100 and self.moves > 20:
                self.ply = 0
            if num_of_cells < 40 and self.moves > 25:
                self.ply = 0

        # print "Ply: ", self.ply + 3, " Moves: ", self.moves,
        """
        # print "Number of cells: ", num_of_cells**self.ply
        m = self.alphabeta(board, blocks_state, old_move, flag, self.ply)
        # m = adv_search(board, blocks_state, old_move, flag,
        #               self.advanced_utility)
        # print m
        return m

    def update_block_state(self, board, old_move, g_block_stat, key):
        """Check if block captured."""
        block_stat = g_block_stat[:]

        if old_move == (-1, -1):
            return block_stat

        block_x = old_move[0] / 3
        block_y = old_move[1] / 3

        hor = block_x * 3
        ver = block_y * 3
        block_num = hor + block_y
        tmp = block_map[block_num]
        if board[tmp[0]][tmp[1]] == board[tmp[2]][tmp[3]] ==\
           board[tmp[4]][tmp[5]] == key:
            block_stat[block_num] = key
            return block_stat

        if board[tmp[6]][tmp[7]] == board[tmp[8]][tmp[9]] ==\
           board[tmp[10]][tmp[11]] == key:
            block_stat[block_num] = key
            return block_stat

        if board[tmp[12]][tmp[13]] == board[tmp[14]][tmp[15]] ==\
           board[tmp[16]][tmp[17]] == key:
            block_stat[block_num] = key
            return block_stat

        if board[tmp[0]][tmp[1]] == board[tmp[6]][tmp[7]] ==\
           board[tmp[12]][tmp[13]] == key:
            block_stat[block_num] = key
            return block_stat

        if board[tmp[2]][tmp[3]] == board[tmp[8]][tmp[9]] ==\
           board[tmp[14]][tmp[15]] == key:
            block_stat[block_num] = key
            return block_stat

        if board[tmp[4]][tmp[5]] == board[tmp[10]][tmp[11]] ==\
           board[tmp[16]][tmp[17]] == key:
            block_stat[block_num] = key
            return block_stat

        if board[tmp[0]][tmp[1]] == board[tmp[8]][tmp[9]] ==\
           board[tmp[16]][tmp[17]] == key:
            block_stat[block_num] = key
            return block_stat

        if board[tmp[4]][tmp[5]] == board[tmp[8]][tmp[9]] ==\
           board[tmp[12]][tmp[13]] == key:
            block_stat[block_num] = key
            return block_stat
        """
        for setup in win_orientation:
            # An auxilliary list to store a line of a 3x3 grid
            line = []
            # Check what lies in the possible win orientations
            for cell in setup:
                tmp1, tmp2 = hor + cell[0], ver + cell[1]
                line.append(board[tmp1][tmp2])
            # declare winner of block, if one
            if line[0] == line[1] == line[2] != '-':
                block_stat[block_num] = key
                return block_stat
        """

        for i in range(hor, hor + 3):
            for j in range(ver, ver + 3):
                if board[i][j] == '-':
                    return block_stat

        block_stat[block_num] = 'D'
        return block_stat

        for i in range(hor, hor + 3):
            for j in range(ver, ver + 3):
                if board[i][j] == '-':
                    return block_stat

        block_stat[block_num] = 'D'
        return block_stat

    def get_valid_blocks(self, old_move, blocks_state):
        """Determine valid blocks."""
        if old_move == (-1, -1):
            return [x for x in xrange(9)]
        else:
            move_to_num = old_move[0] * 9 + old_move[1]
            final = []
            possible_blocks = num_to_valid[move_to_num]
            for i in possible_blocks:
                if blocks_state[i] == '-':
                    final.append(i)
            if not final:
                for i, block in enumerate(blocks_state):
                    if block == '-':
                        final.append(i)
            return final

    def get_playable_cells(self, board, blocks_allowed, blocks_state):
        """Get playable cells."""
        p_cells = []
        for block in blocks_allowed:
                v = (int(block / 3)) * 3
                h = (block % 3) * 3
                for i in range(v, v + 3):
                    for j in range(h, h + 3):
                        if board[i][j] == '-':
                            p_cells.append((i, j))
        return p_cells

    def alphabeta(self, board, blocks_state, old_move, flag, ply):
        """Basic Alpha-Beta pruning algorithm."""
        if old_move == (-1, -1):
            return (3, 3)
        playable_cells =\
            self.get_playable_cells(board, self.get_valid_blocks(old_move,
                                                                 blocks_state),
                                    blocks_state)
        alpha = best_score = float('-inf')
        beta = float('inf')
        best_move = []
        for move in playable_cells:
            temp_blocks_st = blocks_state[:]
            board[move[0]][move[1]] = flag
            temp_blocks_st = self.update_block_state(board, move, blocks_state,
                                                     flag)
            score = self.alpha_min(board, temp_blocks_st, move, flag, 0, alpha,
                                   beta, ply)
            # print score
            board[move[0]][move[1]] = '-'
            if score == best_score:
                best_move.append(move)
            if score > best_score:
                best_score = score
                best_move = [move]
            alpha = max(alpha, best_score)
            if alpha >= beta:
                    break
        print best_score
        return best_move[random.randrange(len(best_move))]

    def alpha_min(self, board, blocks_state, old_move, flag, depth, alpha,
                  beta, ply):
        """Min part of the minimax adversarial search."""
        if self.is_good_terminal(blocks_state) is True:
                return float('inf')
        t_flag = 'o' if flag == 'x' else 'x'
        if depth > 2 + ply:
            return self.advanced_utility(flag, board, blocks_state, old_move)
        playable_cells =\
            self.get_playable_cells(board, self.get_valid_blocks(old_move,
                                                                 blocks_state),
                                    blocks_state)
        if not playable_cells:
            return self.advanced_utility(flag, board, blocks_state, old_move)
        best_score = float('inf')
        # best_move = []
        # best_blocks_state = blocks_state[:]
        for move in playable_cells:
            temp_blocks_st = blocks_state[:]
            board[move[0]][move[1]] = t_flag
            temp_blocks_st = self.update_block_state(board, move,
                                                     temp_blocks_st, t_flag)
            score = self.alpha_max(board, temp_blocks_st, move, flag,
                                   depth + 1, alpha, beta, ply)
            board[move[0]][move[1]] = '-'
            if score < best_score:
                best_score = score
                # best_move = move
                # best_blocks_state = temp_blocks_st
            beta = min(beta, best_score)
            if alpha >= beta:
                break
        # board[best_move[0]][best_move[1]] = t_flag
        # util = self.advanced_utility(flag, board, best_blocks_state,
        #                 best_move)
        # board[best_move[0]][best_move[1]] = '-'
        return best_score

    def alpha_max(self, board, blocks_state, old_move, flag, depth, alpha,
                  beta, ply):
        """Max part of the minimax adversarial search."""
        if self.is_bad_terminal(blocks_state) is True:
                return float('-inf')
        if depth > 2 + ply:
            return self.advanced_utility(flag, board, blocks_state, old_move)
        playable_cells =\
            self.get_playable_cells(board, self.get_valid_blocks(old_move,
                                                                 blocks_state),
                                    blocks_state)
        if not playable_cells:
            return self.advanced_utility(flag, board, blocks_state, old_move)
        best_score = float('-inf')
        # best_move = playable_cells[0]
        # best_blocks_state = blocks_state[:]
        for move in playable_cells:
            temp_blocks_st = blocks_state[:]
            board[move[0]][move[1]] = flag
            temp_blocks_st = self.update_block_state(board, move,
                                                     temp_blocks_st, flag)
            score = self.alpha_min(board, temp_blocks_st, move, flag,
                                   depth + 1, alpha, beta, ply)
            board[move[0]][move[1]] = '-'
            if score > best_score:
                best_score = score
                # best_move = move
                # best_blocks_state = temp_blocks_st
            alpha = max(alpha, best_score)
            if alpha >= beta:
                break

        # board[best_move[0]][best_move[1]] = flag
        # util = self.advanced_utility(flag, board, best_blocks_state)
        # board[best_move[0]][best_move[1]] = '-'
        return best_score

    def advanced_utility(self, flag, board, block_state, move):
        """Advanced utility function."""
        # i = move[0] / 3 + (move[1] % 3) * 3
        bs = block_state
        score = 0
        anyflag = 0
        util = [0] * 9
        def_weight = [1] * 9
        for i in xrange(9):
            if bs[i] == flag:
                anyflag = 1
                util[i] = 1000
                if i == 0:
                    def_weight[1] *= 8
                    def_weight[3] *= 8
                    def_weight[4] *= 8

                    def_weight[6] *= 8
                    def_weight[8] *= 8
                    def_weight[2] *= 8

                elif i == 1:
                    def_weight[0] *= 8
                    def_weight[2] *= 8
                    def_weight[4] *= 8

                    def_weight[7] *= 8
                elif i == 2:
                    def_weight[1] *= 8
                    def_weight[5] *= 8
                    def_weight[4] *= 8

                    def_weight[0] *= 8
                    def_weight[6] *= 8
                    def_weight[8] *= 8
                elif i == 3:
                    def_weight[0] *= 8
                    def_weight[6] *= 8
                    def_weight[4] *= 8

                    def_weight[5] *= 8
                elif i == 4:
                    def_weight[0] *= 8
                    def_weight[2] *= 8
                    def_weight[6] *= 8
                    def_weight[8] *= 8
                elif i == 5:
                    def_weight[2] *= 8
                    def_weight[8] *= 8
                    def_weight[4] *= 8

                    def_weight[3] *= 8
                elif i == 6:
                    def_weight[3] *= 8
                    def_weight[7] *= 8
                    def_weight[4] *= 8

                    def_weight[0] *= 8
                    def_weight[2] *= 8
                    def_weight[8] *= 8
                elif i == 7:
                    def_weight[6] *= 8
                    def_weight[8] *= 8
                    def_weight[4] *= 8

                    def_weight[1] *= 8
                elif i == 8:
                    def_weight[5] *= 8
                    def_weight[7] *= 8
                    def_weight[4] *= 8

                    def_weight[0] *= 8
                    def_weight[2] *= 8
                    def_weight[6] *= 8
            elif bs[i] != '-' and bs[i] != 'D':
                util[i] = -1000
                anyflag = 1
                if i == 0:
                    def_weight[1] *= 8
                    def_weight[3] *= 8
                    def_weight[4] *= 8

                    def_weight[6] *= 8
                    def_weight[8] *= 8
                    def_weight[2] *= 8

                elif i == 1:
                    def_weight[0] *= 8
                    def_weight[2] *= 8
                    def_weight[4] *= 8

                    def_weight[7] *= 8
                elif i == 2:
                    def_weight[1] *= 8
                    def_weight[5] *= 8
                    def_weight[4] *= 8

                    def_weight[0] *= 8
                    def_weight[6] *= 8
                    def_weight[8] *= 8
                elif i == 3:
                    def_weight[0] *= 8
                    def_weight[6] *= 8
                    def_weight[4] *= 8

                    def_weight[5] *= 8
                elif i == 4:
                    def_weight[0] *= 8
                    def_weight[2] *= 8
                    def_weight[6] *= 8
                    def_weight[8] *= 8
                elif i == 5:
                    def_weight[2] *= 8
                    def_weight[8] *= 8
                    def_weight[4] *= 8

                    def_weight[3] *= 8
                elif i == 6:
                    def_weight[3] *= 8
                    def_weight[7] *= 8
                    def_weight[4] *= 8

                    def_weight[0] *= 8
                    def_weight[2] *= 8
                    def_weight[8] *= 8
                elif i == 7:
                    def_weight[6] *= 8
                    def_weight[8] *= 8
                    def_weight[4] *= 8

                    def_weight[1] *= 8
                elif i == 8:
                    def_weight[5] *= 8
                    def_weight[7] *= 8
                    def_weight[4] *= 8

                    def_weight[0] *= 8
                    def_weight[2] *= 8
                    def_weight[6] *= 8
            else:
                xs = (i / 3) * 3
                ys = (i % 3) * 3
                for setup in win_orientation:
                    line = []
                    for cell in setup:
                        t1, t2 = xs + cell[0], ys + cell[1]
                        line.append(board[t1][t2])
                    fc, nfc = 0, 0
                    for j in line:
                        if j == flag:
                            fc += 1
                        elif j != '-':
                            nfc += 1
                    sc = 0
                    if nfc and fc:
                        sc = 0
                    elif nfc:
                        sc = (10 ** nfc) * -1
                    elif fc:
                        sc = 10 ** fc
                    util[i] += sc
                if util[i] > 1000:
                    util[i] = 1000
                if util[i] < -1000:
                    util[i] = -1000

            util[i] /= 1000.0
        ans = 0
        score = 0
        if anyflag == 1 or anyflag == 0:
            for j in xrange(9):
                util[j] *= def_weight[j]
            if block_state[4] == '-':
                util[4] *= 2
            for i in util:
                score += i
        elif anyflag == 0:
            ans += weight(util, 0, 1, 2)
            ans += weight(util, 3, 4, 5)
            ans += weight(util, 6, 7, 8)
            ans += weight(util, 0, 3, 6)
            ans += weight(util, 1, 4, 7)
            ans += weight(util, 2, 5, 8)
            ans += weight(util, 0, 4, 8)
            ans += weight(util, 2, 4, 6)
            score = ans


        return score

def weight(a, x, y, z):
    
    t = a[x] + a[y] + a[z]
    bh = []
    ans = 0
    bh.append(a[x])
    bh.append(a[y])
    bh.append(a[z])
    ph,pl,nh,nl = 0,0,0,0
    for i in a:
        if i >= 0.11:
            ph += 1
        elif i >= 0.04:
            pl += 1
        if i <= -0.11:
            nh += 1
        elif i <=0.04:
            nl += 1

    if ph == 3 or nh == 3:
        ans = t * 4
    elif ph == 2 and pl == 1:
        ans = t * 3
    elif ph == 2 and nl == 1:
        ans = t * 2
    elif ph == 2 and nh == 1:
        ans = t * 1.5
    elif ph == 1 and pl == 2:
        ans = t * 2
    elif ph == 1 and nh == 2:
        ans = t * 1.5
    elif nh == 2:
        ans = t * 3
    elif nh == 1:
        ans = t * 2
    elif pl == 3 or nl == 3:
        ans = t * 1.2

    return ans
