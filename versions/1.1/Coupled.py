from Atomic import Atomic
from Model import Model
from Entity import Entity
from Processor import Processor
from Port import Port

class Coupling:

    def __init__(self, dstModel, dstName, srcModel, srcName):
        self.destination = Port(dstModel, dstName)
        self.source = Port(srcModel, srcName)
    
    def __eq__(self, other):
        if not issubclass(other, Coupling):
            raise (NotImplementedError("Comparison with another type is not implemented"))
        return True if self.destination == other.destination and self.source == other.source else False

class Coupled(Model):
    def __init__(self, name, processor, parent=None):
        super().__init__(name, processor, parent)
        self.children = []
        # Influences and Receivers are contained in couplings list together
        self.couplings = []
    
    def addCoupling(self, dstModel, dstName, srcModel, srcName):
        self.couplings.append(
            Coupling(dstModel, dstName, srcModel, srcName)
        )
    
    def translate(self, port):
        """
        Translates source port to list of destination ports
        Arguments:
            port {[Port]} -- [Source port to find]
        
        Returns:
            [list] -- [list of the destinations associated with source port]
        """
        destinations = []
        for coupling in couplings:
            if coupling.source == port:
                destinations.append(coupling.destination)
        return destinations
    
    def addChild(self, childModel):
        assert issubclass(childModel, Model)
        self.children.append(childModel)
        childModel.parent = self
    
    
