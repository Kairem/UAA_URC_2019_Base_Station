import wx
import MPembed1 as mp

class CameraPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=42)
        self.SetBackgroundColour(wx.Colour(0, 0, 0))

        self.whnd = self.GetHandle()
                
    def StartPlayer(self, videoPath):
        self.player = mp.MPembed(self.whnd, [videoPath])