#encoding=utf-8
'''
火车时刻表 
webservice:
  wsdl:http://www.webxml.com.cn/WebServices/TrainTimeWebService.asmx?wsdl
     描述：http://www.webxml.com.cn/WebServices/TrainTimeWebService.asmx
  
getStationAndTimeDataSetByLikeTrainCode(TrainCode ,UserID) 
        TrainCode: 车次
        UserID = 商业用户ID（普通用户不需要）


'''
 
from suds.client import Client   
from suds.xsd.doctor import ImportDoctor,Import
   
#Import和DoctorImport是提供wsdl中缺少的import标签的
imp = Import("http://www.w3.org/2001/XMLSchema",location="http://www.w3.org/2001/XMLSchema.xsd")
imp.filter.add("http://WebXml.com.cn/")
doctor=ImportDoctor(imp)
url ='http://www.webxml.com.cn/WebServices/TrainTimeWebService.asmx?wsdl'
client = Client(url,doctor=doctor)
r = client.service.getStationAndTimeDataSetByLikeTrainCode('G6108','')
print (r)
