import multiprocessing
import os
import time

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TJSONProtocol
from thrift.server import TServer
from uploadFile.api import FileInfoExtractService
def fun(args):
    for i in range(1):
        print('myname is : %s \n' %(args))
        time.sleep(1)

class uploadFileHandler:
    def uploadFile(self, filedata):
        for i in range(4):
            t = multiprocessing.Process(target=fun, args=("name %s" % (i),))
            t.start()
        print(filedata.name)
        if os.path.exists(filedata.name):
            with open(filedata.name, 'ab+') as fp:
                fp.write(filedata.buff)
        else:
            with open(filedata.name, 'ab+') as fp:
                fp.write(filedata.buff)
        print("buff size is %s\n" %len(filedata.buff))
        return True

if __name__ == '__main__':
    handler = uploadFileHandler()
    processor = FileInfoExtractService.Processor(handler)
    transport = TSocket.TServerSocket('127.0.0.1', 9090)
    tfactory = TTransport.TFramedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()
    #pfactory = TJSONProtocol.TJSONProtocolFactory()
    #TJSONProtocol

    server = TServer.TThreadPoolServer(processor, transport, tfactory, pfactory)
    print("server start")
    server.serve()
    print("server exit")
