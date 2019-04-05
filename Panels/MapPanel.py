import wx

class MapPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.SetBackgroundColour(wx.Colour(140))
        self.mapLocation = "R\\PMD2Map.jpg" #image for testing

        self.enteredWindow = False

        '''self.map = wx.Image(self.mapLocation, wx.BITMAP_TYPE_ANY)
        self.map = self.map.Scale(291, 200)
        wx.StaticBitmap(self, -1, wx.BitmapFromImage(self.map))'''
        #self.draggable = wx.GenericDragImage(wx.BitmapFromImage(map))
        #self.draggable.Show()


        ##### Event Bindings #####
        self.Bind(wx.EVT_ENTER_WINDOW, self.OnEnter)
        self.Bind(wx.EVT_LEAVE_WINDOW, self.OnExit)
        self.Bind(wx.EVT_LEFT_DOWN, self.OnLeftDown)
    
    def OnEnter(self, e):
        self.enteredWindow = True
        print("inside")

    def OnExit(self, e):
        self.enteredWindow = False
        print("out")

    def OnLeftDown(self, e):
        #Prints mouse position relative to corner of panel in px (ex. 1 - 288 Xpos)
        print("X: " + str(e.x) + " Y: " + str(e.y))
        print(self.GetSize().x)