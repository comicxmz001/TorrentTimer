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

	def killBT(self,wait_time = 0):
		"""Find BT Client process by name, and kill it instantly.
		
		Returns:
		    TYPE: Description
		"""
		BT_CLIENT_PROCESS_NAME = "PROCESS_NAME_BT_CLIENT"
		print "Killing your BT_CLIENT_PROCESS_NAME process in {} seconds.".format(wait_time)
		time.sleep(wait_time)
		os.system('taskkill /f /im BT_CLIENT_PROCESS_NAME')
		print "Your BT_CLIENT_PROCESS_NAME process has been killed!"
		

if __name__ == '__main__':
	timer = torrentTimer()
	timer.killBT(10)
