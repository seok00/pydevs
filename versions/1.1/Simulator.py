from Model import Model
from Message import Message, Content
from Atomic import Atomic
from Port import Port
from Processor import Processor

class Simulator(Processor):


    def __init__(self, name, model, parent=None):
        """[init]
        
        Arguments:
            name {[str]} -- [Name of the entity]
            model {[Model]} -- [Model which this processor will be attached to]
        
        Keyword Arguments:
            parent {[Processor]} -- [Parent processor] (default: {None})
        """
        super().__init__(name, model, parent)

    def process(self, message):
        """[processes message]
        
        Arguments:
            message {[Message]} -- [The message of ]
        
        Returns:
            [type] -- [description]
        """
        assert issubclass(message, Message)

        if type(message) is Message.X:
            """
            Arrival of external event
            1. Time advance and set new sigma variable. This means set next internal transition time
            2. External transition
            
            Returns:
                [Message.Done] -- [Telling that it has finished its external input transition and its next event time]
            """
            self.lastEventTime = self.nextEventTime
            self.nextEventTime = self.model.timeAdvance()
            self.model.externalTransition(message.content)
            return Message.Done(self, message.time, value = self.nextEventTime)
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
            return output, Message.Done(self, message.time, value = self.nextEventTime)
        else:
            raise(ValueError("Wrong message type received. Simulators can only receive type X and Star messages"))


