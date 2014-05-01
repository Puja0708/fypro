import queue
import sys
import chat
from twisted.internet.protocol import Factory
from twisted.protocols.basic import LineReceiver
from twisted.internet import reactor

class queue1:

	def __init__():
    	return self.items = []

	def isEmpty(self):
    	return self.items == []

	#enqueue = queue.put()
	def enqueue(self, items):
		self.items.insert(0, items)

	def dequeue(self):
    	return self.items.pop()

     #queue.qsize()
    	

	q=queue1()

#q.enqueue(nameer)
#q.isEmpty()
	
#q.enqueue('chat.handle_GETNAME.name')
	q.enqueue(4)
#q=Queue()
#q.isEmpty()


#q.enqueue(4)
#q.enqueue('dog')
#q.enqueue(True)
	print q.size()	