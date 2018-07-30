from FSM import FSM
from states import Parking, Reverse, Neutral, Drive, Manual, Transition

from pprint import pprint

class Shifter(object):
    def __init__(self):
        self.FSM = FSM(self)

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
    print('Change gear', gear)
    print()

    shifter.FSM.Transition(str(gear))
    
    """     
    if shifter.Parking and gear is not 'toParking':
        shifter.FSM.Transition(str(gear))
        shifter.Parking = False
    elif not shifter.Parking and gear == 'toParking':
        shifter.FSM.Transition(str(gear))
        shifter.Parking = True
    else:
        shifter.FSM.Transition(str(gear))
        shifter.Parking = False 
    """

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
