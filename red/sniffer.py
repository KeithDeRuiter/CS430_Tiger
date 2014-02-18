import nfqueue
import mono

q = None

def cb(dummy, payload):
    #callback
    # print payload
    pkt = IP(payload.get_data())
    pkt.ttl = 10
    del pkt.chksum
    payload_set_verdict_modified(nfqueue.NF_ACCEPT, str(pkt), len(pkt))
    print pkt
    
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