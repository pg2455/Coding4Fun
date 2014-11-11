
########################################## BASIC NODE OF A TREE ##########################################
class TreeNode():
    def __init__(self,key, val, left=None,right =None, parent = None):
        self.key = key
        self.val = val
        self.left = left
        self.right= right
        self.parent = parent

    def hasRightChild(self):
        return self.right

    def hasLeftChild(self):
        return self.left

    def getRightChild(self):
        return self.right

    def getLeftChild(self):
        return self.left

    def isRightChild(self):
        # if parent is none it will give error in second condition
        return self.parent and self.parent.getRightChild() == self

    def isLeftChild(self):
        # if parent is none it will give error in second condition
        return self.parent and self.parent.getLeftChild() == self

    def hasAnyChild(self):
        return self.left or self.right

    def hasBothChildren(self):
        return self.left and self.right

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not self.left and not self.right

    def hasOnlyOneChild(self):
        # XOR the left and right
        return self.hasLeftChild() ^ self.hasRightChild()

    def replaceNodeData(self,key,val,lc,rc):
        self.left = lc
        self.right = rc
        self.val = val
        self.key = key
        if self.hasLeftChild():
            self.left.parent = self
        if self.hasRightChild():
            self.right.parent = self

########################################## BINARY SEARCH TREE : UNBALANCED AND UNAUGMENTED ##########################################
class binarySearchTree():
    def __init__(self):
        self.size = 0
        self.root = None

    def length(self):
        return self.size

    #method oveloading because same method i.e. len is called with this class else it expects list;
    # __add__ : operator overriding
    # calling : len(tree)
    def __len__(self):
        return self.size

    # calling : tree[key] = val
    def __setitem__(self,key, val):
        self.put(key,val)

    # BST with left <= root < right
    def put(self,key,val):
        # if there is no root then make it as a root
        if self.root:
            self._put(key,val,self.root)
        else:
            self.root = TreeNode(key,val)
        # increment the size
        self.size +=1

    def _put(self,key,val,currentNode):
        # left recursive insert
        if key <= currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key,val,currentNode.left)
            else:
                currentNode.left = TreeNode(key,val,parent = currentNode)
        # right recursive insert
        else:
            if currentNode.hasRightChild():
                self._put(key,val,currentNode.right)
            else:
                currentNode.right = TreeNode(key,val,parent = currentNode)

    # calling : tree[key]
    def __getitem__(self,key):
        return self.get(key)

    # calling: key in tree
    def __contains__(self,key):
        if self._get(key):
            return True
        else:
            return False

    # tree.get(key)
    def get(self,key):
        if self.root:
            node = self._get(key,self.root)
            # None.val is wrong so check before calling that
            if node:
                return node.val
            else:
                return None
        else:
            return None

    #get the node corresponding to a key
    def _get(self,key, currentNode):
        # make sure currentNode exists otherwise subsequent if will give error
        if not currentNode:
            return None
        # check and return node itself
        if key < currentNode.key:
            return self._get(key,currentNode.left)
        elif key > currentNode.key:
            return self._get(key, currentNode.right)
        else:
            return currentNode

    # method overriding
    def __delitem__(self,key):
        self.delete(key)

    def delete(self,key):
        # if there is even one node in the tree : go ahead and perform
        if self.size >1:
            nodeToRemove = self._get(key)
            # if key exists then delete it otherwise raise error
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size -=1
            else:
                raise KeyError('Error: Key not found')

        elif self.size ==1 and self.root.key == key:
            self.root = None
            self.size = 0
        else:
            raise KeyError('Error, key not in tree')

    def remove(self, node):
        # if the node is itself a leaf: simply delete it
        if node.isLeaf():
            if node.isLeftChild():
                node.parent.left = None
            else:
                node.parent.right = None

        # if there is only one child of the node: make its child the child of the parent
        elif node.hasOnlyOneChild():
            whichChild =  [node.left,node.right][node.right != None]

            # if the node is root: then just replace this node with its child
            if node.isRoot():
                node.replaceNodeData(whichChild.key,whichChild.val,whichChild.left,whichChild.right)
            else:
                # update the parent's attachment to the children
                if node.isLeftChild():
                    node.parent.left = whichChild
                else:
                    node.parent.right = whichChild
                # update the parent of the node's children
                whichChild.parent = node.parent

           # reference to the currentNode is now finished

        #if it has both children
        elif node.hasBothChildren():
            # get the successor of that node: now the successor is at leaf
            # replace it with successor
            # delete the successor which will be now at the leaf
            successor =  self.getSuccessor(node)

            successor.left = node.left
            node.left.parent = successor

            successor.right = node.right
            node.right.parent = successor


            successor.parent = node.parent
            if node.isLeftChild():
                node.parent.left = successor
            else:
                node.parent.right = successor

            self.remove(successor)

        else:
            return None

    #successor
    def getSuccessor(self,node):
        if node.hasRightChild():
            return self.findMin(node)
        else:
            while node.isRoot() or node.isRightChild():
                node =  node.right
            if node.isRoot():
                return None
            else:
                return node

    #min
    def findMin(self,node):
        if self.root:
            while node.left:
                node = node.left
            return node
        else:
            return None

    # max
    def findMax(self,node):
        if self.root:
            while node.right:
                node = node.right
            return node
        else:
            return None


########################################## TREE TRAVERSAL  ##########################################
#inorder
def inOrder(root, out = []):
    if root:
        inOrder(root.left)
        print root.key,root.val
        inOrder(root.right)

# get result in a list
def inOrder(root, out = []):
    if root:
        inOrder(root.left,out)
        out.append((root.key,root.val))
        inOrder(root.right,out)
    return out

#preorder
def preOrder(root):
    if root:
        print root.key,root.val
        preOrder(root.left)
        preOrder(root.right)

#postorder
def postOrder(root):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print root.key,root.val



########################################## TESTER  ##########################################
def main():
    mytree = binarySearchTree()
    mytree[3]="red"
    mytree[4]="blue"
    mytree[6]="yellow"
    mytree[2]="at"
    print 'in order walk: ', inOrder(mytree)
    print 'post order walk: ', postOrder(mytree)
    print 'pre order walk:', preOrder(mytree)

    return mytree
