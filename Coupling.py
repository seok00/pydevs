from Model import Model

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

        assert type(source_port) is str
        assert type(target_port) is str
        assert type(source) is Model
        assert type(target) is Model
        self.source_port = source_port
        self.target_port = target_port
        self.source = source
        self.target = target
