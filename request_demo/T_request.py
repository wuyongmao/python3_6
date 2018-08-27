'''
requests 模组使用
   1.post
   2.get
   
r.status_code #响应状态码
r.raw #返回原始响应体，也就是 urllib 的 response 对象，使用 r.raw.read() 读取
r.content #字节方式的响应体，会自动为你解码 gzip 和 deflate 压缩
r.text #字符串方式的响应体，会自动根据响应头部的字符编码进行解码
r.headers #以字典对象存储服务器响应头，但是这个字典比较特殊，字典键不区分大小写，若键不存在则返回None
#*特殊方法*#
r.json() #Requests中内置的JSON解码器
r.raise_for_status() #失败请求(非200响应)抛出异常

''' 
import requests 
import json
  
payload={'wd': 'java'}
  
#POST请求
r = requests.post('https://api.github.com/some/endpoint', data=json.dumps({'some': 'data'}))
r = requests.post('http://localhost:4040/eps/users/checklogin', data=json.dumps({ "USERname":"4897","password":"123456"}))
# print(r.json())
print(r.status_code)
# print(r.content.decode())
  

url_t="http://localhost:4040/eps/users/checklogin"
payload={ "USERname":"HZ0001","password":"123456"};

#GET请求
# g=requests.get("http://localhost:4040/eps/users/getnode?ROLE=GYS",)
# gs=requests.get('http://www.baidu.com/s', params=payload) 
gs=requests.get(url_t, params=payload) 
gs.encoding='utf-8'
# print(gs.content)
print(gs.status_code)
print(gs )

#文件写入
# f=open("E:/1.html","w",encoding='utf-8')
# f.write(gs.text)

