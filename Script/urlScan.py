import urllib.request
import time

opener = urllib.request.build_opener()
opener.addheaders = [('User-agent'),'Mozilla/49.0.2']
file = open('./1.txt')
lines = file.readlines()
aa=[]
for line in lines:
    temp = line.replace('\n','')
    aa.append(temp)

print('scan: ')
for a in aa:
    tempUrl = a
    try:
        opener.open(tempUrl)
        print(tempUrl)
    except:
        print("error")


#    time.sleep(1)
