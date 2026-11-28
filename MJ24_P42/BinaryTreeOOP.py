class Node():
    def __init__(self, DataP):
        self.__LeftPointer = -1 #Integer
        self.__Data = DataP #Integer
        self.__RightPointer = -1 #Integer
    def GetLeft(self):
        return self.__LeftPointer
    def GetRight(self):
        return self.__RightPointer
    def GetData(self):
        return self.__Data
    def SetLeft(self, LeftPointerUpdater):
        self.__LeftPointer = LeftPointerUpdater
    def SetRight(self, RightPointerUpdater):
        self.__RightPointer = RightPointerUpdater
    def SetData(self, DataUpdater):
        self.__Data = DataUpdater

class TreeClass():
    def __init__(self):
        self.__Tree = [Node(-1) for i in range(20)] #Node
        self.__FirstNode = -1 #Integer
        self.__NumberNodes = 0 #Integer
    def InsertNode(self, NewNode):
        if self.__NumberNodes == 0:
            self.__Tree[self.__NumberNodes] = NewNode
            self.__NumberNodes += 1
            self.__FirstNode = 0
        else:
            self.__Tree[self.__NumberNodes] = NewNode
            CurrentNode = self.__FirstNode
            Placed = False

            while not Placed:
                if self.__Tree[CurrentNode].GetData() < NewNode.GetData():
                    if self.__Tree[CurrentNode].GetRight() == -1:
                        self.__Tree[CurrentNode].SetRight(self.__NumberNodes)
                        Placed = True
                    else:
                        CurrentNode = self.__Tree[CurrentNode].GetRight()
                else:
                    if self.__Tree[CurrentNode].GetLeft() == -1:
                        self.__Tree[CurrentNode].SetLeft(self.__NumberNodes)
                        Placed = True
                    else: 
                        CurrentNode = self.__Tree[CurrentNode].GetLeft()
            self.__NumberNodes += 1
    def OutputTree(self):
        if self.__NumberNodes == 0:
            print("No Nodes")
        else:
            for i in range(self.__NumberNodes):
                print(f"Left Pointer: {self.__Tree[i].GetLeft()} Right Pointer: {self.__Tree[i].GetRight()}")

TheTree = TreeClass()
TheTree.InsertNode(Node(10))
TheTree.InsertNode(Node(11))
TheTree.InsertNode(Node(5))
TheTree.InsertNode(Node(1))
TheTree.InsertNode(Node(20))
TheTree.InsertNode(Node(7))
TheTree.InsertNode(Node(15))
TheTree.OutputTree()



