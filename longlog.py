import os
from datetime import datetime 
from datetime import date
import time

def devices_connected():
	os.system("adb devices>deviceslist.txt")
	device_ls = open("deviceslist.txt","r")
	deviceList = device_ls.readlines()
	device_ls.close()
	os.system("rm deviceslist.txt")
	global deviceDSN
	deviceDSN = []
	for device in deviceList:
		deviceDSN.append(device.split('\t')[0])
	del deviceDSN[0] # list of devices attached element
	del deviceDSN[-1] # last \n element
	print(deviceDSN)

def long_logs_connected():
	devices_connected()
	if(len(deviceDSN)==0):
		print ("No devices attached")
	elif (len(deviceDSN)==1):
		take_long_logs(0)
	elif (len(deviceDSN)>1):
		print("You have connected some devices.Pls select the one to take long logs..")
		for x in range(0,len(deviceDSN)):
			print(deviceDSN[x]+"     "+str(x+1))
		usersel="wrong"
		while usersel not in range(0,len(deviceDSN)):	
			usersel=int(input("Enter the selection :"))-1
		take_long_logs(usersel)
	
def get_filename(i):
	os.system("adb -s "+deviceDSN[i]+" shell getprop ro.product.device>devicename.txt")
	deviceName = open("devicename.txt","r")
	device_name = deviceName.readlines()
	deviceName.close()
	os.system("rm devicename.txt")
	#print(deviceDSN[i])
	now = datetime.now()
	current_time = now.strftime("%H%M%S")
	today = date.today()
	date_today=today.strftime("%b%d")
	filename=device_name[0][:-1]+"_"+deviceDSN[i]+"_"+date_today+"_"+current_time
	return filename


def take_long_logs(i):
	file_name=get_filename(i)
	print(file_name)
	os.system("adb -s "+deviceDSN[i]+" logcat -v long threadtime>long_"+file_name+".txt")


long_logs_connected()
