"""
This class is used to create the events for each button
on the XBox Controller. On instantiation, a separate thread
will run and listen to the controller, posting events as
buttons are pressed.
"""

import wx.lib.newevent
import inputs
import threading
import time

class GamePadEvents:
    def __init__(self, frame):
        ##### Create the Events #####
        self.ButtonEvent, self.EVT_GPButton = wx.lib.newevent.NewEvent()
        self.DPadEvent, self.EVT_GPDPad = wx.lib.newevent.NewEvent()

        self.RStickEvent, self.EVT_GPRStick = wx.lib.newevent.NewEvent()
        self.LStickEvent, self.EVT_GPLStick = wx.lib.newevent.NewEvent()

        self.LTriggerEvent, self.EVT_GPLTrigger = wx.lib.newevent.NewEvent()
        self.RTriggerEvent, self.EVT_GPRTrigger = wx.lib.newevent.NewEvent()

        self.target = frame

        ### When set to false, the thread's loop will end
        self.isRunning = True

        for i in inputs.devices:
            print(i)

        self.sensetivity = .02
        self.RStickXValue = 0
        self.RStickYValue = 0

        self.LStickXValue = 0
        self.LStickYValue = 0
        
        ##### Start Thread #####
        self.thread = threading.Thread(target=self.ListenForInputs)
        self.thread.start()

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
    
    def triggerMap(self, minOut, maxOut, x):
        return round( (x - 0) * (maxOut - minOut) / (255 - 0) + minOut, 2)


    def ListenForInputs(self):
        while 1:
            #time.sleep(.01)
            events = inputs.get_gamepad()
            for evt in events:

                ### A, B, X, Y BUTTONS ###
                if (evt.code == 'BTN_SOUTH'):
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

                ### D-PAD BUTTONS ###
                elif (evt.code == 'ABS_HAT0X'):
                    if (evt.state == 1):
                        wx.PostEvent(self.target, self.DPadEvent(direction = 'right'))
                    elif (evt.state == -1):
                        wx.PostEvent(self.target, self.DPadEvent(direction = 'left'))
                elif (evt.code == 'ABS_HAT0Y'):
                    if (evt.state == 1):
                        wx.PostEvent(self.target, self.DPadEvent(direction = 'down'))
                    elif (evt.state == -1):
                        wx.PostEvent(self.target, self.DPadEvent(direction = 'up'))

                ### RIGHT STICK ###
                elif evt.code == "ABS_RX":
                    if self.stickMap(-1, 1, evt.state) > self.RStickXValue + self.sensetivity or self.stickMap(-1, 1, evt.state) < self.RStickXValue - self.sensetivity:
                        self.RStickXValue = self.stickMap(-1, 1, evt.state)
                        wx.PostEvent(self.target, self.RStickEvent(x = self.RStickXValue, y = self.RStickYValue))
                elif evt.code == "ABS_RY":
                    if self.stickMap(-1, 1, evt.state) > self.RStickYValue + self.sensetivity or self.stickMap(-1, 1, evt.state) < self.RStickYValue - self.sensetivity:
                        self.RStickYValue = self.stickMap(-1, 1, evt.state)
                        wx.PostEvent(self.target, self.RStickEvent(x = self.RStickXValue, y = self.RStickYValue))

                elif evt.code == "ABS_X":
                    if self.stickMap(-1, 1, evt.state) > self.LStickXValue + self.sensetivity or self.stickMap(-1, 1, evt.state) < self.LStickXValue - self.sensetivity:
                        self.LStickXValue = self.stickMap(-1, 1, evt.state)
                        wx.PostEvent(self.target, self.LStickEvent(x = self.LStickXValue, y = self.LStickYValue))
                elif evt.code == "ABS_Y":
                    if self.stickMap(-1, 1, evt.state) > self.LStickYValue + self.sensetivity or self.stickMap(-1, 1, evt.state) < self.LStickYValue - self.sensetivity:
                        self.LStickYValue = self.stickMap(-1, 1, evt.state)
                        wx.PostEvent(self.target, self.LStickEvent(x = self.LStickXValue, y = self.LStickYValue))

                ### TRIGGERS ###
                elif evt.code == "ABS_Z":
                    wx.PostEvent(self.target, self.LTriggerEvent(value = self.triggerMap(0, 1, evt.state)))
                elif evt.code == "ABS_RZ":
                    wx.PostEvent(self.target, self.RTriggerEvent(value = self.triggerMap(0, 1, evt.state)))

    def StopListening(self):
        self.isRunning = False

#gp = GamePadEvent(2)
#while 1:
    #print(" ")