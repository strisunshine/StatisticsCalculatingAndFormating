import sys

class State:

    def __init__(self, line, neighbors):
        self.name = line[0]
        self.capital = line[1]
        self.population = line[2]
        self.area = line[3]
        self.seats =line[4]
        self.neighbors = neighbors[self.name]
              
    def __str__(self):
        
        return "%20s %20s %10s %10s %2s   %-10s" %(self.name, self.capital, self.population, self.area, self.seats, self.neighbors)
    

class StateList(list):

    def __init__(self, fname, neighbors):
        inFile = open ( 'H:\\Downloads\\IST600Python\\'+fname )
        next(inFile)
        for line in inFile: 
             line = line[:-1]       ##remove new line
             listprestrip = line.split(',') ##split by comma
             listaftstrip = []
             for x in listprestrip:
                 list_item = x.strip()  ##remove space
                 listaftstrip.append(list_item)
             listaftconvert = []
             for x in listaftstrip:
                 if x.isdigit(): 
                     list_item = int(x)
                 else:
                     list_item = x
                 listaftconvert.append(list_item)
             a = State(listaftconvert, neighbors)
             self.append(a)   
    
        self.checkIntegrity()

    def checkIntegrity(self):
        
        for stateinstance in self:
            for stateneighbor in stateinstance.neighbors.split(', '):
                i = 0
                for stateinstance2 in self:
                    if(stateinstance2.name == stateneighbor):
                        i = 1
                if(i==0):
                    print "Some errors:"
                    print "The state is %-10s, and its neighbor is %-10s" %(stateinstance.name, stateneighbor)
                    sys.exit()
 
            
    def printSortedPopReverse(self):
        print "\nPrint all states sorted by population in reverse (most populous states first):"
        for stateinstance in sorted(self, key = lambda item : item.population, reverse=True):
            print "%-20s %20s" %(stateinstance.name, stateinstance.population)
            
##        templist= []
##        for stateinstance in self:
##          templist.append(stateinstance)
##        print templist
##        templist= []
##        for stateinstance in self:
##            print stateinstance
##            templist.extend(stateinstance)

        
        ##print templist
##        sortedlist = sorted(templist, reverse=True)
##        for each in sortedlist:
##          print each
          
##        sorted1 = sorted(self, )
##        for i in sorted1:
##            print "%-20s %20s" %(i[0],i[2])

    def printSortedDegreeReverse(self):
        print "\nPrint all states sorted by their degree in the network graph:"
        for stateinstance in sorted(self, key = lambda item : (item.neighbors.count(',')+1), reverse=True):
            print stateinstance, [stateinstance.neighbors.count(',')+1]

    def computeNetworkDensity(self):
         NetworkDensity = 0
         for stateinstance in self:
            NetworkDensity += stateinstance.neighbors.count(',')+1
         return float(NetworkDensity)/(len(self)*(len(self)-1))
    def printTriStates(self):
        for stateinstance1 in self:
            for stateinstance2 in self[self.index(stateinstance1)+1:]:
##                if self.index(stateinstance2) <= self.index(stateinstance1):
##                    continue
                for stateinstance3 in self[self.index(stateinstance2)+1:]:
##                    if self.index(stateinstance3) <= self.index(stateinstance2):
##                        continue
                    if stateinstance1.name in stateinstance2.neighbors and stateinstance2.name in stateinstance3.neighbors and stateinstance3.name in stateinstance1.neighbors:
                        print stateinstance1.name+', '+stateinstance2.name+', '+stateinstance3.name
                        

                    
    def findTwoNeighborsLargestPop(self):
        maxPopofNeighborPairs = 0
        for stateinstance1 in self[:-1]:
            for stateinstance2 in self[self.index(stateinstance1)+1:]:
                if(stateinstance1.population + stateinstance2.population) >= maxPopofNeighborPairs:
                    maxPopofNeighborPairs = stateinstance1.population + stateinstance2.population
                    a = stateinstance1.name+', '+stateinstance2.name
        return (a, maxPopofNeighborPairs)

    def __str__(self):
        pass    


class Neighbors(dict):

    def __init__(self, fname):
        inFile = open ( 'H:\\Downloads\\IST600Python\\'+fname )
        for line in inFile:
             line = line[:-1]       ##remove new line
             listprestrip = line.split(',') ##split by comma
             listaftstrip = []
             for x in listprestrip:
                 list_item = x.strip()  ##remove space
                 listaftstrip.append(list_item)      
             c = len(listaftstrip)
             keyval= listaftstrip[0]
             valueval = ''
             for i in range(1,c):
                  valueval += listaftstrip[i]
                  if(i<c-1):
                       valueval += ', '
             self[keyval] = valueval
        inFile.close()

    def __str__(self):
        return "-%10s -%30s" %(self.key, self.neighbors)
    

if __name__ == "__main__":
    neighbors = Neighbors("us_states_adjacency.txt")
    print "######"
    sList = StateList("us_states.txt", neighbors)
    
    print "######"
    
    print '-'*50 + '\nStates sorted by population:\n' + '-'*50
    sList.printSortedPopReverse()

    print '-'*50 + '\nStates sorted by degree:\n' + '-'*50    
    sList.printSortedDegreeReverse()

    print '-'*50 + '\nTristates:\n' + '-'*50    
    sList.printTriStates()

    print "\nNetwork density = %5.3f" % sList.computeNetworkDensity()
    print "Most populous neighbors %s = %d" % sList.findTwoNeighborsLargestPop()
    

    
    
