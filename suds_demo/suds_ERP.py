import suds 
from suds.client import Client

url = "http://192.168.1.235:12581/ServiceYuYue.svc?wsdl"
# client = suds.client.Client(url)

url = 'http://192.168.60.8/web/ws/r/aws_ttsrv2?wsdl'
client = suds.client.Client(url)
# print client
result =client.service.GetAreaData('<Request><Access><Authentication user="" /><Organization name="T2"/></Access><RequestContent> <Parameter> <Record><Field name="condition" value=" 1=1 "/> </Record> </Parameter> </RequestContent> </Request> ') 
  
 

#打印出结果
print(result)