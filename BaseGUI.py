import wx

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
        self.CreateStatusBar()

        #####Create all subs
        """self.splitter = wx.SplitterWindow(self, pos=(10,10) ,size=(780, 430))

        self.panel1 = wx.Panel(self.splitter)
        self.panel2 = wx.Panel(self.splitter)"""

        #Initialize the frames Box Sizer, this component allows panels to be added (with BoxSizer.Add())
        self.frame_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.panel1 = wx.Panel(self)
        self.frame_sizer.Add(self.panel1, 1, wx.EXPAND | wx.ALL, 5)# the second parameter is like a ratio how how much screen should be taken up
        
        self.camera_panel = wx.Panel(self)
        self.frame_sizer.Add(self.camera_panel, 2, wx.EXPAND | wx.TOP | wx.BOTTOM, 5)

        self.panel2 = wx.Panel(self)
        self.frame_sizer.Add(self.panel2, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(self.frame_sizer)

        #Configure those subs
        #self.__do_layout()
        self.panel1.SetBackgroundColour(wx.Colour(255,0,0))
        self.panel2.SetBackgroundColour(wx.Colour(0,255,0))
        self.camera_panel.SetBackgroundColour(wx.Colour(0, 50, 200))

        #Move the frame to the center of the screen, could also use self.Move(x, y) to move window
        self.Center()

        

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