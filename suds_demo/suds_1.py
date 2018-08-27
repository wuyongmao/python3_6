#encoding=utf-8
'''
调用JAVA cxf webservice

'''
  
from suds.client import Client
sobject={}
url = 'http://localhost:8000/?wsdl'
client = Client(url)  
r=client.service.say_hello( 'Milton', 2)    # 调用这个接口下的getMobileCodeInfo方法，并传入参数
print(client.wsdl)
    
   
