from Port import Port
from Model import Model
from Processor import Processor

class Message:
    Done = "done"
    Star = "star"
    
    class X(Message):
        def __init__(self, source, time, portName, value=None):
            """Message that represents external input to simulators
            
            Arguments:
                source {[Model]} -- [Source of the message]
                time {[float]} -- [Time when the message was created]
                portName {[str]} -- [Name of source port]
            
            Keyword Arguments:
                value {[any]} -- [Actual message that is to be passed] (default: {None})
            """
            super().__init__(source, time, portName, value)
    
    class Y(Message):
        def __init__(self, source, time, portName, value=None):
            """Message that represents external output from simulators
            
            Arguments:
                source {[Model]} -- [Source of the message]
                time {[float]} -- [Time when the message was created]
                portName {[str]} -- [Name of source port]
            
            Keyword Arguments:
                value {[any]} -- [Actual message that is to be passed] (default: {None})
            """
            super().__init__(source, time, portName, value)
    
    class Done(Message):
        def __init__(self, source, value):
            """Message that represents end of internal transition
            
            Arguments:
                source {[Model]} -- [Source of the message]
            
            Keyword Arguments:
                value {[any]} -- [Actual message that is to be passed] (default: {None})
            """
            assert type(value) is float
            # value is time of next internal event
            super().__init__(source, None, None, value)
    
    class Star(Message):
        def __init__(self, portName):
            """Message that represents start of internal transition
            
            Arguments:
                portName {[str]} -- [Name of source port]
            
            Keyword Arguments:
                value {[any]} -- [Actual message that is to be passed] (default: {None})
            """
            super().__init__(None, None, portName, Star)

    def __init__(self, source, time, portName, value=None):
        assert type(time) is float
        self.port = Port(source, portName)
        self.time = time
        self.value = value

    @property
    def port(self):
        return self.port

    @port.setter
    def port(self, instance):
        assert type(instance) is Port
        self.port = instance
    
    @property
    def time(self):
        return self.time

    @time.setter
    def time(self, value):
        assert type(time) is float
        self.time = value




