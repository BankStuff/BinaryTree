class Node:

        def __init__(self, data, parent=None):
                self.parent = parent
                self.data = data
                self.left = None
                self.right = None
        
        def leftChild(self, left):
                self.left = Node(left, self)

        def rightChild(self, right):
                self.right = Node(right, self)

        def __str__(self):
                return self.data

def ask(node):
        ans = input(str(node.data) + " Y/N ")
        if ans.upper() == 'Y':
                return node.left
        else:
                return node.right

root = Node("Does it bark?")
root.leftChild("Dog")
root.rightChild("Cat")

response = root

while True:
        response = ask(response)
        if response.left == None:
                new = input("Is it a " + str(response.data) + "? Y/N ")
                if new.upper() == 'y':
                        print('Thanks for playing!')
                        quit()
                else:
                        # TODO make the user ask a question to differaniate their animal to the guess
                        # Then add that to database for the binary tree
                        print("FAILURE!")
                        quit()


