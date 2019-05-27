class Entity:
    def __init__(self, name):
        assert type(name) is str
        self.name = name

    @property
    def name(self):
        return self.name
    
    @name.setter
    def name(self, name):
        assert type(name) is str
        self.name = name
    
    def __eq__(self, other):
        if not isinstance(other, Entity):
            raise (NotImplemented("Compare with another type is not implemented"))
        return True if self.name == other.name else False
