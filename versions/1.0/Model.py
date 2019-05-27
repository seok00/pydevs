import Constant

class Coupling:
    """
    One way.
    Connections are defined by couplings
    """

    def __init__(self, source_port, source, target_port, target):
        """        
        Arguments:
            port {[str]} -- [port to compare between ports,
                            id of the same port at source and
                            target can be different]
            source {[Model]} -- [source of messages]
            target {[Model]} -- [destination of messages]
        """

        """assert type(source_port) is str
        assert type(target_port) is str
        assert type(source) is Model
        assert type(target) is Model"""
        self.source_port = source_port
        self.target_port = target_port
        self.source = source
        self.target = target

class Model:
    """
    Atomic and Coupled are subclass of model
    """
    def __init__(self, model_name,next_event_time = Constant.INF):
        self.model_name = model_name
        # Global time of last event
        self.last_event_time = 0.0
        # Global time of next event
        self.next_event_time = next_event_time
        # Set of ports
        self.coupling_list = []

    def add_coupling(self, source_port, source, target_port, target):
        # Both input and output ports are appended to the coupling list
        self.coupling_list.append(
            Coupling(source_port, source, target_port, target)
        )
 