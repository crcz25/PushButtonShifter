from pprint import pprint

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

class FSM(object):
    def __init__(self, shifter):
        self.shifter = shifter
        self.states = {}
        self.transitions = {}
        self.currState = None
        self.trans = None

    def SetState(self, stateName):
        self.currState = self.states[stateName]

    def Transition(self, transName):
        self.trans = self.transitions[transName]

    def Execute(self):
        if self.trans:
            self.trans.Execute()
            self.SetState(self.trans.toState)
            self.trans = None
        self.currState.Execute()

class Shifter(object):
    def __init__(self):
        self.FSM = FSM(self)
        self.Parking = True
    

def selectedGear(shifterInput):
    return {
        'p': 'toParking',
        'r': 'toReverse',
        'n': 'toNeutral',
        'd': 'toDrive',
        'm': 'toManual',
    }[shifterInput]

def main():
    shifterInput = input('Select gear: ')
    gear = selectedGear(shifterInput)
    print()
    pprint(vars(shifter))
    pprint(vars(shifter.FSM))
    print()
    print('Gear selected', gear)
    print()
    
    if shifter.Parking and gear is not 'toParking':
        shifter.FSM.Transition(str(gear))
        shifter.Parking = False
    elif gear == 'toParking':
        shifter.FSM.Transition(str(gear))
        shifter.Parking = True
    else:
        shifter.FSM.Transition(str(gear))
        shifter.Parking = False

    shifter.FSM.Execute()
    print()
    pprint(vars(shifter))
    pprint(vars(shifter.FSM))

if __name__ == '__main__':
    try:
        shifter = Shifter()

        shifter.FSM.states["Parking"] = Parking()
        shifter.FSM.states["Reverse"] = Reverse()
        shifter.FSM.states["Neutral"] = Neutral()
        shifter.FSM.states["Drive"] = Drive()
        shifter.FSM.states["Manual"] = Manual() 

        shifter.FSM.transitions["toParking"] = Transition("Parking")
        shifter.FSM.transitions["toReverse"] = Transition("Reverse")
        shifter.FSM.transitions["toNeutral"] = Transition("Neutral")
        shifter.FSM.transitions["toDrive"] = Transition("Drive")
        shifter.FSM.transitions["toManual"] = Transition("Manual")
        
        shifter.FSM.SetState("Parking")

        while True:
            main()

    except KeyboardInterrupt:
        pass
