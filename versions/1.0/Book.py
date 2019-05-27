from Atomic import Atomic
from Message import Message
import Constant

class Book(Atomic):
    Borrowed = "borrowed"
    OnShelf = "onshelf"
    Due = "due"
    Fine = "fine"

    def __init__(self, model_name):
        super().__init__(model_name)
        self.sigma = 14.0
        self.next_event_time = Constant.INF
        self.state = self.OnShelf
        self.fine = 0.0

    def internal_transition(self, time):
        # takes 14 days to become 
        message = None
        if self.state == self.Borrowed:
            self.holdIn(self.Due, 1.0)
            self.fine += 1
            # Should send output to transducer
            print(
                self.model_name + " " +
                self.state + " " +
                str(time) + " " +
                " : INT" +
                " warning, book is over due date 1 days"
            )
        elif self.state == self.Due:
            self.holdIn(self.Due, 1.0)
            self.fine += 1
            print(
                self.model_name + " " +
                self.state + " " +
                str(time) + " " +
                " : INT" +
                " warning, over due date. Over " + str(self.fine) + " days"
            )
        elif self.state == self.Fine:
            self.holdIn(self.OnShelf, Constant.INF)
            print(
                self.model_name + " " +
                self.state + " " +
                str(time) + " " +
                " : INT" +
                " Fine paied, Returned"
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
        if self.state == self.OnShelf:
            if message.destination_port == "request":
                self.holdIn(self.Borrowed, 14.0)
        elif self.state == self.Borrowed:
            if message.destination_port == "return":
                self.holdIn(self.OnShelf, Constant.INF)
        elif self.state == self.Due:
            if message.destination_port == "return":
                self.holdIn(self.Fine, 0.0)
                self.fine = 0
                        
        self.external_time_advance(time)

    def output(self, message, time):
        assert type(message) is Message
        print(str(time)+str(message.value))
