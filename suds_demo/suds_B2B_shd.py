# encoding=utf-8
'''
调用JAVA cxf webservice
 
 调用B2B webservice 修改外箱标净重/毛重
 http://192.168.2.241:8081/cywscenter/ws/shd?wsdl
 result = client.service.getDeliveryOrder(  json.dumps(data))   
'''

import suds  
import json
from suds.client import Client
 
# url = 'http://192.168.60.43:8081/cywscenter/ws/shd?wsdl'
url = 'http://192.168.2.241:8081/cywscenter/ws/shd?wsdl'
# url = 'http://localhost:4040/cywscenter/ws/shd?wsdl'

data = {"reqCode":"T6000001913", "data":{"orderNum":"YXH0012018080601"}}  
client = suds.client.Client(url)  
print (client)  
result = client.service.getDeliveryOrder(json.dumps(data))   
print (result)  
# print (client.last_received()  )
