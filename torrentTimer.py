import os
import time
class torrentTimer(object):
	"""torrentTimer is a tiny tool that will kill your torrent client after a certain time period.
	It can also shut down your OS after force quitting your torrent *if you want*
	"""

	def __init__(self):
		"""Summary
		
		Args:
		    arg (TYPE): Description
		"""		
		print "Your torrentTimer has been initiated"

	def killWord(self,wait_time = 0):
		"""Find MS word process by name, and kill it instantly.
		
		Returns:
		    TYPE: Description
		"""
		print "Kill your MS word process in {} seconds.".format(wait_time)
		time.sleep(wait_time)
		os.system('taskkill /f /im winword.exe')
		print "Your word process has been killed!"
		

if __name__ == '__main__':
	timer = torrentTimer()
	timer.killWord(10)
