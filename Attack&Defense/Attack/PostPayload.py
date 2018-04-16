#encoding=utf-8
import urllib
import urllib2
import cookielib
 
filename = 'cookie.txt'
#声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
cookie = cookielib.MozillaCookieJar(filename)
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
postdata = urllib.urlencode({
			'log':'admin',
			'pwd':'admin'
		})
loginUrl = 'http://192.168.19.47/wp-login.php'
#模拟登录，并把cookie保存到变量
result = opener.open(loginUrl,postdata)
