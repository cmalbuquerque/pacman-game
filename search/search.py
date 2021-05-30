# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def genericGraphSearch(problem, structure):
    startNode = problem.getStartState()
    explored = set() # set of explored nodes
    # (Node, list of actions until to achieve the node)
    structure.push((startNode, list()))

    if problem.isGoalState(startNode): # returns actions if is the goal
        return list()
    
    while not structure.isEmpty():
        currentNode, actions = structure.pop() # returns the element of structure
            
        if currentNode not in explored:
            explored.add(currentNode)

            for successorNode, action, cost in problem.getSuccessors(currentNode):
                if successorNode not in explored:
                    # copy actions list and append the new action to achieve the goal
                    nextAction = actions.copy() 
                    nextAction.append(action) 

                    if problem.isGoalState(successorNode): # returns actions if is the goal
                        return nextAction
                        
                    # add the list of actions to achieve the current node
                    structure.push((successorNode, nextAction))
    return list()


def depthFirstSearch(problem):
    structure = util.Stack() # stack because use LIFO implementation
    return genericGraphSearch(problem, structure)



def breadthFirstSearch(problem):
    structure = util.Queue() # queue because use FIFO implementation
    return genericGraphSearch(problem, structure)


def uniformCostSearch(problem):
    startNode = problem.getStartState()
    explored = set() # set of explored nodes
    structure = util.PriorityQueue() # queue because use FIFO implementation

    # ((Node, list of actions until to achieve the node), cost)
    structure.push((startNode, list()), 0)

    if problem.isGoalState(startNode): # returns actions if start node is the goal
        return list()
    
    while not structure.isEmpty():
        currentNode, actions = structure.pop() # returns the priority element

        if currentNode not in explored:
            explored.add(currentNode)

            for successorNode, action, cost in problem.getSuccessors(currentNode):
                nextAction = actions.copy() 
                nextAction.append(action)

                if problem.isGoalState(successorNode): # returns actions if is the goal
                    return nextAction
                
                # get the cost of the actions' path
                pathCost = problem.getCostOfActions(nextAction)
                # add the list of actions to achieve the current node
                structure.update((successorNode, nextAction), pathCost)
                
    return list()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
