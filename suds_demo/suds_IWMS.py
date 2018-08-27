# encoding=utf-8
'''
调用JAVA cxf webservice
 
 调用B2B webservice 修改外箱标净重/毛重
 http://192.168.2.241:8181/wms/services/HikRpcService?wsdl
  http://192.168.4.101:8181/wms/services/HikRpcService?wsdl
 result = client.service.getDeliveryOrder(  json.dumps(data))   
'''

import suds  
import json
from suds.client import Client
url = 'http://192.168.4.101:8181/wms/services/HikRpcService?wsdl'

# url = 'http://192.168.60.43:8081/cywscenter/ws/shd?wsdl'
url = 'http://192.168.2.241:8181/wms/services/HikRpcService?wsdl'
# url = 'http://localhost:4040/cywscenter/ws/shd?wsdl'
'''
plantCode     --账套
locCode       --库位
matCode       --料号
batchNum      --批号
'''

data = {"reqCode":"T60000011913","data":{"plantCode":"T2"
                , "locCode":"F102"
                  }   }  



client = suds.client.Client(url)  
print (client)  
result = client.service.getStocks(json.dumps(data))   
print (result)  
# print (client.last_received()  )
