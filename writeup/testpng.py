import os
import binascii
import struct
misc = open("/Users/zinc/Desktop/WhatIsThat.png","rb").read()
for i in range(1024):
    data = misc[12:20] + struct.pack('>i',i)+ misc[24:29]
    crc32 = binascii.crc32(data) & 0xffffffff
    if crc32 == 0x402e2d95:
        print i

'''
图片crc校验失败，但是高和宽却都有相应的数值，根据图片手指指向的地方猜测可能是高度被篡改
因此根据crc的值来爆破高度
得到高度为626
在010editor中修改高度获得flag
'''