import nfqueue
import mono
from dpkt import ip, tcp

q = None
seq = 0

def cb(dummy, payload):
    #callback

    data = payload.get_data()
    pkt = ip.IP(data)
    packetData = pkt.tcp.data


    #print '--------'
    #print data
    #print '--------'

    if len(packetData) > 0:
        filename = 'message_' + str(seq) + '.txt'
        seq = seq + 1
        f = open(filename, 'w')
        f.write(packetData)
        print packetData
        f.close()

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

q.unbind(socket.AF_INET)
q.close()
