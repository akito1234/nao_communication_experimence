import sys,signal,time
def myfunc(signum, stack):
	print 'SIGALRM!'
	sys.exit()
signal.signal(signal.SIGALRM, myfunc)
signal.alarm(5)
while 1:
	print '.'
	time.sleep(1)