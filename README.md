# Game of Life

## A bit of history

Conway's Game of Life is a cellular automaton devised by the British mathematician John Horton Conway in 1970. It is a zero-player game, meaning its evolution is determined by its initial state, requiring no further input. The game is played on a grid of square cells, where each cell can be in one of two possible states: alive or dead. The state of the grid evolves over discrete time steps according to a set of simple rules.

## Rules

The Game of Life is governed by four simple rules:

1. **Underpopulation**: Any live cell with fewer than two live neighbors dies, as if by underpopulation.
2. **Overpopulation**: Any live cell with more than three live neighbors dies, as if by overpopulation.
3. **Survival**: Any live cell with two or three live neighbors lives on to the next generation.
4. **Reproduction**: Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

The neighbors of a cell are the eight cells surrounding it horizontally, vertically, and diagonally.

## About the Code

This project is a Python implementation of Conway's Game of Life using the Pygame library. It includes a graphical interface to visualize and interact with the game.

### Features

- **Start, Pause, Reset, and Close Buttons**: Control the simulation with intuitive buttons.
- **Interactive Grid**: Click to toggle cells between alive and dead states.
- **Continuous Update**: The grid updates continuously based on the rules of the game when in play mode.
- **Frame Rate Control**: The game updates at a fixed frame rate to ensure smooth visualization.

### Usage

1. **Run the Game**: Execute the script to start the game.
2. **Control the Simulation**: Use the buttons on the right to Play, Pause, Reset, or Close the game.
3. **Toggle Cells**: Click on cells to toggle their state between alive and dead.
4. **Drag to Create Patterns**: Use the right mouse button to drag and create live cells continuously.

### Installation

To run this game, you need to have Python and Pygame installed. You can install Pygame using pip:

```bash
pip install pygame
```

###Running the Game
Simply run the script using Python:

```bash
python game_of_life.py
```