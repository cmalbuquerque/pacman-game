# 👻 🕹 Pacman Game

Resolution of Pacman game in Python using AI approaches in order to allow the Pacman agent find paths through his maze world, both to reach a particular location and to collect food efficiently. This project is divided into steps to built general search algorithms and apply them to Pacman scenarios.

## Steps

1. [X] Finding a Fixed Food Dot using Depth First Search
2. [X] Breadth First Search
3. [X] Uniform Cost Search
4. [X] A* search
5. [X] Finding All the Corners
6. [X] Corners Problem: Heuristic
7. [X] Eating All The Dots
8. [X] Suboptimal Search

## Structure

All project code can be found on [search directory](/search) and the respective reports of steps implementation are available on [reports directory](/reports).

### Relevant Files


|   |   |
| - | - |
| **search.py** | Where all of implemented search algorithms will reside (file to edit) |
| **searchAgents.py** | Where all of implemented search-based agents will reside (file to edit) |
| **pacman.py** | The main file that runs Pacman games. This file describes a Pacman GameState type, which you use in this project |
| **game.py** | The logic behind how the Pacman world works. This file describes several supporting types like AgentState, Agent, Direction, and Grid |
| **util.py** | Useful data structures for implementing search algorithms) |
| **ghostAgents.py** | Agents to control ghosts (can be ignored) |

## How to run

**Options**

```
  -l <mediumMaze / tinyMaze / bigMaze>  -> changes the size of board
  -p <SearchAgent / GhostAgent>         -> forces to use an intelligent agent
  -a fn=<dfs / bfs / ucs / astar>       -> forces to use the search algorithm passed
  -z <0.5>                              -> window's zoom
```

**Example**

```
python3 pacman.py -l mediumMaze -p SearchAgent -a fn=depthFirstSearch
```

## Authors

- [Carolina Albuquerque](https://github.com/cmalbuquerque) (80038)
- [Manuel Cura](https://github.com/manuelcura) (76546)
