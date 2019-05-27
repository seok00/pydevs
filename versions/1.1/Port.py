from Model import Model

class Port:
    def __init__(self, model, portName):
        assert issubclass(model, Model)
        assert type(portName) is str
        self.model = model
        self.name = portName

    @property
    def model(self):
        return self.model

    @model.setter
    def model(self, model):
        assert issubclass(model, Model)
        self.model = model
    
    @property
    def name(self):
        return self.name
    
    @name.setter
    def name(self, value):
        assert type(value) is str
        self.name = value

    def __eq__(self, other):
        if not isinstance(other, Port):
            # don't attempt to compare against unrelated types
            return NotImplemented
        if self.model == other.model and self.name == other.name:
            return True
        else:
            return False
