class Node:
    def __init__(self,vl,l =None,r=None):
        self.l  = l
        self.r = r
        self.v = vl
    def insert(self,v):

            if self.l is None:
                self.l = Node(v)

            elif self.r is None:
                self.r = Node(v)

            elif self.l.v !=-1 and (self.l.l is None or self.l.r is None):
                self.l.insert(v)

            elif self.r.v !=-1 and (self.r.l is None or self.r.r is None):
                self.r.insert(v)
            elif self.l.v !=-1 and (self.l.l.v != -1 or self.l.r.v != -1):
                self.l.insert(v)
            elif self.r.v !=-1 and (self.r.l.v != -1 or self.r.r.v != -1):
                self.r.insert(v)
            

    def PrintTree(self):
        if self.l:
            self.l.PrintTree()
        print( self.v)
        if self.r:
            self.r.PrintTree()






def swapNodes():
    root = Node(1)
    root.insert(-1)
    root.insert(3)
    root.insert(-1)
    root.insert(4)
    root.insert(-1)
    root.insert(5)
    root.insert(-1)
    root.insert(6)

    root.PrintTree()

if __name__ == "__main__":
    swapNodes()
    