import requests
import json

class  apifunction():       # url=1 查询城市天气  url=2  天气类型  url=3  城市列表 ； 后两个 city=""
    def __init__(self,appkey,url,city):
        self.appkey=appkey
        self.url=url
        self.city=city
        self.type=1         #用于判断此后存储信息的字典类型
        self.weathertype={}
        self.citytype={}
        self.data={}
    def cityget(self,k):    #k表示输入城市名称,用于测试
        self.city=k
    def cityname(self):     # 输入城市的名称，用于测试
        name = input("请输入城市名称xx市：")
        self.city=name
    def urltype(self,a):    #a表示查询的方法
        self.url=a
    def urlget(self):
        if   self.url==1:
             self.url="http://op.juhe.cn/onebox/weather/query"
             self.type=1
        elif self.url==2:
             self.url="http://apis.juhe.cn/simpleWeather/wids"
             self.city=""
             self.type=2
        elif self.url==3:
             self.url="http://apis.juhe.cn/simpleWeather/cityList"
             self.city=""
             self.type=3

    def getkey(self):       # 防止appkey泄露
        f = open("appkey.txt", "r")  # 设置文件对象
        str = f.read()  # 将txt文件的所有内容读入到字符串str中
        f.close()  # 将文件关闭
        self.appkey=str
    def mydata(self):
        try:   #防止错误查询
           params = {
                  "cityname": self.city,  # 要查询的城市，如：温州、上海、北京、合肥
                  "key": self.appkey,     # 应用APPKEY(应用详细页查询)
                  "dtype": "json",   # 返回数据的格式,xml或json，默认json
                     }
           r = requests.get(self.url,params,timeout=30)
           r.raise_for_status()
           r.encoding = r.apparent_encoding      #用解析页面的方法获取编码方式，防止乱码信息
           result=json.loads(r.text)             #用json格式,使之成为dict或list类型
           if   self.type==1:    self.data=result
           elif self.type==2:    self.weathertype=result
           else             :    self.citytype=result
           return  result

        except:
           print("出现错误，查询失败")
           return ""

def  main():   #试验函数
        city = "合肥"
        classtest = apifunction('',1,city )
        classtest.urlget()
        classtest.getkey()
        classtest.cityname()
        classtest.mydata()
        print('data')
        print(type(classtest.data))
        print(classtest.data)
        print('weather')
        print(type(classtest.weathertype))
        print(classtest.weathertype)
        print('city')
        print(type(classtest.citytype))
        print(classtest.citytype)
if __name__ == '__main__':

    main()




