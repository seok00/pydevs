from Entity import Entity
from Model import Model
from Processor import Processor

class Atomic(Model):
    # To specify an atomic model
    # 1. Add state variable
    # 2. Specify internal transition function
    # 3. Specify external transition function
    # 4. Specify output function
    # 5. Specify time advance function
    
    def __init__(self, name, processor, parent, phaseList):
        assert issubclass(parent, Model)
        assert type(phaseList) is list
        super().__init__(name, processor, parent)
        self.phaseList = phaseList
        self.phase = None
    
    @property
    def phase(self):
        return self.phase

    @phase.setter
    def phase(self, value):
        if value not in self.phaseList:
            raise (ValueError("Wrong phase value. Phase must be in phase list"))
        else:
            self.phase = value
    
    def output(self):
        # Output based on state
        raise(NotImplementedError("You must specify output function before simulation"))
    
    def internalTransition(self):
        raise(NotImplementedError("You must specify internal transition function before simulation"))

    def externalTransition(self, externalEvent):
        raise(NotImplementedError("You must specify external transition function before simulation"))

    def timeAdvance(self):
        """
        time advance function of DEVS formalism
        changes the sigma varible
        according to its current state
        """
        raise(NotImplementedError("You must specify time advance function before simulation"))

    def reset(self):
        # Set initial state of model
        # Set sigma, phase
        # Set individual variables
        raise(NotImplementedError("You must specify reset function before simulation"))
