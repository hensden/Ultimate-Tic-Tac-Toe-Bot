starts = [
        (0, 0), (0, 3), (0, 6),
        (3, 0), (3, 3), (3, 6),
        (6, 0), (6, 3), (6, 6),
]

def gen_block_m():

    block_map = []
    for k in starts:
        tmp = []
        for i in range(3):
            for j in range(3):
                tup = (k[0] + i, k[1] + j)
                tmp.append(tup)
        block_map.append(tmp)


    print block_map
    print
    print

    for i in range(len(block_map)):
        print block_map[i]


gen_block_m()
