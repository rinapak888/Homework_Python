class Stack:

    def __init__(self):
        self.stack = []

    def add (self, item):
        self.stack.append(item)

    def remove (self):
        return self.stack.pop()

class Queue:

    def __init__(self):
        self.queue = []

    def add (self, item):
        self.queue.append(item)

    def remove(self):
        return self.queue.pop(0)

class Deck:

    def __init__(self):
        self.deck = []

    def add(self, item, end=True):
        if end:
            self.deck.append(item)
        else:
            self.deck.insert(0, item)
    
    def remove(self, end=True):
        if end:
            return self.deck.pop()
        else:
            return self.deck.pop(0)

#return self.deck.pop() if end else self.deck.pop(0)

#queue = Queue()
#for i in range(5):
    #queue.add(i)
#print('stack before: ', queue.queue)
#print ('removed: ', queue.remove())
#print('queue now: ', queue.queue)

deck = Deck()
for i in range(3):
    deck.add(i)
print(deck.deck)

for i in range(3, 6):
    deck.add(i, False)
print(deck.deck)

print('removed from end: ', deck.remove())
print('after removal: ', deck.deck)
print('removed from start: ', deck.remove(False))
print('after removal: ', deck.deck)

class LN:

    def __init__(self, value, next = None):
        self.value, self.next = value, next

    def add_next(self, next):
        self.next = next 

    @classmethod
    def pr_l(cls, head):
        initial = head
        def rec_pr(head):
            print(head.value)
            if head.next and head.next != initial:
                rec_pr(head.next)
        rec_pr(head)

last_node = LN(3)
head = LN(1, LN(2, last_node))
other_node = LN(4, head)
last_node.add_next(other_node)

head = LN(1, LN(2, LN(3)))
other_node = LN(4, head)

node_1 = LN(1)
node_2  = LN(2)
node_1.add_next(node_2)
print(node_1.next.value)

node_1 = LN(1, LN(2))
print(node_1.next.value)

class TN:

    def __init__(self, value, links = []):
        self.value, self.links = value, links

    def add(self, node):
        self.links.append(node) #список ссылок на след. элемент

    @classmethod
    def print_depth(cls, node):
        print(node.value)
        for child in node.links:
            cls.print_depth(child)

nodes = [TN(i) for i in range(9)]
for link in [nodes[1], nodes[2]]:
    nodes[0].add(link)
for link in [nodes[3], nodes[4]]:
    nodes[1].add(link)    
for link in [nodes[5], nodes[6]]:
    nodes[2].add(link)
for link in [nodes[7], nodes[8]]:
    nodes[3].add(link)
TN.print_depth(nodes[0])


node = TN(1) # root
child_nodes = [TN(i) for i in range(2, 5)] 
for child in child_nodes:
    node.add(child) # leafs

print(node.value)
for child in child_nodes:
    print(child_nodes)          

@classmethod
def print_TB (cls, head):
    visited = []
    def bfs(head, visited, queue):
        visited.append(head)
        queue.append(head)
        while queue:
            next = queue.pop(0)
            for node in next.nodes:
                if node not in visited:
                    visited.append(node)
                    queue.append(node)

    bfs(head, visited, queue =[])
    [print]
