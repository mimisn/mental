import sys
from thrift.TMultiplexedProcessor import TMultiplexedProcessor
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
from thrift.transport import TTransport, TSocket


import subprocess
from Monitor.api.ttypes import hostInfoData
from Monitor.api import assetManagement

class assetManagementHandler:
    def getHostInfo(self):
        hosinfodata = hostInfoData()
        ip = subprocess.Popen(" ip a | grep inet | awk -F \" \" '{print $2}' | awk -F \"/\" '{print $1}'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).stdout.read().split("\n")
        hostname = subprocess.Popen("hostname", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).stdout.read()
        os_type = subprocess.Popen("hostname", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).stdout.read()


        return hosinfodata