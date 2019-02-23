import wx

thisthing = 5

class MyFrame(wx.Frame):

    #Constructor for the main frame of the application
    def __init__(self):

        #call the super constructor and initialize with no parent and title parameter
        wx.Frame.__init__(self, None, -1, "Base Station (First Attempt)", size=(800,450))

        #Set the background color of the frame, rgb(22,149,229) is a cool blue I found on the robotics website
        self.SetBackgroundColour(wx.Colour(22, 149, 229, 255))

        #Set the little icon at the top of the window, current icon also stolen from the robotics website
        icon = wx.Icon("R/UAAIceBerg.png", wx.BITMAP_TYPE_PNG)
        self.SetIcon(icon)

        #Create the status bar at the bottom
        status_bar = self.CreateStatusBar()
        status_bar.SetBackgroundColour(wx.Colour(30, 180, 230))

        #Create Menu Bar
        self.createMenubar()

        #####Create all subs
        """self.splitter = wx.SplitterWindow(self, pos=(10,10) ,size=(780, 430))

        self.panel1 = wx.Panel(self.splitter)
        self.panel2 = wx.Panel(self.splitter)"""

        #Initialize the frames Box Sizer, this component allows panels to be added (with BoxSizer.Add())
        self.frame_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.camera_panel = wx.Panel(self)
        self.frame_sizer.Add(self.camera_panel, 2, wx.EXPAND | wx.ALL, 5)

        self.panel1 = ButtonPanel(self)
        self.frame_sizer.Add(self.panel1, 1, wx.EXPAND | wx.ALL, 5)# the second parameter is like a ratio how how much screen should be taken up

        self.panel2 = wx.Panel(self)
        self.frame_sizer.Add(self.panel2, 1, wx.EXPAND | wx.ALL, 5)

        #self.SetSizer(self.frame_sizer)

        self.frame_vsizer = wx.BoxSizer(wx.VERTICAL)
        self.frame_vsizer.Add(self.frame_sizer, 3, wx.EXPAND)

        self.status_panel = wx.Panel(self)
        self.frame_vsizer.Add(self.status_panel, 1, wx.EXPAND | wx.BOTTOM | wx.LEFT | wx.RIGHT, 5)

        self.SetSizer(self.frame_vsizer)

        #Configure those subs
        #self.__do_layout()
        self.panel1.SetBackgroundColour(wx.Colour(255,0,0))
        self.panel2.SetBackgroundColour(wx.Colour(0,255,0))
        self.camera_panel.SetBackgroundColour(wx.Colour(0, 50, 200))
        self.status_panel.SetBackgroundColour(wx.Colour(255,255,255))

        #Move the frame to the center of the screen, could also use self.Move(x, y) to move window
        self.Center()
    
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
        #Alternatively just bind everything to one OnCamera() and pass cameraItem to tell what was selecteced

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

    #Placeholder Functions that are acticated by the Menu Items
    def onConnection(self, event):
        print("Connecting to the rover...")

    def OnCamera1(self, event):
        print("You have swtiched to Camera #1")
    
    def OnCamera2(self, event):
        print("You have swtiched to Camera #2")
    
    def OnCamera3(self, event):
        print("You have swtiched to Camera #3")

    def OnCamera4(self, event):
        print("You have swtiched to Camera #4")

    def OnCamera5(self, event):
        print("You have swtiched to Camera #5")

class ButtonPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        self.button = wx.Button(self, wx.ID_ANY, "test button")

        self.button_sizer = wx.BoxSizer()
        self.button_sizer.Add(self.button, 1)

        self.SetSizer(self.button_sizer)

        self.button.Bind(wx.EVT_BUTTON, self.onClicked)

    def onClicked(self, event):
        print("clicked")

    """def __do_layout(self):
        frame_sizer = wx.BoxSizer(wx.VERTICAL)
        frame_sizer.Add(self.splitter, 1, wx.ALL, 10)
        self.SetSizer(frame_sizer)
        frame_sizer.Fit(self)
        self.splitter.SplitVertically(self.panel1, self.panel2, 0)"""
#Necessary for all wxPyhton Apps
app = wx.App()

#Instantiate the class that is the main frame, the contructor will call Show() so that it appears when run
frame = MyFrame()
frame.Show()

app.MainLoop()