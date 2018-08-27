# encoding=utf-8
'''
调用JAVA cxf webservice
 调用B2B webservice 修改外箱标净重/毛重
 http://192.168.2.241:8081/cywscenter/ws/wxb?wsdl
 result =  client.service.updateWXB(json.dumps(wxbparam))   
'''
import suds  
import json
from suds.client import Client
url = 'http://192.168.2.241:8081/cywscenter/ws/wxb?wsdl'
# url = 'http://localhost:4040/cywscenter/ws/wxb?wsdl'
wxbparam = {"reqCode":"T6000001911",
          "data":{"WXB05":"DY000220180804C00011",
                   "WXB08":22, 
                   "WXB09":22}}
client = suds.client.Client(url)  
print (client)  
result = client.service.updateWXB(json.dumps(wxbparam))   
print (result)  
  
