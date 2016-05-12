# HttpClient.py is written by [xqin]: https://github.com/xqin/SmartQQ-for-Raspberry-Pi
import cookielib, urllib, urllib2


import urllib2,cookielib
cookie=cookielib.CookieJar()
cookiehand=urllib2.HTTPCookieProcessor(cookie)

opener=urllib2.build_opener(cookiehand)
opener.addheaders = [
        ('Accept', 'application/javascript, */*;q=0.8'),
        ('User-Agent', 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)')
]

urllib2.install_opener(opener)

req = urllib2.Request('http://www.baidu.com')
res= urllib2.urlopen(req)



for i in cookie:
    print 'name: %s, value:%s ' % (i.name, i.value)

# class HttpClient:
#     __cookie = cookielib.CookieJar()
#     __req = urllib2.build_opener(urllib2.HTTPCookieProcessor(__cookie))
#     __req.addheaders = [
#         ('Accept', 'application/javascript, */*;q=0.8'),
#         ('User-Agent', 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)')
#     ]
#     urllib2.install_opener(__req)
#
#     def Get(self, url, refer=None):
#         try:
#             req = urllib2.Request(url)
#             if not (refer is None):
#                 req.add_header('Referer', refer)
#             return urllib2.urlopen(req).read()
#         except urllib2.HTTPError, e:
#             return e.read()
#
#
# c = HttpClient()
# c.Get('http://www.baidu.com')
#
# print dir(urllib2)


        

        


    


    


 

# b = webdriver.Firefox() # Get local session of firefox
# b.get("http://127.0.0.1:8069") # Load page
# send_key(b, 'db', 'szodoo2')
# b.execute_script("document.getElementById('dbselector').submit()")
# send_key(b, 'login', 'admin')
# send_key(b, 'password', '2d22')
# bt_click(b,'btn-primary')
    

    









