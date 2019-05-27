from Coupled import Coupled
from Model import Model
from Atomic import Atomic
from Port import Port

class Digraph(Coupled):
    
    def __init__(self, name, processor, parent=None):
        super().__init__(name, processor, parent)
        # Composition tree and influence digraph are implemented
        # as 'couplings' list, at Coupled

        
