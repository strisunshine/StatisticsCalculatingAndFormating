import sys

class State:

    def __init__(self, line, neighbors):
        pass
        
    def __str__(self):
        pass


class StateList(list):

    def __init__(self, fname, neighbors):
        pass
        self.checkIntegrity()

    def checkIntegrity(self):
        pass

    def printSortedPopReverse(self):
        pass

    def printSortedDegreeReverse(self):
        pass

    def computeNetworkDensity(self):
        pass

    def printTriStates(self):
        pass

    def findTwoNeighborsLargestPop(self):
        pass        

    def __str__(self):
        pass    


class Neighbors(dict):

    def __init__(self, fname):
        pass            

    def __str__(self):
        pass
    

if __name__ == "__main__":
    neighbors = Neighbors("us_states_adjacency.txt")
    sList = StateList("us_states.txt", neighbors)
    
    print '-'*50 + '\nStates sorted by population:\n' + '-'*50
    sList.printSortedPopReverse()

    print '-'*50 + '\nStates sorted by degree:\n' + '-'*50    
    sList.printSortedDegreeReverse()

    print '-'*50 + '\nTristates:\n' + '-'*50    
    sList.printTriStates()

    print "Most populous neighbors %s = %d" % sList.findTwoNeighborsLargestPop()

    print "\nNetwork density = %5.3f" % sList.computeNetworkDensity()
    
