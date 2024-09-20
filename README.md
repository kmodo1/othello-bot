# Othello AI

This bot plays Othello at a reasonably high level, and is completely coded within one python file. The bot can evaluate to a depth of ~9 during the midgame, and ~11 during the early game, and sometimes up to ~15 during the endgame, which is reasonable for python. Most of the work on this bot was done in 2022, so some of it is quite hard to read and understand (I may come back to this later to comment everything and give variables better names, but it's in this state right now).

## Rules of Othello
Othello is played on 8x8 grid with 2 players. The board starts with 2 tokens from each player (black/white, represented as `x` or `o` in the code) in a cross shape in the middle. When each player puts a token on the board, it flips all of the opponent's tokens between that new token and any other of the player's other tokens. Players may only play tokens if they flip at least one of the opponent's tokens, and the winner at the end of the game is the player with more tokens. 

## Files
- `final_bot.py` contains the actual bot, which you can run with arguments of a 64-length string board and a player to move (e.g. `.oo..o..oxxxxxx.oxxxxxxoxxoxxoxo.xoxxooooxxxxxoo.xoooo.o..oooo.. o`, which runs the bot on that board with `o` as the starting player).
- `openingbook.py` is how I generated the opening book for the bot (a pre-computed set of states and best moves that it always plays at the start). This can be run with the first argument as the max game depth you would like to compute moves for (e.g. 1 = just starting player's first move, 2 = both player's first move, etc) and the second argument as the depth for bot to evaluate.

## Algorithms/Evaluation/Bitcoding
- This bot mainly relies on [MTD(f)](https://askeplaat.wordpress.com/534-2/mtdf-algorithm/), which is an improvement to Alpha-Beta that relies on iteratively calling alpha-beta with null windows that get closer to an optimal value, and keeping track of previous calls as you go along.
- All game operations for the bot (finding moves, making moves, evaluation calculations, etc) are done with binary operations, which you can see in `final_bot.py`. This is done by representing the board as 2 64-bit integers, which one of those representing the positions of all the black tokens, and one representing all the white tokens. 
- The evaluation function for this bot was created by me, and relies mainly on:
  - stability (tokens that are impossible to take for the rest of the game), which is calculated in `newstable()`.
  - corner score (which players have taken the corners/corner adjacent squares, which are very good and somewhat bad respectively), which is calculated in `crnasc()`.
  - frontier tokens (tokens that are adjacent to empty spaces, which is generally bad), which is calculated in `front()`.
  - mobility score (how many moves each player can make), which is calculated using `getmoves()`.
  
  As well as a couple other statistics with a much smaller rating (full evaluation can be seein in `evalb()`). Winning is weighted as `99934 + final token difference`, with final token difference being how many more tokens you have at the end of the game than the opponent, giving a maximal value of `10000`.