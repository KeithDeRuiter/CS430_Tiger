import nfqueue
#import mono
import socket
from dpkt import ip, tcp

q = None
seq = 0

def incrementSeq():
    global seq
    seq = seq + 1

def cb(dummy, payload):
    #callback

    data = payload.get_data()
    pkt = ip.IP(data)
    packetData = pkt.tcp.data


    #print '--------'
    #print data
    #print '--------'

    if len(packetData) > 0:
        print "Message received"
        filename = 'message_' + str(seq) + '.txt'
        incrementSeq()
        f = open(filename, 'w')
        f.write(packetData)
        print packetData
        f.close()
        print "Message written to file"

    payload.set_verdict(nfqueue.NF_ACCEPT)

    

q = nfqueue.queue()
q.open()
q.bind(socket.AF_INET)
q.set_callback(cb)
q.create_queue(0) 
try:
    q.try_run()
except KeyboardInterrupt:
    print "Exiting..." 
finally:    #Need to ensure that socket is unbound, even on interrupt
    q.unbind(socket.AF_INET)
    q.close()
    print "Unbound"

q.unbind(socket.AF_INET)
q.close()
