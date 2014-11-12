from pythonds.graphs import Graph,Vertex

def knightGraph(bdsize):
    ktgraph = Graph()
    for row in range(bdsize):
        for col in range(bdsize):
            nodeId = posTonodeId(row,col,bdsize)
            legalMovesID = genLegalMovesID(row,col,bdsize)
            for move in legalMovesID:
                ktgraph.addEdge(nodeId,move)
    return ktgraph

def posTonodeId(row,col,bdsize):
    if (row > bdsize -1 ) or (col> bdsize -1) or row<0 or col <0:
        return None
    return row*bdsize + col

def genLegalMovesID(row,col,bdsize):
    moves = [(row+2,col+1),(row+2,col-1),(row-2,col+1),(row-2,col-1),(row+1,col+2),(row+1,col-2),\
    (row-1,col+2),(row-1,col-2)]
    args = [(move[0],move[1],bdsize) for move in moves]
    movesID = [posTonodeId(*arg) for arg in args]
    return [ID for ID in movesID if ID]

# limit = bdsize*bdsize -1
def ktour(n,path,u,limit):
    u.setColor('gray')
    path.append(u)
    if n<limit:
        nbr = order_by_avail(u)
        done = False # true only when n = 63
        i = 0
        while i < len(nbr) and not done:
            if nbr[i].getColor() == 'white':
                done = ktour(n+1, path, nbr[i],limit) # implicit stacking
            i=i+1
        if not done: # backtrack
            path.pop()
            u.setColor('white')
    else:
        done = True
    return done

# speed up the process; use a heuristics for searching
def order_by_avail(n):
    avail_list = []
    for v in n.getConnections():
        if v.getColor() == 'white':
            c =0
            for w in v.getConnections():
                if w.getColor() == 'white':
                    c+=1

            avail_list.append((w,c))
    avail_list.sort(key = lambda x:x[1])
    return [i[0] for i in avail_list]
