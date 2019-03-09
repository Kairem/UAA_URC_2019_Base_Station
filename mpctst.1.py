import wx
from MPembed import MPembed

mfiles=[b'C:\\Users\\eiver\\Documents\\IcebergBaseStation\\R\\video.mov']#replace with your own files
msel=0

import subprocess as sp

class MPembed():
	def __init__(self,wid,opts=[]):
		self.inst=sp.Popen([b'C:\\mplayer\\MPlayer-x86_64-r38116+gf4cf6ba8c9\\mplayer.exe',b'-slave',b'-wid',b'%d'%wid,b'-vf',b'screenshot',b'-idle'] +opts,stdin=sp.PIPE)
	def __del__(self):
		self.inst.stdin.write(b'quit\n')
		self.inst.wait()
	def load(self,fl):
		self.inst.stdin.write(b'loadfile %s\n'%fl)
	def unload(self):
		self.inst.stdin.write(b'stop\n')
	def capture(self):
		self.inst.stdin.write(b'screenshot 0\n')
	def pause(self):
		self.inst.stdin.write(b'pause\n')
	def fullscreen(self):
		self.inst.stdin.write(b'vo_fullscreen\n')

class Frame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self,None,-1,'MPembed Test')
		self.mppan=wx.Panel(self)
		#self.Bind(wx.EVT_MAXIMIZE, self.on_max)
		self.Bind(wx.EVT_WINDOW_CREATE, self.on_create)
		self.Bind(wx.EVT_WINDOW_DESTROY, self.on_destroy)
		self.Show()
	def on_create(self, evt):
		global msel,mfiles
		msel=(msel+1)%len(mfiles)

		wid=self.mppan.GetHandle()
		if wid!=0: self.mpc=MPembed(wid)

		self.mpc.load(mfiles[msel])
	def on_destroy(self, evt):
		del self.mpc

if __name__ == '__main__':
	app = wx.App()
	frame = Frame()
	app.MainLoop()
