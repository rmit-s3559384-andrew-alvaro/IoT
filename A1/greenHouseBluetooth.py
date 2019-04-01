import bluetooth
import subprocess as sp
import os

nearby_devices = bluetooth.discover_devices(lookup_names = True)
#print("Paired devices found " %len(nearby_devices))
#print("Found %d devices" % len(nearby_devices))

#for addr in nearby_devices:
#	print("%s - '%s'" % 
p = sp.Popen(["bt-device", "--list"], stdin = sp.PIPE, stdout = sp.PIPE, close_fds = True)
(stdout, stdin) = (p.stdout, p.stdin)

paired_devices = stdout.readlines()
print(paired_devices)

if p == True:
	print ("Success")

