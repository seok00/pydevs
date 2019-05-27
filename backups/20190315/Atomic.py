from Model import Model
import Constant


class Atomic(Model):
    """
    Atomic model M
    M = < X, S, Y, inp, exp, l, ta>
    X = External Event Set
    S = Sequential State Set
    Y = Output Set
    inp = internal transition function
    exp = external transition function
    l = output function
    ta = time advance function

    To create an atomic model, inherit and do
    1. implement initialization function in __init__
    2. append all possible states to the state list
    3. implement internal transition function
    3.5 wrap internal transition function with 
        wrap_internal_transition decorator
    4. implement external transition function
    4.5 wrap external transition function with
        wrap_external_transition decorator
    5. specify output function
    5.5 wrap output function with wrap_output decorator

    if a model has two or more int/ext transition function
    they are distinguished inside the funcion by phase and port
    """

    def __init__(self):
        super().__init__()
        # Current state of the model
        self.state = Constant.PASSIVE  # TODO (Change the initial state)
        # Set of states the model can have
        # each state is str
        self.state_list = []
        # Amount of time for next internal transition to happen
        self.sigma = 0.0
        # Amount of time passed from previous state change
        self.elapsed_time = 0.0

    def holdIn(self, state, new_sigma):
        """
        Sets the model to a new state. And specifies time 
        until next internal transistion        
        Arguments:
            state {[str]} -- [state to be set]
            new_sigma {[float]} -- [New sigma]

        Raises:
            ValueError -- [raised when given state doesn't 
                        match any possiblestates]
        """

        assert type(state) is str
        assert type(new_sigma) is float
        if state not in self.state_list:
            raise ValueError(state + " is not in state set")
        self.state = state
        self.sigma = new_sigma

    def resume(self):
        self.sigma -= self.elapsed_time

    def internal_transition(self):
        raise NotImplementedError()

    def external_transition(self):
        raise NotImplementedError()
    
    def output(self):
        raise NotImplementedError()

    def wrap_internal_transition(self, function):
        """
        Decorator for internal transition function
        An internal transition function at the subclass
        should be wrapped by this decorator.

        This decorator will do the pre and post processing
        
        Arguments:
            function {[function]} -- [internal transition function]
        """

        def wrapper(time):
            if time == self.next_event_time:
                self.output(time)
                self.internal_transition()
                self.last_event_time = time
                self.next_event_time = self.last_event_time - self.sigma
    
                
            

