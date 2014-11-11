from pythonds.graphs import Graph, Vertex
from pythonds.basic import Queue
from collections import defaultdict

#create a graph
def buildGraph(wordFile):
    d = defaultdict(list)
    g = Graph()
    wordList = open(wordFile,'r').read().strip().split(',')
    # create a hash table
    for word in wordList:
        for i in range(len(word)):
            bucket =  word[:i] + '_' + word[i+1:]
            d[bucket].append(word)

    # create a graph
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.addEdge(word1,word2)

    return g




# start is Vertex object; implement bfs for graph g starting from start node
def bfs(g,start):
    start.setDistance(0)
    start.setPred(None)
    vertQueue = Queue()
    vertQueue.enqueue(start)
    while(vertQueue.size() > 0):
        currentVert = vertQueue.deque()
        for nbr in currentVert.getConnections():
            if nbr.getColor() =='white':
                nbr.setColor = 'gray'
                nbr.setDistance(currentVert.getDistance()+1)
                nbr.setPred(currentVert)
                currentVert.enque(nbr)
        currentVert.setColor ='black'
