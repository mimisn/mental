import sys

sys.path.append('./gen-py')


from uploadFile.api import FileInfoExtractService
from uploadFile.api.ttypes import *
from uploadFile.api.constants import *
import logging


from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TJSONProtocol

try:

    logging.basicConfig(filename='app.log', level=logging.INFO,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(message)s', datefmt='%Y-%m-%d')
    logging.info('test info')
    filedata = FileData()


    path = "E:\\BaiduNetdiskDownload\\视频\\下载必看.txt"
    filedata.name = "下载必看.txt"





    # Make socket
    transport = TSocket.TSocket('127.0.0.1', '9090')

    # Buffering is critical. Raw sockets are very slow
    transport = TTransport.TFramedTransport(transport)

    # Wrap in a protocol
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    #protocol =TJSONProtocol.TJSONProtocol(transport)
    # Create a client to use the protocol encoder
    client = FileInfoExtractService.Client(protocol)

    # Connect!
    transport.open()
    with open(path,'rb') as fp:
        while  True:
            block = fp.read(1024*1)
            if not block:
                break
            filedata.buff = block
            client.uploadFile(filedata)
            filedata.buff = ''
    # client.uploadFile(filedata)
    # filedata.buff = '55555555'.encode(encoding="utf-8")
    # client.uploadFile(filedata)
    transport.close()

except Thrift.TException as tx:
    print( "%s" % tx.message)