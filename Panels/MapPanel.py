import wx

class MapPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        ##### Class Variables #####
        
        self.robotGPSLat = 0
        self.robotGPSLon = 0

        ###Coords relative to map
        self.robotX = 50
        self.robotY = 50

        self.mapLocation = "R\\UtahMap.png" #image for testing
        self.enteredWindow = False
        self.mouseButtonDown = False

        self.mapScreenPosX = 100
        self.mapScreenPosY = 100

        self.mouseOffsetX = 0
        self.mouseOffsetY = 0

        ##### Set Up #####

        self.dc = wx.ClientDC(self)
        
        self.map = wx.Bitmap(self.mapLocation)
        self.dc.DrawBitmap(self.map, self.mapScreenPosX, self.mapScreenPosY)
        self.dc.SetBrush(wx.Brush(wx.Colour(0, 255,0)))
        self.dc.DrawCircle(50, 50, 5)

        self.SetBackgroundColour(wx.Colour(0))

        ##### Event Bindings #####
        self.Bind(wx.EVT_ENTER_WINDOW, self.OnEnter)
        self.Bind(wx.EVT_LEAVE_WINDOW, self.OnExit)
        self.Bind(wx.EVT_LEFT_DOWN, self.OnLeftDown)
        self.Bind(wx.EVT_LEFT_UP, self.OnLeftUp)
        self.Bind(wx.EVT_MOTION, self.OnMotion)
    
    ##### Event Bindings #####

    def OnEnter(self, e):
        self.enteredWindow = True
        print("inside")

    def OnExit(self, e):
        self.enteredWindow = False
        print("out")

    def OnLeftUp(self, e):
        self.mouseButtonDown = False

    def OnLeftDown(self, e):
        self.mouseButtonDown = True
        #Prints mouse position relative to corner of panel in px (ex. 1 - 288 Xpos)
        print("X: " + str(e.x) + " Y: " + str(e.y))
        self.mouseOffsetX = e.x - self.mapScreenPosX
        self.mouseOffsetY = e.y - self.mapScreenPosY

    ##### Drawing the Maps #####
    def Draw(self):
        self.dc = wx.ClientDC(self)
        self.dc.Clear()
    
        #self.map = wx.Bitmap(self.mapLocation)
        self.dc.DrawBitmap(self.map, self.mapScreenPosX, self.mapScreenPosY)
        self.dc.SetBrush(wx.Brush(wx.Colour(0, 255,0)))
        self.dc.DrawCircle(self.mapScreenPosX + self.robotX, self.mapScreenPosY + self.robotY, 5)
    
    def OnMotion(self, e):
        if self.mouseButtonDown:
            self.mapScreenPosX = e.x - self.mouseOffsetX
            self.mapScreenPosY = e.y - self.mouseOffsetY

            self.Draw()
    
    ##### Map Panel Functions #####
    def updateRoverPosition(self, x, y):
        self.robotX = x
        self.robotY = y
        self.Draw()