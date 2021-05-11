# Pacman Game
Resolution of Pacman game in Python using AI approaches

## Code Structure

|  |  |
|--|--|
| **search.py** | Where all of implemented search algorithms will reside (file to edit) |
| **searchAgents.py** | Where all of implemented search-based agents will reside (file to edit) |
| **pacman.py** | The main file that runs Pacman games. This file describes a Pacman GameState type, which you use in this project |
| **game.py** | The logic behind how the Pacman world works. This file describes several supporting types like AgentState, Agent, Direction, and Grid |
| **util.py** | Useful data structures for implementing search algorithms) |
| **ghostAgents.py** | Agents to control ghosts (can be ignored) |


## How to run 

**Options:**

```
  -l <mediumMaze / tinyMaze / bigMaze>  -> changes the size of board
  -p <SearchAgent / GhostAgent>          -> forces to use an intelligent agent
  -a fn=<dfs / bfs / ucs / astar>       -> forces to use the search algorithm passed
```


```
python3 pacman.py -l mediumMaze -p SearchAgent -a fn=depthFirstSearch
``` 
