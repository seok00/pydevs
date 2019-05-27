from Entity import Entity
from Processor import Processor

class Model(Entity):
    def __init__(self, name, parent=None):
        """[summary]
        
        Arguments:
            name {[str]} -- [name of the entity]
        
        Keyword Arguments:
            parent {[Model]} -- [parent of the model] (default: {None})
        """
        assert parent is None or issubclass(parent, Model)
        super().__init__(name)
        self.inports = []
        self.outports = []
        self.parent = parent
        self.pos = None

    @property
    def parent(self):
        return self.parent

    @parent.setter
    def parent(self, parent):
        assert issubclass(parent, Model) or parent is None
        self.parent = parent
