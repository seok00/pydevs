from Port import Port
from Model import Model
from Processor import Processor

class Content:
    def __init__(self, port, value):
        self.port = port
        self.value = value
    
    @property
    def port(self):
        return self.port
    
    @port.setter
    def port(self, instance):
        assert isinstance(instance, Port)
        self.port = port

class Message:
    

    class X(Message):
        def __init__(self, source, time, content=None):
            super().__init__(source, time, content)
    class Y(Message):
        def __init__(self, source, time, content=None):
            super().__init__(source, time, content)
    class Done(Message):
        def __init__(self, source, time, content=None):
            super().__init__(source, time, content)
    class Star(Message):
        def __init__(self, source, time, content=None):
            super().__init__(source, time, content)
    
    def __init__(self, source, time, content=None):
        """[__init__]
        Arguments:
            source {[Processor]} -- [Source processor of the message]
            time {[float]} -- [Time when the message was sent]
        
        Keyword Arguments:
            content {Content} -- [Value to be carried with the message] (default: {None})
        """
        self.source = source
        self.time = time
        self.content = content

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
    def content(self):
        return self.content
    
    @content.setter
    def content(self, instance):
        assert isinstance(instance, Content) or instance is None
        self.content = instance

