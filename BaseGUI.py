import wx

from Panels.CameraPanel import CameraPanel
from Panels.ButtonPanel import ButtonPanel
from Panels.SensorPanel import SensorPanel
from Panels.MapPanel import MapPanel

from ConnectionWindow import ConnectionWindow

import MPembed1 as mp
from GamePadEvents import GamePadEvents


class MyFrame(wx.Frame):

    def __init__(self):

        ####call the super constructor and initialize with no parent and title parameter
        wx.Frame.__init__(self, None, -1, "Base Station", size=(1200,700))#(800,450))

        ####Set the background color of the frame, rgb(22,149,229) is a cool blue I found on the robotics website
        self.SetBackgroundColour(wx.Colour(22, 149, 229, 255))

        ###Set the little icon at the top of the window, current icon also stolen from the robotics website
        icon = wx.Icon("R/UAAIceBerg.png", wx.BITMAP_TYPE_PNG)
        self.SetIcon(icon)

        ###Create the status bar at the bottom
        status_bar = self.CreateStatusBar()
        status_bar.SetBackgroundColour(wx.Colour(30, 180, 230))

        ###Create Menu Bar
        self.createMenubar()

        ##### Create All Panels #####

        self.camera_panel = CameraPanel(self)
        self.button_panel = ButtonPanel(self)
        self.sensor_panel = SensorPanel(self)
        self.status_panel = wx.Panel(self)
        self.map_panel = MapPanel(self)

        self.connection_window = ConnectionWindow()

        ##### Create Sizers for Panels #####

        ###Initialize the frames Box Sizer, this component allows panels to be added (with BoxSizer.Add())
        self.frame_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.frame_sizer.Add(self.camera_panel, 2, wx.EXPAND | wx.ALL, 5)
        self.frame_sizer.Add(self.sensor_panel, 1, wx.EXPAND | wx.TOP | wx.BOTTOM | wx.RIGHT, 5)# the second parameter is like a ratio how how much screen should be taken up
        #self.frame_sizer.Add(self.sensor_panel, 1, wx.EXPAND | wx.TOP | wx.BOTTOM | wx.RIGHT, 5)

        self.map_sizer = wx.BoxSizer(wx.VERTICAL)
        self.map_sizer.Add(self.map_panel, 1, wx.EXPAND)
        self.map_sizer.Add(0, 5, 0)
        self.map_sizer.Add(self.button_panel, 1, wx.EXPAND)
        self.frame_sizer.Add(self.map_sizer, 1, wx.EXPAND | wx.TOP | wx.BOTTOM | wx.RIGHT, 5)

        self.frame_vsizer = wx.BoxSizer(wx.VERTICAL)
        self.frame_vsizer.Add(self.frame_sizer, 3, wx.EXPAND)
        self.frame_vsizer.Add(self.status_panel, 1, wx.EXPAND  | wx.LEFT |  wx.RIGHT, 5)

        self.SetSizer(self.frame_vsizer)

        ###Configure Those Sub-Panels
        self.button_panel.SetBackgroundColour(wx.Colour(51, 102, 204))
        self.sensor_panel.SetBackgroundColour(wx.Colour(51, 102, 204))
        self.status_panel.SetBackgroundColour(wx.Colour(51, 102, 204))

        ###Move the frame to the center of the screen, could also use self.Move(x, y) to move window
        self.Center()

        ##### Frame Bindings #####

        ###Bind functions to the X button for properly closing the frame
        self.Bind(wx.EVT_CLOSE, self.OnClose)

        ###Input Binding
        self.gpe = GamePadEvents(self)
        self.Bind(self.gpe.EVT_GPButton, self.OnXBoxButton)
        self.Bind(self.gpe.EVT_GPRStickX, self.OnXBoxRStickX)
        self.Bind(self.gpe.EVT_GPRStickY, self.OnXBoxRStickY)
        self.Bind(self.gpe.EVT_GPLTrigger, self.OnXBoxLTrigger)
        self.Bind(self.gpe.EVT_GPRTrigger, self.OnXBoxRTrigger)

    
    def createMenubar(self):
        #Create a Connection Menu
        connection_menu = wx.Menu()
        connectionItem = connection_menu.Append(-1, "Connection\tc", "Connect to the rover")
        self.Bind(wx.EVT_MENU, self.onConnection, connectionItem)

        #Create a Camera Menu for the menu bar
        camera_menu = wx.Menu()
        #Create Items that will go in the camera menu (Supports 1-5 keyboard controls)
        camera1Item = camera_menu.Append(1, "Camera 1\t1", "Switch Camera View to #1")
        camera2Item = camera_menu.Append(2, "Camera 2\t2", "Switch Camera View to #2")
        camera3Item = camera_menu.Append(3, "Camera 3\t3", "Switch Camera View to #3")
        camera4Item = camera_menu.Append(4, "Camera 4\t4", "Switch Camera View to #4")
        camera5Item = camera_menu.Append(5, "Camera 5\t5", "Switch Camera View to #5")
        #Bind each Camera Menu Item to its own function
        self.Bind(wx.EVT_MENU, self.OnCamera1, camera1Item)
        self.Bind(wx.EVT_MENU, self.OnCamera2, camera2Item)
        self.Bind(wx.EVT_MENU, self.OnCamera3, camera3Item)
        self.Bind(wx.EVT_MENU, self.OnCamera4, camera4Item)
        self.Bind(wx.EVT_MENU, self.OnCamera5, camera5Item)
        #Alternatively just bind everything to one OnCamera() and pass cameraItem to tell what was selected

        #Place for future map
        map_menu = wx.Menu()

        #Create the Menu Bar to hold each Menu
        menu_bar = wx.MenuBar()
        #Add each Menu to the Menu Bar
        menu_bar.Append(connection_menu, "&Connection")
        menu_bar.Append(camera_menu, "&Camera")
        menu_bar.Append(map_menu, "&Map")

        #Set the Menu Bar to the frame for display
        self.SetMenuBar(menu_bar)

        self.Bind(wx.EVT_JOYSTICK_EVENTS, self.onJoyEvent)

    def onJoyEvent(self, event):
        print("Joystick event")

    #Placeholder Functions that are activated by the Menu Items
    def onConnection(self, event):
        print("Connecting to the rover...")
        self.connection_window.Show()

    def OnCamera1(self, event):
        print("You have swtiched to Camera #1")
        self.camera_panel.StartPlayer(["udp://239.0.0.20:8080"])
        #self.camera_panel.StartPlayer("R\\LuckyStarOp.mp4")
    
    def OnCamera2(self, event):
        print("You have swtiched to Camera #2")
        self.camera_panel.StartPlayer("R\\video.mov")
    
    def OnCamera3(self, event):
        print("You have swtiched to Camera #3")

    def OnCamera4(self, event):
        print("You have swtiched to Camera #4")

    def OnCamera5(self, event):
        print("You have swtiched to Camera #5")

    ###XBOX TEST: Bind A button to this function
    def OnXBoxButton(self, event):
        if (event.button == 'a'):
            print("a was pressed")
        elif (event.button == 'b'):
            print ("b was pressed")
        elif (event.button == 'x'):
            print ("x was pressed")
            #self.camera_panel.StartPlayer(["udp://192.168.1.129:8080"])
        elif (event.button == 'y'):
            print ("y was pressed")
            #self.camera_panel.StartPlayer("R\\video.mov")
    
    def OnXBoxRStickX(self, event):
        print("X: " + str(event.x))
    
    def OnXBoxRStickY(self, event):
        print("Y: " + str(event.y))
    
    def OnXBoxLTrigger(self, event):
        print("LT: " + str(event.value))

    def OnXBoxRTrigger(self, event):
        print("RT: " + str(event.value))

    ### Run when frame is closed
    def OnClose(self, event):
        self.gpe.StopListening()
        self.Destroy()

#def onButtonDown(evt):
#    print("a button was pressed")
#Necessary for all wxPyhton Apps
app = wx.App()

#Instantiate the class that is the main frame, the contructor will call Show() so that it appears when run
frame = MyFrame()
frame.Show()

app.MainLoop()