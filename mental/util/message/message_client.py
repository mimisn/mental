import sys

sys.path.append('./gen-py')


from mental.util.message.api import MessageService
from mental.util.message.api.ttypes import *
from mental.util.message.api.constants import *
import logging


from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

try:

    logging.basicConfig(filename='app.log', level=logging.INFO,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(message)s', datefmt='%Y-%m-%d')
    logging.info('test info')



    # Make socket
    transport = TSocket.TSocket('127.0.0.1', '9090')

    # Buffering is critical. Raw sockets are very slow
    transport = TTransport.TBufferedTransport(transport)

    # Wrap in a protocol
    protocol = TBinaryProtocol.TBinaryProtocol(transport)

    # Create a client to use the protocol encoder
    client = MessageService.Client(protocol)

    # Connect!
    transport.open()

    client.sendEmailMessage("sss","1233")
    client.sendEmailMessage("12", "1233")
    client.getEmail()

    transport.close()

except Thrift.TException as tx:
    print ( "%s") % (tx.message)