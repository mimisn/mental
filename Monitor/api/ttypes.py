#
# Autogenerated by Thrift Compiler (0.12.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TFrozenDict, TException, TApplicationException
from thrift.protocol.TProtocol import TProtocolException
from thrift.TRecursive import fix_spec

import sys

from thrift.transport import TTransport
all_structs = []


class RsyncType(object):
    rsync_ssh = 0
    rsync_dome = 1

    _VALUES_TO_NAMES = {
        0: "rsync_ssh",
        1: "rsync_dome",
    }

    _NAMES_TO_VALUES = {
        "rsync_ssh": 0,
        "rsync_dome": 1,
    }


class UploadFileData(object):
    """
    Attributes:
     - fileName
     - buff
     - fileDestPath
     - fileSize
     - fileMd5

    """


    def __init__(self, fileName=None, buff=None, fileDestPath="/tmp", fileSize=None, fileMd5=None,):
        self.fileName = fileName
        self.buff = buff
        self.fileDestPath = fileDestPath
        self.fileSize = fileSize
        self.fileMd5 = fileMd5

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.fileName = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.buff = iprot.readBinary()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.fileDestPath = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I64:
                    self.fileSize = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.fileMd5 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('UploadFileData')
        if self.fileName is not None:
            oprot.writeFieldBegin('fileName', TType.STRING, 1)
            oprot.writeString(self.fileName.encode('utf-8') if sys.version_info[0] == 2 else self.fileName)
            oprot.writeFieldEnd()
        if self.buff is not None:
            oprot.writeFieldBegin('buff', TType.STRING, 2)
            oprot.writeBinary(self.buff)
            oprot.writeFieldEnd()
        if self.fileDestPath is not None:
            oprot.writeFieldBegin('fileDestPath', TType.STRING, 3)
            oprot.writeString(self.fileDestPath.encode('utf-8') if sys.version_info[0] == 2 else self.fileDestPath)
            oprot.writeFieldEnd()
        if self.fileSize is not None:
            oprot.writeFieldBegin('fileSize', TType.I64, 4)
            oprot.writeI64(self.fileSize)
            oprot.writeFieldEnd()
        if self.fileMd5 is not None:
            oprot.writeFieldBegin('fileMd5', TType.STRING, 5)
            oprot.writeString(self.fileMd5.encode('utf-8') if sys.version_info[0] == 2 else self.fileMd5)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.fileName is None:
            raise TProtocolException(message='Required field fileName is unset!')
        if self.buff is None:
            raise TProtocolException(message='Required field buff is unset!')
        if self.fileDestPath is None:
            raise TProtocolException(message='Required field fileDestPath is unset!')
        if self.fileSize is None:
            raise TProtocolException(message='Required field fileSize is unset!')
        if self.fileMd5 is None:
            raise TProtocolException(message='Required field fileMd5 is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class RsyncDtata(object):
    """
    Attributes:
     - userName
     - ip
     - fileDestPath
     - fileStartPath
     - isRsyncMultiprocessing
     - rsyncType

    """


    def __init__(self, userName=None, ip=None, fileDestPath=None, fileStartPath=None, isRsyncMultiprocessing=False, rsyncType=1,):
        self.userName = userName
        self.ip = ip
        self.fileDestPath = fileDestPath
        self.fileStartPath = fileStartPath
        self.isRsyncMultiprocessing = isRsyncMultiprocessing
        self.rsyncType = rsyncType

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.userName = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.ip = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.fileDestPath = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.fileStartPath = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.BOOL:
                    self.isRsyncMultiprocessing = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I32:
                    self.rsyncType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('RsyncDtata')
        if self.userName is not None:
            oprot.writeFieldBegin('userName', TType.STRING, 1)
            oprot.writeString(self.userName.encode('utf-8') if sys.version_info[0] == 2 else self.userName)
            oprot.writeFieldEnd()
        if self.ip is not None:
            oprot.writeFieldBegin('ip', TType.STRING, 2)
            oprot.writeString(self.ip.encode('utf-8') if sys.version_info[0] == 2 else self.ip)
            oprot.writeFieldEnd()
        if self.fileDestPath is not None:
            oprot.writeFieldBegin('fileDestPath', TType.STRING, 3)
            oprot.writeString(self.fileDestPath.encode('utf-8') if sys.version_info[0] == 2 else self.fileDestPath)
            oprot.writeFieldEnd()
        if self.fileStartPath is not None:
            oprot.writeFieldBegin('fileStartPath', TType.STRING, 4)
            oprot.writeString(self.fileStartPath.encode('utf-8') if sys.version_info[0] == 2 else self.fileStartPath)
            oprot.writeFieldEnd()
        if self.isRsyncMultiprocessing is not None:
            oprot.writeFieldBegin('isRsyncMultiprocessing', TType.BOOL, 5)
            oprot.writeBool(self.isRsyncMultiprocessing)
            oprot.writeFieldEnd()
        if self.rsyncType is not None:
            oprot.writeFieldBegin('rsyncType', TType.I32, 6)
            oprot.writeI32(self.rsyncType)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.isRsyncMultiprocessing is None:
            raise TProtocolException(message='Required field isRsyncMultiprocessing is unset!')
        if self.rsyncType is None:
            raise TProtocolException(message='Required field rsyncType is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class hostInfoData(object):
    """
    Attributes:
     - ip
     - port
     - hostname
     - os_type
     - os_version
     - mem_total
     - mem_swap
     - cpu_type
     - cpu_num
     - disk_info
     - kernel
     - status

    """


    def __init__(self, ip=None, port=None, hostname=None, os_type=None, os_version=None, mem_total=None, mem_swap=None, cpu_type=None, cpu_num=None, disk_info=None, kernel=None, status=None,):
        self.ip = ip
        self.port = port
        self.hostname = hostname
        self.os_type = os_type
        self.os_version = os_version
        self.mem_total = mem_total
        self.mem_swap = mem_swap
        self.cpu_type = cpu_type
        self.cpu_num = cpu_num
        self.disk_info = disk_info
        self.kernel = kernel
        self.status = status

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.ip = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.port = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.hostname = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.os_type = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.os_version = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.STRING:
                    self.mem_total = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.STRING:
                    self.mem_swap = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.STRING:
                    self.cpu_type = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 9:
                if ftype == TType.STRING:
                    self.cpu_num = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 10:
                if ftype == TType.STRING:
                    self.disk_info = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 11:
                if ftype == TType.STRING:
                    self.kernel = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 12:
                if ftype == TType.STRING:
                    self.status = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('hostInfoData')
        if self.ip is not None:
            oprot.writeFieldBegin('ip', TType.STRING, 1)
            oprot.writeString(self.ip.encode('utf-8') if sys.version_info[0] == 2 else self.ip)
            oprot.writeFieldEnd()
        if self.port is not None:
            oprot.writeFieldBegin('port', TType.STRING, 2)
            oprot.writeString(self.port.encode('utf-8') if sys.version_info[0] == 2 else self.port)
            oprot.writeFieldEnd()
        if self.hostname is not None:
            oprot.writeFieldBegin('hostname', TType.STRING, 3)
            oprot.writeString(self.hostname.encode('utf-8') if sys.version_info[0] == 2 else self.hostname)
            oprot.writeFieldEnd()
        if self.os_type is not None:
            oprot.writeFieldBegin('os_type', TType.STRING, 4)
            oprot.writeString(self.os_type.encode('utf-8') if sys.version_info[0] == 2 else self.os_type)
            oprot.writeFieldEnd()
        if self.os_version is not None:
            oprot.writeFieldBegin('os_version', TType.STRING, 5)
            oprot.writeString(self.os_version.encode('utf-8') if sys.version_info[0] == 2 else self.os_version)
            oprot.writeFieldEnd()
        if self.mem_total is not None:
            oprot.writeFieldBegin('mem_total', TType.STRING, 6)
            oprot.writeString(self.mem_total.encode('utf-8') if sys.version_info[0] == 2 else self.mem_total)
            oprot.writeFieldEnd()
        if self.mem_swap is not None:
            oprot.writeFieldBegin('mem_swap', TType.STRING, 7)
            oprot.writeString(self.mem_swap.encode('utf-8') if sys.version_info[0] == 2 else self.mem_swap)
            oprot.writeFieldEnd()
        if self.cpu_type is not None:
            oprot.writeFieldBegin('cpu_type', TType.STRING, 8)
            oprot.writeString(self.cpu_type.encode('utf-8') if sys.version_info[0] == 2 else self.cpu_type)
            oprot.writeFieldEnd()
        if self.cpu_num is not None:
            oprot.writeFieldBegin('cpu_num', TType.STRING, 9)
            oprot.writeString(self.cpu_num.encode('utf-8') if sys.version_info[0] == 2 else self.cpu_num)
            oprot.writeFieldEnd()
        if self.disk_info is not None:
            oprot.writeFieldBegin('disk_info', TType.STRING, 10)
            oprot.writeString(self.disk_info.encode('utf-8') if sys.version_info[0] == 2 else self.disk_info)
            oprot.writeFieldEnd()
        if self.kernel is not None:
            oprot.writeFieldBegin('kernel', TType.STRING, 11)
            oprot.writeString(self.kernel.encode('utf-8') if sys.version_info[0] == 2 else self.kernel)
            oprot.writeFieldEnd()
        if self.status is not None:
            oprot.writeFieldBegin('status', TType.STRING, 12)
            oprot.writeString(self.status.encode('utf-8') if sys.version_info[0] == 2 else self.status)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(UploadFileData)
UploadFileData.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'fileName', 'UTF8', None, ),  # 1
    (2, TType.STRING, 'buff', 'BINARY', None, ),  # 2
    (3, TType.STRING, 'fileDestPath', 'UTF8', "/tmp", ),  # 3
    (4, TType.I64, 'fileSize', None, None, ),  # 4
    (5, TType.STRING, 'fileMd5', 'UTF8', None, ),  # 5
)
all_structs.append(RsyncDtata)
RsyncDtata.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'userName', 'UTF8', None, ),  # 1
    (2, TType.STRING, 'ip', 'UTF8', None, ),  # 2
    (3, TType.STRING, 'fileDestPath', 'UTF8', None, ),  # 3
    (4, TType.STRING, 'fileStartPath', 'UTF8', None, ),  # 4
    (5, TType.BOOL, 'isRsyncMultiprocessing', None, False, ),  # 5
    (6, TType.I32, 'rsyncType', None, 1, ),  # 6
)
all_structs.append(hostInfoData)
hostInfoData.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'ip', 'UTF8', None, ),  # 1
    (2, TType.STRING, 'port', 'UTF8', None, ),  # 2
    (3, TType.STRING, 'hostname', 'UTF8', None, ),  # 3
    (4, TType.STRING, 'os_type', 'UTF8', None, ),  # 4
    (5, TType.STRING, 'os_version', 'UTF8', None, ),  # 5
    (6, TType.STRING, 'mem_total', 'UTF8', None, ),  # 6
    (7, TType.STRING, 'mem_swap', 'UTF8', None, ),  # 7
    (8, TType.STRING, 'cpu_type', 'UTF8', None, ),  # 8
    (9, TType.STRING, 'cpu_num', 'UTF8', None, ),  # 9
    (10, TType.STRING, 'disk_info', 'UTF8', None, ),  # 10
    (11, TType.STRING, 'kernel', 'UTF8', None, ),  # 11
    (12, TType.STRING, 'status', 'UTF8', None, ),  # 12
)
fix_spec(all_structs)
del all_structs
