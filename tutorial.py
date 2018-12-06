from transitions import Machine

class Matter(object):
    def disappear(self): 
      print("where'd all the liquid go?")

lump = Matter()

def go_to_C():
    global machine
    machine.to_C()

def after_advance():
    print("I am in state B now!")

def entering_C():
    print("I am in state C now!")

states = ['A', 'B', 'C']
transitions = [
    { 'trigger': 'melt', 'source': 'A', 'dest': 'B', 'after': 'disappear'},
    { 'trigger': 'evaporate', 'source': 'B', 'dest': 'C' }
]


machine = Machine(lump, states=states, transitions=transitions,queued=True, initial='A')
machine.add_ordered_transitions()

print(lump.state)
lump.melt()
print(lump.state)

""" 
# we want a message when state transition to B has been completed
machine.add_transition('advance', 'A', 'C', after=after_advance)

# call transition from state B to state C
machine.on_enter_B(go_to_C)

# we also want a message when entering state C
machine.on_enter_C(entering_C)
machine.advance()
 """
"""
class Shifter(object):
  def Parking(self):
    print('Car is in parking')

  def Reverse(self):
    print('Car is in reverse')

  def Neutral(self):
    print('Car is in neutral')

  def Drive(self):
    print('Car is in drive')

  def Manual(self):
    print('Car is in manual')


def after_advance():
    print("I am in state R now!")

def go_to_R():
  global machine
  machine.to_R()

def go_to_N():
  global machine
  machine.to_N()

def go_to_D():
  global machine
  machine.to_D()

def entering_R():
    print("I am in state R now!")

lump = Shifter()

states = ['P', 'R', 'N', 'D', 'O', '3', '2', '1']

transitions = [
    { 'trigger': 'drive', 'source': 'P', 'dest': 'D', 'before': 'Drive'},
    { 'trigger': 'evaporate', 'source': 'liquid', 'dest': 'gas', 'after': 'disappear' }
]

machine = Machine(lump, states=states, initial='P', queued=True)
machine.add_ordered_transitions()
machine.add_transition('advance', 'P', 'R', after=after_advance)




machine.on_enter_P(go_to_R)
machine.on_enter_R(go_to_N)
machine.on_enter_N(go_to_D)

machine.on_enter_R(entering_R)

machine.advance()

#lump.Drive()


print(machine.state)
machine.next_state()
print(machine.state)
machine.next_state()
print(machine.state)
"""