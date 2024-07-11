# Game of Life

## Description
This project implements Conway's Game of Life, a cellular automaton devised by mathematician John Conway. The game consists of a grid of cells that can live, die, or multiply based on a few mathematical rules.

## Rules
1. Any live cell with fewer than two live neighbours dies (underpopulation).
2. Any live cell with two or three live neighbours lives on to the next generation.
3. Any live cell with more than three live neighbours dies (overpopulation).
4. Any dead cell with exactly three live neighbours becomes a live cell (reproduction).

## Project Structure

- **game_of_life.py**: Contains the main implementation of the Game of Life.
- **README.md**: This file.

## How to Run

1. Clone this repository:
   ```sh
   git clone https://github.com/your-username/game-of-life.git
