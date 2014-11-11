################################################### MIN BIN HEAP ################################################

class minBinHeap():
    def __init__(self):
        self.heap = []
        self.heapsize = -1

    def insert(self,key):
        self.heap.append(key)
        self.heapsize+=1
        self.percUp(self.heapsize)

    def delete(self,key):
        pass

    def extract_min(self):
        if self.heapsize >=0:
            tmp = self.heap[0]
            self.heap[0], self.heap[self.heapsize] = self.heap[self.heapsize], self.heap[0]
            self.heapsize -=1
            self.heap.pop()
            self.heapify(0)
            return tmp

    def update(self,key_old,key_new):
        pass

    def percUp(self,i):
        parentIndex = Pindex(i)
        if i > 0 and self.heap[i] < self.heap[parentIndex]:
            self.heap[i], self.heap[parentIndex] =  self.heap[parentIndex], self.heap[i]
            self.percUp(parentIndex)

    def heapify(self,i):
        childMinIndex = self.minChild(i)
        if childMinIndex:
            minimum = self.heap[childMinIndex]
            # if the minimum is not in order property; swap it
            if self.heap[i] > minimum:
                self.heap[i], self.heap[childMinIndex] =  self.heap[childMinIndex], self.heap[i]
                self.heapify(childMinIndex)

    def buildHeap(self,aList):
        # this does not take O(n) time. it will be expensive  to go over all elements
        # all you need is to go through only n/2 elements
        #for key in aList:
        #    self.insert(key)
        self.heap = aList
        self.heapsize = len(aList) -1
        for i in range(len(aList)//2)[::-1]:
            self.heapify(i)

    def minChild(self,i):
        if 2*i+2 <= self.heapsize:
            childIndex = Cindex(i)
            # find the minimum children's index and minimum itself
            childMinIndex = childIndex[1]
            if self.heap[childIndex[0]] < self.heap[childIndex[1]]:
                childMinIndex = childIndex[0]
        elif 2*i+1 == self.heapsize:
            childMinIndex = 2*i+1
        else:
            return None

        return childMinIndex

    def peek(self):
        return self.heap[0]

def Pindex(i):
    return [i//2, i//2 -1][i%2==0]

def Cindex(i):
    return [2*i+1,2*i+2]

################################################### MAX BIN HEAP ################################################

class maxBinHeap():
    def __init__(self):
        self.heap = []
        self.heapsize = -1

    def insert(self,key):
        self.heap.append(key)
        self.heapsize+=1
        self.percUp(self.heapsize)

    def extract_max(self):
        if self.heapsize >= 0:
            tmp = self.heap[0]
            self.heap[0], self.heap[-1] = self.heap[-1],self.heap[0]
            self.heap.pop()
            self.heapsize-=1
            self.heapify(0)
            return tmp

    # moving key down, needs comparison with children
    def heapify(self,i):
        # used by extract_max and buildHeap
        # get the child with maximum value and swap it with parent
        childMaxIndex = self.maxChild(i)
        if childMaxIndex:
            maximum =  self.heap[childMaxIndex]
            #if parent is less than the child : swap it
            if self.heap[i] < maximum:
                self.heap[i], self.heap[childMaxIndex] =  self.heap[childMaxIndex], self.heap[i]
                self.heapify(childMaxIndex)

    # move a node up if order is not satisfied
    def percUp(self,i):
     # used by insert
     parentIndex =Pindex(i)
     # if parent is less than child: move the child up
     if self.heap[i] > self.heap[parentIndex]:
         self.heap[i], self.heap[parentIndex] =  self.heap[parentIndex], self.heap[i]
         self.percUp(parentIndex)

    def peek(self):
        return self.heap[0]

    def buildHeap(self, aList):
        # to make it O(n): u just need to heapify n/2 elements because
        # in any array n/2 elements are at the leaf of binary tree
        # and you need to heapify those not at leaf  an leaves will be taken
        # care of: simple enough
        self.heap = aList
        self.heapsize = len(aList) - 1
        for i in range(len(aList)//2)[::-1]:
            self.heapify(i)

    def maxChild(self,i):
        # return the index of child with maximum value
        childIndex =  Cindex(i)
        # there are two children
        if 2*i + 2 <= self.heapsize:
            childMaxIndex  = childIndex[0]
            if self.heap[childIndex[0]] < self.heap[childIndex[1]]:
                childMaxIndex =  childIndex[1]
            return childMaxIndex
        # there is only one child
        elif 2*i+1 == self.heapsize:
            return childIndex[0]
        # its a leaf
        else:
            return None

def Cindex(i):
    # return possible index of children
    return [2*i+1, 2*i+2]

def Pindex(i):
    return [i//2,i//2 -1][i%2==0]

################################################### TESTER FUNCTIONS ################################################

## minBinHeap

## tester
def main():
    heap = binHeap()
    heap.buildHeap([4,213,123,34,12,2413,412,14,23235,2,542,52,5,25,2,5,25,24,52,45,24,5,-22,3,-234,24,2])
    for i in range(100):
        print heap.extract_min(),
    for i in range(100):
        heap.insert(i)

    return heap


##  maxBinHeaptester
def main2():
    heap = maxBinHeap()
    heap.buildHeap([4,213,123,34,12,2413,412,14,23235,2,542,52,5,25,2,5,25,24,52,45,24,5,-22,3,-234,24,2])
    for i in range(100):
        print heap.extract_max(),
    for i in range(100):
        heap.insert(i)

    return heap
