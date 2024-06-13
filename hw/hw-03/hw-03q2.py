def readADC1():
    # Placeholder function to simulate reading from an ADC.
    return 128  # Middle Value

def getDistance():
    value = readADC1()
    distance = value*0.0078125
    return distance

print(getDistance())