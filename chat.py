#import queue1
#from queue import LifoQueue
#from calculus.client_2 import RemoteCalculationClient, ClientTimeoutError
#import tictac
#from tictac import letsplay
from math import pi
from twisted.internet.protocol import Factory
from twisted.protocols.basic import LineReceiver
from twisted.internet import reactor
from twisted.internet import task
from twisted.trial import unittest
from twisted.test import proto_helpers

#p = 0

class Chat(LineReceiver):

    #enqueue = queue.LifoQueue._put()
    #size = queue.LifoQueue._qsize()


    def __init__(self, users):
        self.users = users
        self.name = None
        self.state = "GETNAME"
        #enqueue('name')
        #print size

    def connectionMade(self):
        self.sendLine("What's your name?")
        #p = p + 1
        print len(self.users)


    def connectionLost(self, reason):
        if self.name in self.users:
            del self.users[self.name]
            #p = p - 1
            len(self.users)

    def lineReceived(self, line):
        if self.state == "GETNAME":
            self.handle_GETNAME(line)
        else:
            self.handle_CHAT(line)

    def handle_GETNAME(self, name):
        if name in self.users:
            self.sendLine("Name taken, please choose another.")
            return
        self.sendLine("Welcome, %s!" % (name,))


        self.name = name
        self.users[name] = self
        self.state = "CHAT"

    def handle_CHAT(self, message):
        message = "<%s> %s" % (self.name, message)
        for name, protocol in self.users.iteritems():
            if protocol != self:
                protocol.sendLine(message)

    #def handle_queue(self):
     #   print len(self.users0)


class ChatFactory(Factory):

    def __init__(self):
        self.users = {} # maps user names to Chat instances

    def buildProtocol(self, addr):
        return Chat(self.users)

class ClientCalculationTestCase(unittest.TestCase):

    def setUp(self):
        self.tr = proto_helpers.StringTransportWithDisconnection()
        self.clock = task.Clock()
        self.proto = RemoteCalculationClient()
        self.tr.protocol = self.proto
        self.proto.callLater = self.clock.callLater
        self.proto.makeConnection(self.tr)

        

    
reactor.listenTCP(8024, ChatFactory())
reactor.run()
