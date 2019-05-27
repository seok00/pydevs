from Atomic import Atomic
from Model import Model
from Entity import Entity
from Processor import Processor
from Port import Port

class Coupled(Model):
    def __init__(self, name, processor, parent=None):
        super().__init__(name, processor, parent)
        self.children = []
        # Influences and Receivers are contained in couplings list together
        self.couplings = []
    
    def addCoupling(self, targetModel, targetName, sourceModel, sourceName):
        targetPort = Port(targetModel, targetName)
        sourcePort = Port(sourceModel, sourceName)
        self.couplings.append(
            (targetPort, sourcePort)
        )
        targetModel.inports.append(targetPort)
        sourceModel.outports.append(sourcePort)
    
    def addChild(self, childModel):
        assert issubclass(childModel, Model)
        self.children.append(childModel)
        childModel.parent = self
    
    def translate(self, source, sourcePort):
        """
        Arguments:
            source {Model} -- [source of the coupling]
            sourcePort {str} -- []
        
        Returns:
            [list] -- [list of the destinations associated with source port]
        """
        destinations = []
        for coupling in couplings:
            if coupling[1].model == source and coupling[1].name == sourcePort:
                destinations.append(coupling[0])
        return destinations
