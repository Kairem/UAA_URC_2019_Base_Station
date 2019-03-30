import inputs

for i in inputs.devices:
    print(i)

#Method to map raw inputs to more useful values
#Raw inputs from analog sticks seem to range from 2^14 to -2^14
#A small dead zone placed in the center of the stick
#Even smaller dead zone on the outside <-- could be bigger in the future
#Displays numbers rounded to 2 decimal points
def stickMap(minOut, maxOut, x):
    if x > 32000:
        x = 32000
    elif x < -32000:
        x = -32000
    elif x < 2000 and x > -2000:
        x = 0
    #return round( (x - minIn) * (maxOut - minOut) / (maxIn - minIn) + minOut, 2)
    return round( (x + 32000) * (maxOut - minOut) / (32000 + 32000) + minOut, 2)


#Left Stick: ABS_X ABS_Y || Right Stick: ABS_RX ABS__RY
#Butons: BTN_[cardinal] (BTN_EAST) || Button State: 1 is down, 0 is up
while 1:
    events = inputs.get_gamepad()
    for evt in events:
        #if evt.code == "ABS_RX":
            #print(stickMap(-1, 1, evt.state))
        print(evt.code)
        #if (evt.code == 'BTN_SOUTH'):
            #print(evt.state)