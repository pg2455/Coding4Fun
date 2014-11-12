#Hash tables
class KeyValue():
    def __init__(self,key,value):
        self.key = key
        self.value = value

class HashTable():
    def __init__(self):
        self.__TABLESIZE = 30 #need to hide this number because hash function relies on this
        self.list = [[]]*self.__TABLESIZE

    #define hash map
    def hash(self, key):
        return sum([ord(i) for i in key]) % self.__TABLESIZE

    #set some key
    def set(self, key, value):
        tmp = KeyValue(key,value)
        self.list[self.hash(key)].append(tmp)
        return True

    #get value of a key
    def get(self, key):
        bucket =  self.list[self.hash(key)]
        for i in bucket:
            if i.key == key:
                return i.value
        return False

has = HashTable()
has.set('jim',12)
has.set('kim', 13)
has.set('mij',23)

##graphs :
graph = { 'A' : ['B','C'],
'B' : ['C','D'],
'C' : ['D'],
'D' : ['C'],
'F' : ['C'],
'E' : ['F']
}

#find_path between two nodes in a graph

# user dont need to pass path..its for recursion purpose
def find_path(graph,start,end,path = []):
    path = path + [start]
    if start == end:
        return path
    if not graph.has_key(start):
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph,node,end,path)
            if newpath: return newpath
    return None

#multiple paths
def multi_path(graph,start,end,path =[]):
    path =path + [start]
    if start == end:
        return [path]
    if not graph.has_key(start):
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            pdb.set_trace()
            newpaths = multi_path(graph,node,end,path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

# find shortest new path
def shortest_path(graph,start,end,path =[]):
    path = path + [start]
    if start ==end:
        return path
    if not graph.has_key(start):
        return None
    shortest =None
    for node in graph[start]:
        if node not in path:
            newpath = shortest_path(graph,node,end,path)
            if not shortest or len(newpath) < len(shortest):
                shortest = newpath
    return shortest
