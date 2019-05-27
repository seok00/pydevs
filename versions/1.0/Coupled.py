from Model import Model
from Message import Message
import Constant

class Coupled(Model):

    def _init__(self,model_name):
        super().__init__(model_name)
        # list of its sub models
        # all entry must be type Model
        self.sub_model_list = []
        # list of all ports 'inside'
        # ports that are connected to itself also
        self.port_list = []
        # Amount of time for next internal transition to happen
        self.elapsed_time = 0.0
        self.next_event_time = self.get_next_event_time()
    
    def internal_transition(self, time):
        """
        Excute all internal transition of sub models 
        1. for all sub models:
            a. if next event time is same as current time
            b. excute its internal transition
            c. collect its result
        2. for all result:
            a. send to its destination
            b. excute external transition
        3. time advance
        """
        assert type(time) is float

        transition_results = []
        for sub_model in self.sub_model_list:
            if sub_model.next_event_time == time:
                sub_model_result = sub_model.internal_transition(time)
                if type(sub_model_result) is Message:
                    transition_results.append(sub_model_result)
        for result in transition_results:
            self.external_transition(result, time)
        
        # TIme advancing of coupled model
        self.last_event_time = time
        self.next_event_time = self.get_next_event_time()


    def external_transition(self, message, time):
        """
        External_transition is evoked in an output function of an internal transition.
        A coupled model's external transition acts differently from atomic models.

        Upon receiving external message
        1. Find port to send the message.
        2. Send message
        3. Excute its external transition
        4. time advance
        Arguments:
            time {[float]} -- [current global time]
            message {[Message]} -- [to port and value]
        """
        assert type(message) is Message
        assert type(time) is float
        for coupling in self.coupling_list:
            if coupling.source == message.source and\
                coupling.source_port == message.source_port:
                coupling.target.external_transition(message, time)

        self.last_event_time = time
        self.next_event_time = self.get_next_event_time()

    def get_next_event_time(self):
        min = Constant.INF
        for model in self.sub_model_list:
            if model.next_event_time < min:
                min = model.next_event_time
        
        return min
        # This function could be modified to return next event model
        # This would let us to not compare all model's next time
