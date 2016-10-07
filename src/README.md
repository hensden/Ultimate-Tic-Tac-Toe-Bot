# Source README

## How Evaluator works

1. First, `game_board` and `block_stat` are initialised. They are basically list of lists. They are initialised to the following:
```
game_board =   
                 [[- - -  - - -  - - -],
                 `[- - -  - - -  - - -],`
                 `[- - -  - - -  - - -],`

                 [- - -  - - -  - - -],
                 [- - -  - - -  - - -],
                 [- - -  - - -  - - -],

                 [- - -  - - -  - - -],
                 [- - -  - - -  - - -],
                 [- - -  - - -  - - -]]
```
`block_stat` =   `[- - - - - - - - -]`

2. A track is kept of the `old_move`. Initially, it is `(-1, -1)`. The player is assigned a `fl` or flag which is **x** or **o**.

3. The main game loop then commences. Here, the players make their `move`. To the `move` function, the `temp_board_state`, `temp_block_state`, `old_move` and `fl` is passed. Using this information only, the player has to pick the best move.

## What we have to do

Make a bot that plays this game obviously. It should be similar to `Player2` in the given code.

Refer to [this](https://moodle.iiit.ac.in/mod/forum/discuss.php?d=688) for more.
