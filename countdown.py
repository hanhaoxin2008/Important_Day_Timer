"""
计时器模块
"""

from Timec import  *
from cjson import  *
from threading import Thread
class countdown:
    """
    计时器类
    """
    def __init__(self,id,title,type,start=None,end=None):
        """
        初始化计时器

        :param id: 计时器id，程序自动生成
        :param title: 计时器标题
        :param type: 计时器类型，1：正计时，2：倒计时
        :param start: 开始时间，格式：0000-00-00 00:00:00
        :param end: 结束时间，格式：0000-00-00 00:00:00

        """
        self.id=id
        self.type=type
        self.title=title
        self.start_time=start
        self.end_time=end
        self.state=0
    def Refresh(self):
        """
        刷新计时器
        """
        if self.type==1:
            cdict=Pcountdown(self.start_time)
            str="%s第%d天%d小时%d分%d秒"%(self.title,cdict["day"],cdict["hour"],cdict["minute"],cdict["second"])
            return  str
        if self.type==2:
            cdict=Icountdown(self.end_time)
            str="%s还剩%d天%d小时%d分%d秒"%(self.title,cdict["day"],cdict["hour"],cdict["minute"],cdict["second"])
            return  str
    def __repr__(self):
        """
        打印计时器
        """
        return f"{self.title}, {self.type}, {self.end_time},{self.end_time}"
    def run(self,ui):
        """
        计时器刷新线程线程，一秒钟刷新一次
        :param ui: 计时器ui类

        """
        while True:
            if self.state==0:
                ui.tlable.config(text=self.Refresh())
                time.sleep(1)
            else:
                break

    def start(self,ui):
        """
        启动计时器
        :param ui: 计时器ui类

        """
        self.refresh_thead=Thread(target=self.run,args=[ui])
        self.refresh_thead.start()

    def close(self):
        """
        关闭计时器
        """
        self.state=1



def create_countdown(title,type,start=None,end=None):
    """
    创建一个计时器
    :param title: 标题
    :param type: 类型
    :param start: 开始时间
    :param end: 结束时间
    :return: 计时器对象
    """
    clist=read_countdown()
    if len(clist)==0:
        id=1
    else:
        id=clist[-1]["id"]+1
    return countdown(id,title,type,start,end)


def get_countdown_list():
    """
    获取所有计时器
    :return: 计时器列表
    """
    #把ead_countdown()返回的字典列表转换成countdown对象列表
    clist=read_countdown()
    countdown_list=[]
    for i in clist:
        countdown_list.append(countdown(i["id"],i["title"],i["type"],i["start_time"],i["end_time"]))
    return countdown_list


def delete_countdown(id):
    """
    删除计时器
    :param id: 计时器id
    """
    #删除id为id的countdown对象
    json_dict=read_json()
    for i in json_dict["list"]:
        if i["id"]==id:
            json_dict["list"].remove(i)
            break
    write_json(json_dict)