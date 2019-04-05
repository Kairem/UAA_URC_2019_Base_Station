import wx

class ButtonPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.SetForegroundColour(wx.Colour(255,255,255))
        
        self.clicks = 0
        self.text = wx.StaticText(self, label="Static Text Test\nButton Clicks: " + str(self.clicks))

        self.button = wx.Button(self, wx.ID_ANY, "Test")

        self.button_sizer = wx.BoxSizer(wx.VERTICAL)
        self.button_sizer.Add(self.button, 1)
        self.button_sizer.Add(self.text, 9)

        self.SetSizer(self.button_sizer)

        self.button.Bind(wx.EVT_BUTTON, self.onClicked)

    def onClicked(self, event):
        print("clicked")
        self.clicks += 1
        self.text.SetLabel("Static Text Test\nButton Clicks: " + str(self.clicks))