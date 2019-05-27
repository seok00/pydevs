from Port import Port
from Model import Model
from enum import Enum

class Message:
    class MsgType(Enum):
        Done = "done"
        Star = "star"
        X = "x"
        Y = "y"

    def __init__(self, msgType, srcPort, dstPort, time, value=None):
        """[__init__]
        Arguments:
            msgType {[MsgType]} -- [Represents type of the message in DEVS formalism]
            srcPort {[Port]} -- [Source port of the message]
            dstPort {[Port]} -- [Destination port of the message]
            time {[float]} -- [Time when the message was sent]
        
        Keyword Arguments:
            value {[any]} -- [Value to be carried with the message] (default: {None})
        """
        self.msgType = msgType
        self.srcPort = srcPort
        self.dstPort = dstPort
        self.time = time
        self.value = value
    
    @property
    def srcPort(self):
        return self.srcPort

    @srcPort.setter
    def srcPort(self, instance):
        assert isinstance(instance, Port)
        self.srcPort = instance
    
    @property
    def dstPort(self):
        return self.dstPort

    @dstPort.setter
    def dstPort(self, instance):
        assert isinstance(instance, Port)
        self.dstPort = instance

    @property
    def time(self):
        return self.time
    
    @time.setter
    def time(self, value):
        assert type(value) is float
        self.time = value
