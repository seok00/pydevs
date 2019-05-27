class Message:

    def __init__(self, port, value):
        """
        Arguments:
            port {[str]} -- [destination port]
            value {[any]} -- [actual message]
        """
        self.port = port
        self.value = value

