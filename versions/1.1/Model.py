from Entity import Entity
from Processor import Processor

class Model(Entity):
    def __init__(self, name, processor, parent=None):
        assert issubclass(processor, Processor)
        assert parent is None or issubclass(parent, Model)
        super().__init__(name)

        self.processor = processor
        self.inports = []
        self.outports = []
        self.parent = parent
        self.pos = None

    @property
    def processor(self):
        return self.processor

    @processor.setter
    def processor(self, processor):
        assert issubclass(processor, Processor)
        self.processor = processor

    @property
    def parent(self):
        return self.parent

    @parent.setter
    def parent(self, parent):
        assert issubclass(parent, Model) or parent is None
        self.parent = parent
