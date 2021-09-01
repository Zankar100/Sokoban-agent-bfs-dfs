# SOLVER CLASSES WHERE AGENT CODES GO
from helper import *
import random


# Base class of agent (DO NOT TOUCH!)
class Agent:
    def getSolution(self, state, maxIterations):
        return []       # set of actions


#####       EXAMPLE AGENTS      #####

# Do Nothing Agent code - the laziest of the agents
class DoNothingAgent(Agent):
    def getSolution(self, state, maxIterations):
        if maxIterations == -1:     # RIP your machine if you remove this block
            return []

        #make idle action set
        nothActionSet = []
        for i in range(20):
            nothActionSet.append({"x":0,"y":0})

        return nothActionSet

# Random Agent code - completes random actions
class RandomAgent(Agent):
    def getSolution(self, state, maxIterations):

        #make random action set
        randActionSet = []
        for i in range(20):
            randActionSet.append(random.choice(directions))

        return randActionSet


#####    ASSIGNMENT 1 AGENTS    #####


# BFS Agent code
class BFSAgent(Agent):
    def getSolution(self, state, maxIterations=-1):
        intializeDeadlocks(state)
        iterations = 0
        bestNode = None
        
        # YOUR CODE HERE
        begin = Node(state.clone(),None,None) #starting node 

        if(begin.checkWin()): #check for win condition
        	return begin.getActions()

        explored = [] #explored nodes
        queue = [begin] #to be checked
        bestNode = begin
        
        while queue:
        	node = queue.pop(0)
       		explored.append(node.getHash())

        	children = node.getChildren()

        	hashcomparequeue = []

        	for people in queue:
        		hashcomparequeue.append(people.getHash())

        	for child in children :
        		if (child.getHash() not in explored and child.getHash() not in hashcomparequeue):
        			if child.checkWin():
        				return child.getActions()

        			#if not checkDeadlock(child.state):
        			queue.append(child)
        			if(child.getHeuristic() < bestNode.getHeuristic()):
        				bestNode = child
        			if(child.getHeuristic() == bestNode.getHeuristic()):
        				if(child.getCost() < bestNode.getCost()):
        					bestNode = child




        return bestNode.getActions()   



# DFS Agent Code
class DFSAgent(Agent):
    def getSolution(self, state, maxIterations=-1):
        intializeDeadlocks(state)
        iterations = 0
        bestNode = None

        # YOUR CODE HERE
        begin = Node(state.clone(),None,None) #starting node 

        if(begin.checkWin()): #check for win condition
        	return begin.getActions()

        explored = [] #explored nodes
        queue = [begin] #to be checked
        bestNode = begin
        
        while queue:
        	node = queue.pop(-1)
       		explored.append(node.getHash())

        	children = node.getChildren()

        	hashcomparequeue = []

        	for people in queue:
        		hashcomparequeue.append(people.getHash())
        	
        	for child in children :
        		if (child.getHash() not in explored and child.getHash() not in hashcomparequeue):
        			if child.checkWin():
        				return child.getActions()

        			#if not checkDeadlock(child.state):
        			queue.append(child)
        			if(child.getHeuristic() < bestNode.getHeuristic()):
        				bestNode = child
        			if(child.getHeuristic() == bestNode.getHeuristic()):
        				if(child.getCost() < bestNode.getCost()):
        					bestNode = child

                               
        return bestNode.getActions()   



# AStar Agent Code
class AStarAgent(Agent):
    def getSolution(self, state, maxIterations=-1):
        balance=1

        intializeDeadlocks(state)
        iterations = 0
        bestNode = None
        Node.balance = balance
        
        # YOUR CODE HERE




        return []                       #remove me
        #return bestNode.getActions()   #uncomment me


#####    ASSIGNMENT 2 AGENTS    #####


# Hill Climber Agent code
class HillClimberAgent(Agent):
    def getSolution(self, state, maxIterations=-1):
        #setup
        intializeDeadlocks(state)
        iterations = 0
        bestNode = None

        # YOUR CODE HERE




        return []                       #remove me
        #return bestNode.getActions()   #uncomment me


# Genetic Algorithm code
class GeneticAgent(Agent):
    def getSolution(self, state, maxIterations=-1):
        #setup
        intializeDeadlocks(state)
        iterations = 0
        bestNode = None

        # YOUR CODE HERE




        return []                       #remove me
        #return bestNode.getActions()   #uncomment me


# Monte Carlo Tree Search Algorithm code
class MCTSAgent(Agent):
    def getSolution(self, state, maxIterations=-1):
        #setup
        intializeDeadlocks(state)
        iterations = 0
        bestNode = None

        # YOUR CODE HERE


        

        return []                       #remove me
        #return bestNode.getActions()   #uncomment me
