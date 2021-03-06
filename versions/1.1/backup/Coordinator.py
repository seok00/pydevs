from Model import Model
from Message import Message
from Atomic import Atomic
from Port import Port
from Coupled import Coupled
from Processor import Processor

class Coordinator(Processor):
     
     def __init__(self, name, parent=None, children=None):
          assert children is None or type(children) is list
          super().__init__(name, parent)
          self.children = children if children is not None else []

     @property
     def children(self):
          return self.children

     @children.setter
     def children(self, value):
          assert value is None or type(value) is list
          assert all(issubclass(child, Processor) for child in value)
          self.children = value 

     def process(self, message):
          assert issubclass(message, Message)
          if type(message) is Message.Y:
               destinations = self.model.findDestPort(message.port.model, message.port.name)
               for dest in destinations:
                    # check if message should be passed to its parent or its children
                    if dest.model in self.model.children: # its a message to sibling
                         X = Message.X(message.port.model, message.time, message.port.name, message.value)



               

