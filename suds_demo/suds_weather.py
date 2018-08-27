#encoding=utf-8
'''
天气
webservice:
  wsdl:http://www.webxml.com.cn/WebServices/WeatherWebService.asmx?wsdl
     描述：http://www.webxml.com.cn/WebServices/WeatherWebService.asmx
  
getSupportCity( )  


''' 
  
from suds.client import Client   
from suds.xsd.doctor import ImportDoctor,Import 
#Import和DoctorImport是提供wsdl中缺少的import标签的
imp = Import("http://www.w3.org/2001/XMLSchema",location="http://www.w3.org/2001/XMLSchema.xsd")
imp.filter.add("http://WebXml.com.cn/")
doctor=ImportDoctor(imp)
url ='http://www.webxml.com.cn/WebServices/WeatherWebService.asmx?wsdl'
client = Client(url,doctor=doctor)
r2 = client.service.getWeatherbyCityName("中山");

print (r2)
