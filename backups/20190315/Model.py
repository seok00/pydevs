import Constant
from Coupling import Coupling

class Model:
    """
    Atomic and Coupled are subclass of model
    """
    def __init__(self, next_event_time = Constant.INF):
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
 