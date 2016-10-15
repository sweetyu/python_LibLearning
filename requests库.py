#!/usr/bin/python
#-*- coding:utf-8 –*-
import requests 

#遇到网络问题（如：DNS查询失败、拒绝连接等）时，Requests会抛出一个ConnectionError 异常。
#遇到罕见的无效HTTP响应时，Requests则会抛出一个 HTTPError 异常。
#若请求超时，则抛出一个 Timeout 异常。
#若请求超过了设定的最大重定向次数，则会抛出一个 TooManyRedirects 异常。
#所有Requests显式抛出的异常都继承自 requests.exceptions.RequestException 。

#返回网页返回码
def get_status(url):
    r = requests.get(url, allow_redirects = False)
    return r.status_code

#代理访问
def getProxies(url,pro):
	pro = {
	  "http": "http://10.10.1.10:3128",
	  "https": "user:pass@http://10.10.1.10:1080",	#使用用户名和密码
	}
	requests.get(url, proxies=pro)

if __name__ == '__main__':	
	#HTTP请求类型:POST,PUT,DELETE,HEAD,OPTIONS,GET
	payload = {'ie': 'utf-8', 'wd': 'python'}
	#不允许自动跳转，超时时间为0.1s
	r = requests.get("http://www.baidu.com/s", params=payload, allow_redirects = False, timeout=0.1)

	print(r.url)				#请求超链接
	print(r.request.headers)	#请求头信息
	print(r.headers["content-type"])		#返回部分头部信息
	#或者使用   print(r.headers.get('content-type'))
	print(r.encoding)			#编码信息
	text1 = r.text				#返回内容部分
	text2 = r.content			#返回内容部分(推荐)
	print(r.cookies)			#缓存


