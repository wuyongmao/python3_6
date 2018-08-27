#encoding=utf-8
import suds  
from suds.client import Client
 
'''
url = 'http://http://localhost:4040/cywscenter/ws/wxb?wsdl'  
#url = 'http://10.3.18.44:8080/test/calc?wsdl'  
client = suds.client.Client(url)  
service = client.service  
'''
 
  
url = 'http://www.webxml.com.cn/WebServices/MobileCodeWS.asmx?wsdl'  
  
client = suds.client.Client(url)  
  
# print client  
  
result =  client.service.getMobileCodeInfo('13528190235') # 手机号码  
  
print( result)  
   