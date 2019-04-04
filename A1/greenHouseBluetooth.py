import bluetooth
import subprocess as sp
import os

class PairedDevice:
	
	def paired():

		nearby_devices = bluetooth.discover_devices(lookup_names = True)
		p = sp.Popen(["bt-device", "--list"], stdin = sp.PIPE, stdout = sp.PIPE, close_fds = True)
		(stdout, stdin) = (p.stdout, p.stdin)

		paired_devices = stdout.readlines()
		print(paired_devices)

		if p == True:
			print ("Success")

	def main():
		pair = PairedDevice()
		pair.paired()

	if __name__ == "__main__":
		main()