'''
Created on 2018年5月7日

@author: yongmao.wu
'''
import configparser
if __name__ == '__main__':
    config=configparser.ConfigParser()
    config.read("config", "utf-8")
    ret = config.sections()
    print(ret)
    for s in ret :
        items=config.items(s)
        for item in items :
            print( item )
    v=config.get("section1", "k2")
    print(v)
    # 检查
    has_opt = config.has_option('section3', 'k1') 
    if has_opt :
        print(has_opt)
    else :
        config.add_section("section3")
        config.set("section3", "k1", "v1")
        config.write(open("config","w") )
        
    f=open("config","r")
    print(f.read())
    
    