# Tiny Chess — a 4 KB chess engine

[![bounty](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/Gendon1/tiny-chess-01/rank.svg)](https://make.fun/bounty/tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/Gendon1/tiny-chess-01/reward.svg)](https://make.fun/bounty/tiny-chess-01)

A chess engine in a single Python file ([`main.py`](main.py), 4,096 bytes) for the [make.fun bounty](https://make.fun/bounty/tiny-chess-01): build the strongest chess engine in 4 KB of Python.

## How it plays

- 0x88 board with full legal move generation: castling, en passant, promotion, check, checkmate and stalemate
- Negamax alpha-beta with iterative deepening on a fixed node budget (60,000 nodes per move, no clock), so play is fully deterministic and replays match
- Capture-only quiescence with delta pruning, plus check evasions in quiescence; checks extend the search one ply (capped by ply)
- Material plus piece-square evaluation (mirrored tables) and MVV plus history-heuristic move ordering
- Repetition-aware root: a move that would repeat a position for the third time is penalised when ahead or level and favoured when behind
- Talks to the gauntlet env at `MAKEFUN_ENV_URL` (`POST /game`, `POST /move`)

## Size

- `main.py`: 4,096 bytes (limit 4,096)
- Whole repo: under the 8,192 byte cap

## License

MIT — see [LICENSE](LICENSE).
