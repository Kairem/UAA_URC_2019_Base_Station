import wx
import MPembed as mp

class CameraPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=42)
        self.SetBackgroundColour(wx.Colour(255, 255, 255))

        #player = mp.MPembed(self)
