import wx

class ConnectionWindow(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "Connection Settings")#, size=(800,450))
        self.SetBackgroundColour(wx.Colour(22, 149, 229, 255))
        self.SetForegroundColour(wx.Colour(255, 255, 255))

        self.status_bar = self.CreateStatusBar()
        self.status_bar.SetBackgroundColour(wx.Colour(30, 180, 230))

        self.instructions = wx.StaticText(self, label="Enter IP and port to connect")
        self.ip_input = wx.TextCtrl(self, size=(300, 20))

        self.frame_sizer = wx.BoxSizer(wx.VERTICAL)
        self.frame_sizer.Add(self.instructions, 1)
        self.frame_sizer.Add(self.ip_input, 1)
        self.SetSizer(self.frame_sizer)