import wx

class SensorPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.SetForegroundColour(wx.Colour(255, 255, 255))
        self.font = wx.Font()
        self.font.SetPointSize(50)
        self.font.Scale(2)
        self.SetFont(self.Font)

        self.title = wx.StaticText(self, label="Sensor Data:")
        self.sensor_1 = wx.StaticText(self, label="Sensor 1: xx.xxx")
        self.sensor_2 = wx.StaticText(self, label="Sensor 2: xx.xxx")
        self.sensor_3 = wx.StaticText(self, label="Sensor 3: xx.xxx")
        self.sensor_4 = wx.StaticText(self, label="Sensor 4: [xx, yy]")
        self.sensor_5 = wx.StaticText(self, label="Sensor 5: true")

        self.main_box_sizer = wx.BoxSizer(wx.VERTICAL)
        self.main_box_sizer.Add(self.title, 1, wx.EXPAND)
        self.main_box_sizer.Add(self.sensor_1, 1, wx.EXPAND)
        self.main_box_sizer.Add(self.sensor_2, 1, wx.EXPAND)
        self.main_box_sizer.Add(self.sensor_3, 1, wx.EXPAND)
        self.main_box_sizer.Add(self.sensor_4, 1, wx.EXPAND)
        self.main_box_sizer.Add(self.sensor_5, 1, wx.EXPAND)

        self.SetSizer(self.main_box_sizer)