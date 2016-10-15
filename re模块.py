#!/usr/bin/python
#-*- coding:utf-8 –*-
import re	#系统自带，正则表达式处理#返回pattern对象

#常用匹配函数
#re.match(pattern, string[, flags])
#re.search(pattern, string[, flags])
#re.split(pattern, string[, maxsplit])
#re.findall(pattern, string[, flags])
#re.finditer(pattern, string[, flags])
#re.sub(pattern, repl, string[, count])
#re.subn(pattern, repl, string[, count])
 
def func(m):
    return m.group(1).title() + ' ' + m.group(2).title()

if __name__=="__main__":
	#使用re.compile(string[,flag])，返回pattern对象 
	#flag参数含义如下
	#	re.I(全拼：IGNORECASE): 忽略大小写（括号内是完整写法，下同）
	#	re.M(全拼：MULTILINE): 多行模式，改变'^'和'$'的行为
	#	re.S(全拼：DOTALL): 点任意匹配模式，改变'.'的行为
	#	re.L(全拼：LOCALE): 使预定字符类 \w \W \b \B \s \S 取决于当前区域设定
	#	re.U(全拼：UNICODE): 使预定字符类 \w \W \b \B \s \S \d \D 取决于unicode定义的字符属性
	#	re.X(全拼：VERBOSE): 详细模式。这个模式下正则表达式可以是多行，忽略空白字符，并可以加入注释
	pattern = re.compile(r'hello') 

	# 使用re.match匹配文本，获得匹配结果，无法匹配时将返回None
	m = re.match(pattern, 'hello world!')
	print "m.string:", m.string								# hello world!
	print "m.re:", m.re										# <_sre.SRE_Pattern object at 0x019080F0>
	print "m.pos:", m.pos									# 0
	print "m.lastindex:", m.lastindex						# None
	print "m.lastgroup:", m.lastgroup						# None
	print "m.group():", m.group()							# hello
	print "m.groups():", m.groups()							# ()
	print "m.groupdict():", m.groupdict()					# {}

	str = 'one1two2three3four4'
	pattern = re.compile(r'\d+')
	print re.split(pattern,str)			# ['one', 'two', 'three', 'four', '']
	print re.findall(pattern,str)		# ['1', '2', '3', '4']
	for m in re.finditer(pattern,str):
		print m.group()					# 1 2 3 4

	pattern = re.compile(r'(\w+) (\w+)')
	s = 'i say, hello world!'
	print re.sub(pattern,r'\2 \1', s)	# say i, world hello!
	print re.sub(pattern,func, s)		# I Say, Hello World!
	
	

	
	

