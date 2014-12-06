from datetime import datetime
from threading import Timer

x=datetime.today()
y=x.replace(day=x.day, hour=x.hour, minute=x.minute, second=x.second+5, microsecond=0)
delta_t=y-x
secs=delta_t.seconds+1

def hello_world():
	print "hello world"
	x=datetime.today()
	print x
	
	t = Timer(secs, hello_world)
	t.start()

    #...

t = Timer(secs, hello_world)
print secs, type(secs)
t.start()