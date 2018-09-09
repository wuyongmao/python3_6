Python 3.6

| 水果 | 价格 | 数量 |
| -- | --   | --: |
| 香蕉    | $1      |   5   |
| 苹果     | $1      |   6    |
| 草莓    | $1      |   7    |
 
 
 
 
| HTTP法 | 路径	 |    		描述                     | 	 鉴权 |
| --------   | :-----   | :---- | :----: | 
| GET |  /autoconfig	 | 	查看自动配置的使用情况	    |  true |
| GET |  /configprops	 | 	查看配置属性，包括默认配置	|  true |
| GET |  /beans	      	 | 	查看bean及其关系列表	    |  true |
| GET |  /dump	      	 |     打印线程栈				| 	 true |
| GET |  /env	      	 |     查看所有环境变量			|  true |
| GET |  /env/{name}	 | 	查看具体变量值				|  true |
| GET |  /health		 | 	查看应用健康指标			|  false |
| GET |  /info	  	 	 | 	查看应用信息（需要自己在application.properties里头添加信息 ）| 	false |
| GET |  /mappings		 | 	查看所有url映射				| true |
| GET |  /metrics		 | 	查看应用基本指标			| true |
| GET |  /metrics/{name} | 	查看具体指标				| true |
| POS |  /shutdown		 |     关闭应用（要真正生效，得配置文件开启endpoints.shutdown.enabled: true）| 	true |
| GET |  /trace	         |      查看基本追踪信息		| 	true |
