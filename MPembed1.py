"""
	MPembed: simple mplayer wrapper for embedding
		MPembed(wid,opts) - constructor, starts mplayer instance in idle, embedded into window wid, options list opts
		~MPembed() - destructor, terminates mplayer instance
		load(fl) - start playing file fl
		unload() - stop playing
		pause() - pause/resume playing
		capture() - take screenshot, saved in file shotxxxx.png
		fullscreen() - toggle fullscreen
"""

import subprocess as sp

class MPembed():
	def __init__(self,wid,opts=[]):
		self.inst=sp.Popen(['C:\\mplayer\\MPlayer-x86_64-r38116+gf4cf6ba8c9\\mplayer.exe', "C:\\video.mov"])
	def __del__(self):
		self.inst.stdin.write('quit\n')
		self.inst.wait()
	def load(self,fl):
		self.inst.stdin.write('loadfile %s\n'%fl)
	def unload(self):
		self.inst.stdin.write('stop\n')
	def capture(self):
		self.inst.stdin.write('screenshot 0\n')
	def pause(self):
		self.inst.stdin.write('pause\n')
	def fullscreen(self):
		self.inst.stdin.write('vo_fullscreen\n')
