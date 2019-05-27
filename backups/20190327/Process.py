from Atomic import Atomic
from Message import Message
import Constant

class Process(Atomic):

    def __init__(self, model_name):
        super().__init__(model_name)
        self.sigma = 7.0
        self.state = "busy"
    
    @Atomic.internal_time_advance
    def internal_transition(self, time):
        print(self.model_name+" : "+str(time))
        self.holdIn(Constant.PASSIVE, Constant.INF)

        message = Message(
            self, "out", "in", "out"
        )
        return message
    
    @Atomic.external_time_advance
    def external_transition(self, message, time):
        print(self.model_name+" : "+str(time)+str(message.value))
        if self.state == "busy":
            if message.destination_port == "in":
                self.holdIn("busy",self.sigma)
        if self.state == "passive":
            if message.destination_port == "in":
                self.holdIn("busy", self.sigma)

    def output(self, message, time):
        assert type(message) is Message
        print(str(time)+str(message.value))
