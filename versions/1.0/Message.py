from Model import Model
class Message:

    def __init__(self, source, source_port, destination_port, value):
        """
        Arguments:
            source {[Model]} -- [source model of the message]
            port {[str]} -- [port]
            value {[any]} -- [actual message]
        """
        # assert type(source) is Model
        # assert type(source_port) is str
        # assert type(destination_port) is str
        # message can be any type
        self.source = source
        self.source_port = source_port
        self.destination_port = destination_port
        self.value = value

