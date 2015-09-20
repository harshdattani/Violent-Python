import optparse
from socket import *

parser = optparse.OptionParser()
parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
parser.add_option('-p', dest='tgtPort', type='int', help='specify target port')
(options, args) = parser.parse_args()
tgtHost = options.tgtHost
tgtPort = options.tgtPort

if (tgtHost == None) | (tgtPort == None):
    print parser.usage
    exit(0)

try:
    connSkt = socket(AF_INET, SOCK_STREAM)
    connSkt.connect((tgtHost, tgtPort))
    connSkt.send('ViolentPython\r\n')
    results = connSkt.recv(100)
    connSkt.close()
    print results
    print '[+]%d/tcp open'% tgtPort
except Exception, e:
    print '[-]%d/tcp closed'% tgtPort
