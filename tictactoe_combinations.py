from copy import deepcopy 
import time



class Node:
    def __init__(self):
        self.key = None
        self.value = None
        self.children = dict()
        
class decisionTree:
    def __init__(self):
        self.turn = 0
        self.Owinningpaths = []
        self.Xwinningpaths = []
        self.root = Node()
        self.root.key = ()
        self.root.value =  [None for i in range(9)]
        self.constructTree(self.root , self.turn)
    
    def constructTree(self , currentNode , turn):
        if turn>5:
            haswon = self.won(currentNode.value)
            if (haswon[0]):
                if (haswon[1]==0):
                    self.Owinningpaths.append(currentNode.key)
                else:
                    self.Xwinningpaths.append(currentNode.key)
                return
                    
                
            
        for x in range(9):
            if (currentNode.value[x]== None):
                currentNode.children[x] = Node()
                currentNode.children[x].key = currentNode.key + (x , )
                currentNode.children[x].value = deepcopy(currentNode.value)
                currentNode.children[x].value[x] = (1 if turn%2==0 else 0)
                self.constructTree(currentNode.children[x] , turn+1)
    def won(self , array):
        Ozig = 0
        Xzig = 0
        for x in range(3):
            Orow = 0
            Ocol = 0
            Xrow = 0
            Xcol = 0
            
            for y in range(3):
                if(array[(3*x)+y]==0):
                    Orow+=1
                if(array[(3*y)+x]==0):
                    Ocol+=1
                if(array[(3*x)+y]==1):
                    Xrow+=1
                if(array[(3*y)+x]==1):
                    Xcol+=1
            if (Orow==3 or Ocol==3):
                return (True  , 0)
            elif (Xrow==3 or Xcol==3):
                return (True  , 1)
        
            if(array[(3*x)+x]==0):
                Ozig+=1
            if(array[(3*x)+(2-x)]==0):
                Xzig+=1
        if (Ozig==3):
                return (True  , 0)
        elif (Xzig==3):
                return (True  , 1)
        return(False , 0)
        
         
        
            
                
                
                
if __name__ == "__main__":
    start = time.time()
    TicTacToe = decisionTree()
    end = time.time()
    print(end - start)
    
    
                
                
                