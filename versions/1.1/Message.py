from Port import Port
from Model import Model
from Processor import Processor
   

class Message:
    

    class X(Message):
        def __init__(self, source, time, port=None, value=None):
            super().__init__(source, time, port, value)
    class Y(Message):
        def __init__(self, source, time, port=None, value=None):
            super().__init__(source, time, port, value)
    class Done(Message):
        def __init__(self, source, time, port=None, value=None):
            super().__init__(source, time, port, value)
    class Star(Message):
        def __init__(self, source, time, port=None, value=None):
            super().__init__(source, time, port, value)
    
    def __init__(self, source, time, port, value):
        """[__init__]
        Arguments:
            source {[Processor]} -- [Source processor of the message]
            time {[float]} -- [Time when the message was sent]
        
        Keyword Arguments:
            port {[Port]} -- [Source port of the message](default: {None})
            value {any} -- [Value to be carried with the message] (default: {None})
        """
        self.source = source
        self.time = time
        self.port = port
        self.value = value

    @property
    def source(self):
        return self.source

    @source.setter
    def source(self, instance):
        assert issubclass(instance, Processor)
        self.source = instance

    @property
    def time(self):
        return self.time
    
    @time.setter
    def time(self, value):
        assert type(value) is float
        self.time = value

    @property
    def port(self):
        return self.port
    
    @port.setter
    def port(self, instance):
        assert isinstance(instance, Port) or instance is None
        self.port = port

