import random
import sys 
import dj as d

class Dungeion:
    def __init__(self,level,row,column):
        self.level = level
        self.row = row
        self.column = column
        
        C = []
        self.visited = []
        self.item = [".","#"]
        self.whole_door = [True]
        self.current_level = 1

        self.xq= []
        self.yq= []
        self.x = 0
        self.y = 0

        self.move_count = 0
        self.node_layer = 1
        self.node_next_layer = 0
        self.reach = False
        self.graph = []

        self.dx = [-1,+1,0,0]
        self.dy = [0,0,+1,-1]

        self.Dungeion_map= []
        
    def walk(self,x,y):
        for i in range(4):
            self.x = x + self.dx[i]
            self.y = y + self.dy[i]

            if self.x < 0 or self.y < 0:
                continue
            if self.x >= self.row or self.y >= self.column:
                continue
            if self.Dungeion_map[self.x][self.y] == "#":
                continue
            if self.Dungeion_map[self.x][self.y] == "X":
                continue
            if self.Dungeion_map[self.x][self.y] == "E":
                self.reach = True
                break
            
            self.Dungeion_map[self.x][self.y] = "X"
            self.xq.append(self.x)
            self.yq.append(self.y)
            self.node_next_layer+=1
            
    def solve(self):
        self.xq.append(self.x)
        self.yq.append(self.y)
        self.Dungeion_map[self.x][self.y] = "X"
        
        while len(self.xq) > 0:
            
            x = self.xq.pop()
            y = self.yq.pop()
            self.walk(x,y)
            if self.reach == True:
                break
            self.node_layer-=1
            if self.node_layer == 0:
                self.node_layer = self.node_next_layer
                self.node_next_layer = 0
                self.move_count+=1
            self.print_dungeion()

            

            
        
        
        if self.reach:
            print("Done!")
        else:
            print("Trapped!")
        
        
    def generate_map(self):
        dunMap = [[None for j in range(self.row)]for i in range(self.column)]
        for i in range(self.column):
            for j in range(self.row):
                a = random.choice(self.item)
                if i == 0 and j == 0:
                    dunMap[i][j] = "S"
                    continue

                    
                elif a == "#":
                    dunMap[i][j] = "#"
                elif a == ".":
                    dunMap[i][j] = "."
        if self.whole_door[0] == True:
            door_random = [i for i in range(self.row)]
            rann = random.choice(door_random)
            dunMap[random.choice(door_random)][random.choice(door_random)] = "E"
            self.whole_door[0] = False
            
                
                     
        self.Dungeion_map = dunMap
        self.visited = self.Dungeion_map
        for i in range(self.row):
            list1 =[]
            for j in range(self.column):
                
                if self.Dungeion_map[i][j] == ".":
                    list1.append(1)
                elif self.Dungeion_map[i][j] == "S":
                    list1.append(1)
                elif  self.Dungeion_map[i][j] == "#":
                    list1.append(0)
                else:
                    list1.append(1)
            self.graph.append(list1)
        print(self.graph)

        for i in range(self.column):
            for j in range(self.row):
                print(self.graph[i][j],end=" ")
            print()
                    
        


    def print_dungeion(self):
        for i in range(self.column):
            for j in range(self.row):
                print(self.Dungeion_map[i][j],end=" ")
            print()

a = Dungeion(1,4,4)
a.generate_map()
a.print_dungeion()
b = d.Graph(a.row)
b.graph(a.graph)
        
        

    






