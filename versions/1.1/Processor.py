from Entity import Entity
from Model import Model

class Processor(Entity):
    def __init__(self, name, model,parent=None):
        assert issubclass(parent, Processor) or parent is None
        assert issubclass(model, Model)
        super().__init__(name)
        
        self.lastEventTime = 0.0
        self.nextEventTime = 0.0
        # model which the Processor is processing
        self.model = model
        self.parent = parent
    @property
    def model(self):
        return self.model

    @model.setter
    def model(self, instance):
        assert issubclass(instance, Model)
        self.model = instance

    @property
    def lastEventTime(self):
        return self.lastEventTime
    
    @lastEventTime.setter
    def lastEventTime(self, value):
        assert type(value) is float or type(value) is int
        self.lastEventTime = float(value)
    
    @property
    def nextEventTime(self):
        return self.nextEventTime
    
    @nextEventTime.setter
    def nextEventTime(self, value):
        assert type(value) is float or type(value) is int
        self.nextEventTime = float(value)

    @property
    def parent(self):
        return self.parent
    
    @parent.setter
    def parent(self, instance):
        assert issubclass(instance, Processor) or instance is None
        self.parent = instance
