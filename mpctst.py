import wx
from MPembed import MPembed

mfiles=['tst.avi','Funkorama.oga']#replace with your own files
msel=0

class Frame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self,None,-1,'MPembed Test')
		self.mppan=wx.Panel(self)
		self.Bind(wx.EVT_MAXIMIZE, self.on_max)
		self.Bind(wx.EVT_WINDOW_DESTROY, self.on_destroy)
		wid=self.mppan.GetHandle()
		if wid!=0: self.mpc=MPembed(wid)
		self.Show()
	def on_max(self, evt):
		global msel,mfiles
		msel=(msel+1)%len(mfiles)
		self.mpc.load(mfiles[msel])
	def on_destroy(self, evt):
		del self.mpc		

if __name__ == '__main__':
	app = wx.App()
	frame = Frame()
	app.MainLoop()
