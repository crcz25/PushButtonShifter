"""
All the functions listed below are the posible states 
for the FSM with its own execute call
"""
State = type("State", (object,), {})

class Parking(State):
  def Execute(self):
    print('Car is in parking')

class Reverse(State):
  def Execute(self):
    print('Car is in reverse')

class Neutral(State):
  def Execute(self):
    print('Car is in neutral')

class Drive(State):
  def Execute(self):
    print('Car is in drive')

class Manual(State):
  def Execute(self):
    print('Car is in manual')

class Transition(object):
  def __init__(self, toState):
    self.toState = toState

  def Execute(self):
    print('Transitioning...')