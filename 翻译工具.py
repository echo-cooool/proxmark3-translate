import re  
 

import  xml.dom.minidom
# coding=utf-8
import urllib
import urllib2
import json
import time
import hashlib

import sys  

reload(sys)  

sys.setdefaultencoding('utf8')   

class YouDaoFanyi:
    def __init__(self, appKey, appSecret):
        self.url = 'https://openapi.youdao.com/api/'
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36",
        }
        self.appKey = appKey  # 应用id
        self.appSecret = appSecret  # 应用密钥
        self.langFrom = 'auto'   # 翻译前文字语言,auto为自动检查
        self.langTo = 'auto'     # 翻译后文字语言,auto为自动检查

    def getUrlEncodedData(self, queryText):
        '''
        将数据url编码
        :param queryText: 待翻译的文字
        :return: 返回url编码过的数据
        '''
        salt = str(int(round(time.time() * 1000)))  # 产生随机数 ,其实固定值也可以,不如"2"
        sign_str = self.appKey + queryText + salt + self.appSecret
        sign = hashlib.md5(sign_str).hexdigest()
        payload = {
            'q': queryText,
            'from': self.langFrom,
            'to': self.langTo,
            'appKey': self.appKey,
            'salt': salt,
            'sign': sign
        }

        # 注意是get请求，不是请求
        data = urllib.urlencode(payload)
        return data

    def parseHtml(self, html):
        '''
        解析页面，输出翻译结果
        :param html: 翻译返回的页面内容
        :return: None
        '''
        data = json.loads(html)
        #print '-' * 10
        translationResult = data['translation']
        if isinstance(translationResult, list):
            translationResult = translationResult[0]
        #print translationResult
        return translationResult
        if "basic" in data:
            youdaoResult = "\n".join(data['basic']['explains'])
            #print '有道词典结果'
            #print youdaoResult
            
            
        #print '-' * 10
        
    def translate(self, queryText):
        data = self.getUrlEncodedData(queryText)  # 获取url编码过的数据
        target_url = self.url + '?' + data    # 构造目标url
        request = urllib2.Request(target_url, headers=self.headers)  # 构造请求
        response = urllib2.urlopen(request)  # 发送请求
        return self.parseHtml(response.read())    # 解析，显示翻译结果


if __name__ == "__main__":
    appKey = '############'  # 应用id
    appSecret = '#########################'  # 应用密钥
    fanyi = YouDaoFanyi(appKey, appSecret)
    #while True:
     #   queryText = raw_input("请输入你好翻译的文字[Q|quit退出]: ").strip()
      #  if queryText in ['Q', 'quit']:
       #     break
        # fanyi.translate(queryText)


def change_node_properties(nodelist, kv_map, is_delete=False):
  '''修改/增加 /删除 节点的属性及属性值
    nodelist: 节点列表
    kv_map:属性及属性值map'''
  for node in nodelist:
    for key in kv_map:
      if is_delete:
        if key in node.attrib:
          del node.attrib[key]
      else:
        node.set(key, kv_map.get(key))
 
def change_node_text(nodelist, text, is_add=False, is_delete=False):
  '''改变/增加/删除一个节点的文本
    nodelist:节点列表
    text : 更新后的文本'''
  for node in nodelist:
    if is_add:
      node.text += text
    elif is_delete:
      node.text = ""
    else:
      node.text = text

def write_result(str):  
    writeresult=file(r'test_result.log','a+')  
    str = unicode(str)
    str1=writeresult.write(str+'\n')  
    writeresult.close()  
    return str 

def alter(file,old_str,new_str):
    """
    替换文件中的字符串
    :param file:文件名
    :param old_str:就字符串
    :param new_str:新字符串
    :return:
    """
    file_data = ""
    with open(file, "r") as f:
        for line in f:
            if old_str in line:
                line = line.replace(old_str,new_str)
            file_data += line
    with open(file,"w") as f:
        f.write(file_data)

#打开xml文档
dom = xml.dom.minidom.parse('1.xml')
#得到文档元素对象
root = dom.documentElement
print root.nodeName
bb = root.getElementsByTagName('section')
b= bb[0]
print b.nodeName

itemlist = root.getElementsByTagName('item')
for i in range(3000):
     item = itemlist[i]
     if item.getAttribute("text") != "" :
     #print item
        u = item.getAttribute("text") 
        print u
        if u != "" :
            a = fanyi.translate(u)         
            #   print a
            print(write_result(u))
            print(write_result(a))
            alter("1.xml", u, a)



 
  
 
      
