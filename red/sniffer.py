import nfqueue

q = None
seq = 0

def cb(dummy, payload):
    #callback
    data = payload.get_data()

    print '--------'
    print data
    print '--------'
    
    filename = 'message_' + seq + '.txt'
    seq = seq + 1
    f = open(filename, 'w')
    for x in data:
        f.write(x)
        print x
    f.close()




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
