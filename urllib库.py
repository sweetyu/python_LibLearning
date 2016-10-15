#!/usr/bin/python
#-*- coding:utf-8 –*-
import urllib,urllib2
import cookielib

#获取请求数据
def openUrl(request):
	#方式一
	#response = urllib2.urlopen(url,data,timeout)	#urlopen是特殊的opener
	#方式二(包括异常处理)
	try: 
		response = urllib2.urlopen(request)
	except urllib2.HTTPError, e:
	    print e.code
	except urllib2.URLError, e:
	    print e.reason
	else:
	    print response.readline()

#get请求方式
def getUrl(url,data):
	geturl = url + "?"+data
	request = urllib2.Request(geturl)
	return request

#post请求方式
def postUrl(url,data):
	request = urllib2.Request(url,data) 
	return request

#设置代理访问服务
def getProxies():
	enable_proxy = True
	proxy_handler = urllib2.ProxyHandler({"http" : 'http://some-proxy.com:8080'})
	null_proxy_handler = urllib2.ProxyHandler({})
	if enable_proxy:
	    opener = urllib2.build_opener(proxy_handler)
	else:
	    opener = urllib2.build_opener(null_proxy_handler)
	urllib2.install_opener(opener)

#获取并保存cookie
def setCookie(url):
	#声明一个CookieJar对象实例来保存cookie
	cookie = cookielib.CookieJar()
	#利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
	handler=urllib2.HTTPCookieProcessor(cookie)
	#通过handler来构建opener
	opener = urllib2.build_opener(handler)
	#此处的open方法同urllib2的urlopen方法，也可以传入request
	response = opener.open(url)
	for item in cookie:
	    print 'Name = '+item.name
	    print 'Value = '+item.value
	return cookie

#获取cookie
def getCookie(cookie,req):
	#利用urllib2的build_opener方法创建一个opener
	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
	response = opener.open(req)
	print response.read()

if __name__=="__main__":	
	#待传递参数
	values = {"username":"1016903103@qq.com","password":"XXXX"}
	values = {};values['username'] = "1016903103@qq.com";values['password'] = "XXXX"
	data = urllib.urlencode(values)

	headers = { 'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)' }
	url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"

	request = postUrl(url,data)
	request = getUrl(url,data)
	request = urllib2.Request(url, data, headers) 

	getCookie(setCookie(url),request)
