class AVLSearchBinaryTree_Insert:
    def __init__(self, value, leftChild_Node, rightChild_Node, parent_Node):
        self.value = value
        self.leftChild_Node = leftChild_Node
        self.rightChild_Node = rightChild_Node
        self.parent_Node = parent_Node

        self.balanceFactor = 0
        self.heigth = 0


    def count(self):
        left = 0 if self.leftChild_Node == None else 1 + self.leftChild_Node.count()
        right = 0 if self.rightChild_Node == None else 1 + self.rightChild_Node.count()

        return left + right


    def isBill(self):
        return self.leftChild_Node == None and self.rightChild_Node == None

    def contains_index(self, i):
        if self.value[1] == i:
            return self.value
        if self.value[1] - i < 0:
            if self.leftChild_Node is None:
                return None
            return self.leftChild_Node.contains_index(i)
        if self.rightChild_Node is None:
            return None
        return self.rightChild_Node.contains_index(i)
        

    def contains(self, v):
        if self.value[0] == v[0] and self.value[1] == v[1]:
            return True
        if self.value[1] - v[1] < 0:
            return self.leftChild_Node != None and self.leftChild_Node.contains(v)
        return self.rightChild_Node != None and self.rightChild_Node.contains(v)


    def insert(self, v):
        if self.contains(v):
            return
        
        self.insert__(v)
    

    def insert__(self, v):

        if self.value[1] - v[1] < 0:
            if self.rightChild_Node != None:
                self.rightChild_Node.insert__(v)
            else:
                self.rightChild_Node = AVLSearchBinaryTree_Insert(v, None, None, self)

                #verify balance factor and height
                if self.leftChild_Node == None:
                    self.heigth += 1
                    self.update_heigth()
                
                self.update_balance_factor()
        else:
            if self.leftChild_Node != None:
                self.leftChild_Node.insert__(v)
            else:
                self.leftChild_Node = AVLSearchBinaryTree_Insert(v, None, None, self)

                #verify balance factor and height
                if self.rightChild_Node == None:
                    self.heigth += 1
                    self.update_heigth()
                
                self.update_balance_factor()


    def update_heigth(self):
        if self.parent_Node == None:
            return
        
        if self.parent_Node.leftChild_Node != None and self.parent_Node.rightChild_Node != None:
            if self.parent_Node.leftChild_Node.heigth == self.parent_Node.rightChild_Node.heigth:
                self.parent_Node.heigth = self.parent_Node.leftChild_Node.heigth + 1
                return
            self.parent_Node.heigth = max(self.parent_Node.leftChild_Node.heigth, self.parent_Node.rightChild_Node.heigth) + 1
            self.parent_Node.update_heigth()
            return
        
        self.parent_Node.heigth = self.parent_Node.leftChild_Node.heigth + 1 if self.parent_Node.leftChild_Node != None else self.parent_Node.rightChild_Node.heigth + 1
        self.parent_Node.update_heigth()


    def update_balance_factor(self):
        if self.isBill():
            self.balanceFactor = 0
        elif self.leftChild_Node == None:
            self.balanceFactor = self.rightChild_Node.heigth + 1
        elif self.rightChild_Node == None:
            self.balanceFactor =  - (self.leftChild_Node.heigth + 1)
        else:
            self.balanceFactor = self.rightChild_Node.heigth - self.leftChild_Node.heigth

        #don't exist balance -> rotate
        if self.balanceFactor < -1:
            if self.leftChild_Node != None and self.leftChild_Node.balanceFactor == 1:
                # --, + case
                self.leftChild_Node.leftRotate()
                self.rightRotate()
            if self.leftChild_Node != None and self.leftChild_Node.balanceFactor == -1:
                # --, - case
                self.rightRotate()
    
        if self.balanceFactor > 1:
            if self.rightChild_Node != None and self.rightChild_Node.balanceFactor == 1:
                # ++, + case
                self.leftRotate()
            elif self.rightChild_Node != None and self.rightChild_Node.balanceFactor == -1:
                # ++, -
                self.rightChild_Node.rightRotate()
                self.leftRotate()


    def leftRotate(self):
        h = self.heigth
        p = self.parent_Node
        self.leftChild_Node = AVLSearchBinaryTree_Insert(self.value, self.leftChild_Node, self.rightChild_Node.leftChild_Node, self)

        self.value =  self.rightChild_Node.value
        self.rightChild_Node = self.rightChild_Node.rightChild_Node

        if self.rightChild_Node != None:
            self.rightChild_Node.parent_Node = self

        self.parent_Node = p

        #update heigth
        #if right == null not chains heigth -> double rotate
        if self.rightChild_Node != None:
            self.heigth = h - 1
            self.leftChild_Node.heigth = self.heigth - 1

            if self.parent_Node != None:
                self.parent_Node.heigth -= 1
                self.parent_Node.update_heigth()
            self.balanceFactor = 0
        else:
            self.balanceFactor = -1
        
        self.leftChild_Node.balanceFactor = 0


    def rightRotate(self):
        h = self.heigth
        p = self.parent_Node
        self.rightChild_Node = AVLSearchBinaryTree_Insert(self.value, self.leftChild_Node.rightChild_Node, self.rightChild_Node, self)

        self.value =  self.leftChild_Node.value
        self.leftChild_Node = self.leftChild_Node.leftChild_Node

        if self.leftChild_Node != None:
            self.leftChild_Node.parent_Node = self

        self.parent_Node = p

        #update heigth
        #if right == null not chains heigth -> double rotate
        if self.leftChild_Node != None:
            self.heigth = h - 1
            self.rightChild_Node.heigth = self.heigth - 1

            if self.parent_Node != None:
                self.parent_Node.heigth -= 1
                self.parent_Node.update_heigth()
            self.balanceFactor = 0
        else:
            self.balanceFactor = 1
        
        self.rightChild_Node.balanceFactor = 0


    def __str__(self):
        return '{ ' + str(self.leftChild_Node) + ' } , { '  + str(self.value) + ' } , { ' + str(self.rightChild_Node) + ' )  }'


    def in_order(self):
        in_order_run = []
        self.in_order__(in_order_run)
        return in_order_run


    def in_order__(self, in_order_run):

        if self.leftChild_Node != None:
            self.leftChild_Node.in_order__(in_order_run)
        
        in_order_run.append(self.value)

        if self.rightChild_Node != None:
            self.rightChild_Node.in_order__(in_order_run)