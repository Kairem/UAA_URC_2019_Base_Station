import wx.lib.newevent
import inputs
import threading
import time

class GamePadEvents:
    def __init__(self, frame):
        self.ButtonEvent, self.EVT_GPButton = wx.lib.newevent.NewEvent()
        self.RStickXEvent, self.EVT_GPRStickX = wx.lib.newevent.NewEvent()
        self.RStickYEvent, self.EVT_GPRStickY = wx.lib.newevent.NewEvent()

        self.target = frame

        for i in inputs.devices:
            print(i)

        self.sensetivity = .02
        self.RStickXValue = 0
        self.RStickYValue = 0
        thread = threading.Thread(target=self.ListenForInputs)
        thread.start()

    #Method to map raw inputs to more useful values
    #Raw inputs from analog sticks seem to range from 2^14 to -2^14
    #A small dead zone placed in the center of the stick
    #Even smaller dead zone on the outside <-- could be bigger in the future
    #Displays numbers rounded to 2 decimal points
    def stickMap(self, minOut, maxOut, x):
        if x > 32000:
            x = 32000
        elif x < -32000:
            x = -32000
        elif x < 2000 and x > -2000:
            x = 0
        #return round( (x - minIn) * (maxOut - minOut) / (maxIn - minIn) + minOut, 2)
        return round( (x + 32000) * (maxOut - minOut) / (32000 + 32000) + minOut, 2)

    def ListenForInputs(self):
        while 1:
            #time.sleep(.01)
            events = inputs.get_gamepad()
            for evt in events:
                if (evt.code == 'BTN_SOUTH'):
                    #print(evt.state)
                    if (evt.state == 1):
                        wx.PostEvent(self.target, self.ButtonEvent(button = 'a'))
                elif (evt.code == 'BTN_EAST'):
                    if (evt.state == 1):
                        wx.PostEvent(self.target, self.ButtonEvent(button = 'b'))
                elif (evt.code == 'BTN_WEST'):
                    if (evt.state == 1):
                        wx.PostEvent(self.target, self.ButtonEvent(button = 'x'))
                elif (evt.code == 'BTN_NORTH'):
                    if (evt.state == 1):
                        wx.PostEvent(self.target, self.ButtonEvent(button = 'y'))
                elif evt.code == "ABS_RX":
                    if self.stickMap(-1, 1, evt.state) > self.RStickXValue + self.sensetivity or self.stickMap(-1, 1, evt.state) < self.RStickXValue - self.sensetivity:
                        self.RStickXValue = self.stickMap(-1, 1, evt.state)
                        wx.PostEvent(self.target, self.RStickXEvent(x = self.RStickXValue))
                elif evt.code == "ABS_RY":
                    if self.stickMap(-1, 1, evt.state) > self.RStickYValue + self.sensetivity or self.stickMap(-1, 1, evt.state) < self.RStickYValue - self.sensetivity:
                        self.RStickYValue = self.stickMap(-1, 1, evt.state)
                        wx.PostEvent(self.target, self.RStickYEvent(y = self.RStickYValue))


#gp = GamePadEvent(2)
#while 1:
    #print(" ")