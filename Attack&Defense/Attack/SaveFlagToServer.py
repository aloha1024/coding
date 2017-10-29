#encoding=utf-8
import urllib

import urllib2
import cookielib


flag=['sju{123}']  #保存flag列表

filename = 'cookie.txt'
cookie = cookielib.MozillaCookieJar(filename)
#声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
for i in range(len(flag)):
	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
	postdata = urllib.urlencode({
                        'flag':flag[i],
			'token':'',
			'log':'admin',
			'pwd':'admin'	
        	        })
	#登录flag提交界面的url
	loginUrl = 'http://192.168.19.47/wp-login.php'
	#模拟登录，并把cookie保存到变量
	result = opener.open(loginUrl,postdata)
	#cookie.save(ignore_discard=True, ignore_expires=True)
	#gradeUrl = 'http://192.168.19.47/wp-admin'
	#result = opener.open(gradeUrl)
	print result.read()
