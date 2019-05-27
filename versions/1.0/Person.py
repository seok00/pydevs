from Atomic import Atomic
from Message import Message
import Constant
import random


class Person(Atomic):
    Idle = "idle"
    Reading = "reading"

    def __init__(self, model_name):
        super().__init__(model_name)
        self.sigma = 1.0
        self.state = self.Idle
        self.next_event_time = self.sigma
    
    def internal_transition(self, time):
        print(
            self.model_name + " " +
            self.state + " " +
            str(time) + " " +
            " : INT" 
        )
        message = None
        if self.state == self.Idle:
            p = random.uniform(0, 8)
            if p < 12:
                self.holdIn(self.Reading, 1.0)
                message = Message(
                    self, "request", "request", ""
                )
        elif self.state == self.Reading:
            p = random.uniform(0, 14)
            if p < 11:
                self.holdIn(self.Reading, 1.0)
            else:
                self.holdIn(
                    self.Idle, 1.0
                )
                message = Message(
                    self, "return", "return", ""
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
        self.external_time_advance(time)

    def output(self, message, time):
        assert type(message) is Message
        print(str(time)+str(message.value))

