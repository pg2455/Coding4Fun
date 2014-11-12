#dijkstra

from pythonds.graphs import Graph, PriorityQueue, Vertex

def dijkstra(graph,start):
    start.setDistance(0)
    pq =PriorityQueue()    
    pq.buildHeap([(aVertex.getDistance(),aVertex) for aVertex in graph])
    while pq.size() > 0:
        currentVert = pq.delMin()
        for nextVert in currentVert.getConnections():
            newDist = currentVert.getDistance() + currentVert.getWeight(nextVert)
            if newDist < nextVert.getDistance():
                nextVert.setDistance(newDist)
                nextVert.setPred(currentVert)
                pq.decreaseKey(nextVert, newDist)



#prim's algorithm
def prim(graph,start):
    pq = PriorityQueue()
    for v in graph:
        v.setDistance(sys.maxsize)
        v.setPred(None)
    start.setDistance(0)
    pq.buildHeap([(v.getDistance(),v) for v in graph])
    while not pq.isEmpty():
        currentVert = pq.delMin()
        currentVert.setVisited(1)
        for nextVert in currentVert.getConnections():
            newCost = currentVert.getDistance() + currentVert.getWeight(nextVert)
            if nextVert.getVisited() ==0 and newCost < nextVert.getDistance():
                nextVert.setPred(currentVert)
                nextVert.setDistance(newCost)
                pq.decreaseKey(nextVert,newCost)
