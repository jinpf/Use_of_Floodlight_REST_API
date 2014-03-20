#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: jinpf
# @Date:   2014-02-26 23:59:04
# @Last Modified by:   jinpf
# @Last Modified time: 2014-03-06 23:59:39

import requests

def Print_all(value,slen=0):
	'''
	print all values in mixed structure, slen stands for 
	how many backspace in front of the output
	'''
	if type(value)==dict:
		for i in value:
			print slen*'    ',i,':',
			temp=value[i]
			if type(temp)==dict:
				print
			Print_all(temp,slen+1)
	elif type(value)==list:
		print
		print slen*'    ','['
		for i in value:
			# print '    '
			if type(i) in(dict,list):
				Print_all(i,slen+1)
			else:
				print slen*'    '+' ',i
		print slen*'    ',']'
	else:
		print value

def Swich_feature():
	r = requests.get('http://127.0.0.1:8080/wm/core/controller/switches/json')
	status = r.json()
	print 25*'#'
	print 'Working Swiches feature:'
	for i,_switch in enumerate(status):
		print '***swich',i+1,'***'
		Print_all(status[i])
		print

def Controller_summary():
	r = requests.get('http://127.0.0.1:8080/wm/core/controller/summary/json')
	status = r.json()
	print 25*'#'
	print 'Controller summary:'
	Print_all(status)
	print

def Controller_memory():
	r = requests.get('http://127.0.0.1:8080/wm/core/memory/json')
	status = r.json()
	print 25*'#'
	print 'Controller memory condition:'
	Print_all(status)
	print

def Devices_linked():
	r = requests.get('http://127.0.0.1:8080/wm/device/')
	status = r.json()
	print 25*'#'
	print 'active devices:'
	for i,_device in enumerate(status):
		print '***device',i+1,'***'
		Print_all(status[i])
		print

def Show_static_flow(Swich_ID="all"):
	'''
	Swich_ID: Valid Switch DPID (XX:XX:XX:XX:XX:XX:XX:XX) or "all"
	'''
	r = requests.get('http://127.0.0.1:8080/wm/staticflowentrypusher/list/'+Swich_ID+'/json')
	status = r.json()
	print 25*'#'
	print 'swich static flow:'
	Print_all(status)
	print
	# for i,_switch in enumerate(status):
	# 	print '***swich',i+1,'***'
	# 	Print_all(status[i])
	#  	print


def Traffic_counter(counterTitle="all"):
	'''
	"all" or something of the form <DPID>_<COUNTER_NAME>_<SUB_CATEGORY>
	ie. 00:00:00:00:00:00:00:01_OFPacketIn_broadcast (SUB_CATEGORY being "broadcast")
	00:00:00:00:00:00:00:01_OFPacketIn_L3_ARP (SUB_CATEGORY being "L3_ARP")
	L3 sub_categories take the form "L3_<ether-type>", L4 sub_categories take the form "L4_<protocol>"
	For more details look at net.floodlightcontroller.counter.CounterStore.java 
	'''
	try:
		r = requests.get('http://127.0.0.1:8080/wm/core/counter/'+counterTitle+'/json')
		status = r.json()
		print 25*'#'
		print 'Controller traffic counter:'
		Print_all(status)
		print
	except Exception, e:
		print e


if __name__ == "__main__":
	# Devices_linked()
	# Swich_feature()
	# Controller_summary()
	# Controller_memory()
	# Traffic_counter()
	# Show_static_flow()
