import nfqueue

q = None

def cb(dummy, payload):
    #callback
    print payload


q = nfqueue.queue()
q.open()
q.bind(socket.AF_INET)
q.set_callback(cb)
q.create_queue(0) 
try:
    q.try_run()
except KeyboardInterrupt:
    print "Exiting..." 

q.unbind(socket.AF_INET)
q.close()
