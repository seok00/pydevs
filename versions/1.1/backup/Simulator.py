from Model import Model
from Message import Message
from Atomic import Atomic
from Port import Port
from Processor import Processor

class Simulator(Processor):
    def __init__(self, name, parent=None):
        super().__init__(name, parent)
        self.model = model


    def process(self, message):
        assert issubclass(message, Message)
        result = None
        if type(message) is Message.X:
            # arrival of external event, global time
            # 1. Update time variables
            # 2. execute external transition function
            # 3. repond with a done message
            self.lastEventTime = self.nextEventTime
            self.nextEventTime = self.model.timeAdvance()
            self.model.externalTransition(message)
            return Message.Done(self.model, self.nextEventTime)
        elif type(message) is Message.Star:
            # Time to execute internal transition
            # 1. Get output of current phase's internal transition
            # 2. Comput internal transition function
            # 2. Send y message with the output
            # 3. Send done message to indicate state transition has been carried out and proved next event time
            
            self.lastEventTime = self.nextEventTime
            self.nextEventTime = self.model.timeAdvance()
            # the output variable below is the y message
            output = self.model.output()
            self.model.internalTransition()
            return output, Message.Done(self.model, self.nextEventTime)
        else:
            raise(ValueError("Wrong message type received. Simulators can only receive type X and Star messages"))


