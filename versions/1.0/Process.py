from Atomic import Atomic
from Message import Message
import Constant

class Process(Atomic):

    def __init__(self, model_name):
        super().__init__(model_name)
        self.sigma = 7.0
        self.state = "busy"
        self.next_event_time = self.sigma

    def internal_transition(self, time):
        print(
            self.model_name + " " +
            self.state + " " +
            str(time) + " " +
            " : INT" 
        )
        self.holdIn(Constant.PASSIVE, Constant.INF)

        message = Message(
            self, "out", "in", "stop"
        )
        self.internal_time_advance(time)
        return message
    
    def external_transition(self, message, time):
        print(
            self.model_name + " " +
            self.state + " " +
            str(time) + " " +
            str(message.source.model_name) + " " +
            str(message.source_port) + " " +
            str(message.value) + " " +
            " : EXT"
        )
        self.elapsed_time = time - self.last_event_time
        if self.state == "busy":
            if message.destination_port == "in":
                self.holdIn("busy",self.sigma)
        if self.state == "passive":
            if message.destination_port == "in":
                self.holdIn("busy", self.sigma)
        self.external_time_advance(time)

    def output(self, message, time):
        assert type(message) is Message
        print(str(time)+str(message.value))
