from collections import deque
from logging import exception

from wsproto.frame_protocol import NULL_MASK


# Stack - Last in First Out
# QUEUE - FIRST In FIRST OUT


class operations:
    def __init__(self):
        self.items=deque()


    def add_element(self,element):
        self.items.append(element)


    def stack_pop(self):
        if not self.items:
            return "No itemd, First add items to the LIST"
        return self.items.pop()

    def queue_pop(self):
        if not self.items:
            return "No itemd, First add items to the LIST"
        #WRONG WAY AS THIS IS ONLY A TEMPORARY COPY OF YOUR LIST AND NEVER POPS ITEMS FROM ACTUAL LIST
        #return deque(self.items).popleft()
        return self.items.popleft()

    def printlist(self):
        return self.items



operations_obj= operations()
print(operations_obj.queue_pop())
print(operations_obj.stack_pop())
operations_obj.add_element(45)
operations_obj.add_element(25)
operations_obj.add_element(75)
operations_obj.add_element(145)
operations_obj.add_element(40)
print(operations_obj.printlist())
print(operations_obj.queue_pop())
print(operations_obj.stack_pop())
print(operations_obj.printlist())

