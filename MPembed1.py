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

class MPembed():#'{} {}'.format("-wid", str(wid))
	def __init__(self,wid,opts=[]):
		#self.inst = sp.Popen(['C:\\mplayer\\MPlayer-x86_64-r38116+gf4cf6ba8c9\\mplayer.exe', "R\\LuckyStarOp.mp4", "-slave", "-wid", str(wid)], stdin=sp.PIPE, universal_newlines=True)
		self.inst = sp.Popen(['C:\\mplayer\\MPlayer-x86_64-r38116+gf4cf6ba8c9\\mplayer.exe', "-slave", "-wid", str(wid)] +opts, stdin=sp.PIPE, universal_newlines=True)
	def __del__(self):
		#self.inst.stdin.write('quit\n')
		self.inst.communicate('quit\n')
		self.inst.wait()
	def load(self,fl):
		self.inst.communicate('loadfile %s\n'%fl)
	def unload(self):
		self.inst.communicate('stop\n')#it works!
	def capture(self):
		self.inst.communicate('screenshot 0\n')
	def pause(self):
		self.inst.communicate('pause\n')
	def fullscreen(self):
		self.inst.communicate('vo_fullscreen\n')