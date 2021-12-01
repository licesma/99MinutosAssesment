
import queue
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def add(self, value):  # value es integer
        if value < self.val:
            if self.left == None:
                tn = TreeNode(value)
                self.left = tn
            else:
                self.left.add(value)
        else:  # this.val < value
            if self.right == None:
                tn = TreeNode(value)
                self.right = tn
            else:
                self.right.add(value)

    def getHeight(self):
        if self.left == None and self.right == None:
            return 1
        else:
            if self.left == None:
                return self.right.getHeight() + 1
            elif self.right == None:
                return self.left.getHeight() + 1
            else:
                return max(self.left.getHeight(), self.right.getHeight())


def makeTree(listTree):
    if len(listTree) == 0:
        return 0
    head = None
    for num in listTree:
        if head == None:
            head = TreeNode(num)
        else:
            head.add(num)
    return head

def bfsWithIndexes(head):
    que = queue.Queue()
    queIdx = queue.Queue()
    que.put(head)
    queIdx.put(1)
    ls = []
    lsIdx =[]
    while (not que.empty()):
        tn = que.get()
        idx = queIdx.get()
        ls.append(tn)
        lsIdx.append(idx)
        if tn.left != None:
            que.put(tn.left)
            queIdx.put(idx+1)
        if tn.right != None:
            que.put(tn.right)
            queIdx.put(idx+1)
    resNum = []
    for nd in ls:
        resNum.append(nd.val)
    return [resNum, lsIdx]

def bfs(head):
    return bfsWithIndexes(head)[0]
