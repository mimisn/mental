namespace java cn.xwtec.thrift.uploadFile
namespace py api

struct UploadFileData
{
    1:required string   fileName;
    2:required binary   buff;
    3:required string   fileDestPath = "/tmp";
    4:required i64      fileSize;
    5:required string   fileMd5;
}
enum RsyncType
{
    rsync_ssh = 0,
    rsync_dome = 1
}
struct RsyncDtata{
    1:optional  string userName;
    2:optional  string ip;
    3:optional  string fileDestPath;
    4:optional  string fileStartPath;
    5:required  bool  isRsyncMultiprocessing=false;
    6:required  RsyncType rsyncType=RsyncType.rsync_dome;
}

service UploadFileServer
{
    bool UploadFile(1:UploadFileData uploadFileData);
    void RsyncFile(1:RsyncDtata rsyncData);
    string getRsyncProgess();
}

struct hostInfoData
{
    1:string ip;
    2:string port;
    3:string hostname;
    4:string os_type;
    5:string os_version;
    6:string mem_total;
    7:string mem_swap;
    8:string cpu_type;
    9:string cpu_num;
    10:string disk_info;
    11:string kernel;
    12:string status;
}


service assetManagement
{
    hostInfoData getHostInfo();
}


#  d:\thrift-0.12.0.exe --gen py  -out D:/PycharmProjects/mental/mental/util/ D:/PycharmProjects/mental/mental/util/thrift/MessageService.thrift