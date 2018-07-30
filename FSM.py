class FSM(object):
  def __init__(self, shifter):
    self.shifter = shifter
    self.states = {}
    self.transitions = {}
    self.currState = 'Parking'
    self.trans = None
    self.successTransition = 0

  def SetState(self, stateName):
    print()
    if self.currState is not self.states[stateName]:
      self.currState = self.states[stateName]
      self.successTransition = 1
    else:
      print("Already in", stateName)
      self.successTransition = 0

  def Transition(self, transName):
    self.trans = self.transitions[transName]

  def Execute(self):
    if self.trans:
      self.trans.Execute()
      self.SetState(self.trans.toState)
      self.trans = None

    if self.successTransition:
      self.currState.Execute()