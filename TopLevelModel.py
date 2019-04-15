import Constant
from Coupled import Coupled
from Model import Model

class TopLevelModel(Coupled):
    """
    Top level model
    contains the generator, transducer and 
    user specified simulation models
    """

    def __init__(self, model_name, time_limit = Constant.INF):
        super().__init__(model_name)
        # time limit of simulation
        # When INF, simulation will run until termination or message end has been made
        # When elsse, simulation will stop if current time passes limit
        self.time_limit = time_limit
        # Current simulation time
        self.simulation_time = 0.0
    
    def run_simulation(self):
        self.simulation_time = 0.0
        while self.simulation_time < self.time_limit and self.simulation_time != Constant.INF:
            self.simulation_time = self.get_next_event_time()
            self.internal_transition(self.simulation_time)
    


        
