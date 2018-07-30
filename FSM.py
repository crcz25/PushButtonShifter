class FSM(object):
  """
  Creates the FSM:
    shifter = object that uses FSM
    states = dictionary of states complementary with states file
    transitions = dictionary of posible changes from to where ex. toDrive
    currState = actual state in that moment of time
    trans = transition used to get that state until the change is done
    successTransition = flag to know if the change was posible 
        (no self return to state)
  """
  def __init__(self, shifter):
    self.shifter = shifter
    self.states = {}
    self.transitions = {}
    self.currState = None
    self.trans = None
    self.successTransition = 0

  def SetState(self, stateName):
    """
    Tries to change the state only if the FMS comes from other state and
    updates successTransition
    """
    if self.currState is not self.states[stateName]:
      self.currState = self.states[stateName]
      self.successTransition = 1
    else:
      print("Already in", stateName)
      self.successTransition = 0

  def Transition(self, transName):
    """
    Record how you get to that state (transition) until change is complete
    """
    self.trans = self.transitions[transName]

  def Execute(self):
    """
    If there is a chance to change state it tries to,
    and executes the new state actions if change was a success
    """
    if self.trans:
      self.trans.Execute()
      self.SetState(self.trans.toState)
      self.trans = None

    if self.successTransition:
      self.currState.Execute()