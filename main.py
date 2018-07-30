from FSM import FSM
from states import Parking, Reverse, Neutral, Drive, Manual, Transition

from pprint import pprint

class Shifter(object):
    """
    Functions that create the FSM
    """
    def __init__(self):
        self.FSM = FSM(self)

def selectedGear(shifterInput):
    """
    Function that maps the keyboardInput to transitions 
    """
    return {
        'p': 'toParking',
        'r': 'toReverse',
        'n': 'toNeutral',
        'd': 'toDrive',
        'm': 'toManual',
    }[shifterInput]

def main():
    # Get desired gear to go 
    shifterInput = input('Select gear: ')
    gear = selectedGear(shifterInput)

    print()
    pprint(vars(shifter.FSM))
    print()
    print('Change gear', gear)
    print()

    # Change FSM state (if posible)
    shifter.FSM.Transition(str(gear))
    shifter.FSM.Execute()
    
    print()
    pprint(vars(shifter.FSM))

if __name__ == '__main__':
    try:
        shifter = Shifter()
        # Create states for FSM
        shifter.FSM.states["Parking"] = Parking()
        shifter.FSM.states["Reverse"] = Reverse()
        shifter.FSM.states["Neutral"] = Neutral()
        shifter.FSM.states["Drive"] = Drive()
        shifter.FSM.states["Manual"] = Manual() 

        # Create transitions for FSM
        shifter.FSM.transitions["toParking"] = Transition("Parking")
        shifter.FSM.transitions["toReverse"] = Transition("Reverse")
        shifter.FSM.transitions["toNeutral"] = Transition("Neutral")
        shifter.FSM.transitions["toDrive"] = Transition("Drive")
        shifter.FSM.transitions["toManual"] = Transition("Manual")
        
        # Set initial state
        shifter.FSM.SetState("Parking")

        while True:
            main()

    except KeyboardInterrupt:
        pass
