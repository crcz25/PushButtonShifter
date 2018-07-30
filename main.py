def selectedGear(shifterInput):
    return {
        'p': 'Parking',
        'r': 'Reverse',
        'n': 'Neutral',
        'd': 'Drive',
        'm': 'Manual',
    }[shifterInput]

def main():
    shifterInput = input('Select gear: ')
    gear = selectedGear(shifterInput)
    print('Gear selected', gear)

if __name__ == '__main__':
    while True:
        main()