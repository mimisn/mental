from mental.util.message.api import  MessageService
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer


class MessageServiceHandler:
    def sendMobileMessage(self, mobile, message):
        print("sendMolbileMessage")
        return True

    def sendEmailMessage(self, email, message):



        print("senEmailMessage %s" % email)
        return  True


if __name__ == '__main__':
    handler = MessageServiceHandler()
    processor = MessageService.Processor(handler)
    transport = TSocket.TServerSocket('127.0.0.1', 9090)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TServer.TThreadPoolServer(processor, transport, tfactory, pfactory)
    print("server start")
    server.serve()
    print("server exit")
