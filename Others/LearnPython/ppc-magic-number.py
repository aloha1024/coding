import socket
import re, sys

nums = [0] * 1024
cnt = 0


def change(l, r, n, flag):
    if flag:
        for i in range(l, r):
            nums[i] = n
    else:
        for i in range(l, r):
            nums[i] -= n


def func2(l, r, n):
    send_str = "? %d %d\n" % (l, (l+r)/2)
    print send_str,
    sock.send(send_str)
    recv_str = sock.recv(1024)
    try:
        m = int(recv_str[:-1])
    except:
        print "Error"
        sys.exit(0)
    print m
    if r - l == 2:
        print "-", m, n
        if m == 1 and n == 1:
            nums[l] = -1
            nums[l+1] = 0
            print l
            return 0
        elif m == 1 and n == 2:
            nums[l] = -1
            nums[l+1] = -1
            print l, l+1
            return 0
        elif m == 2 and n == 2:
            nums[l] = -2
            nums[l+1] = 0
            print l, l
            return 0
        elif m == 0 and n == 1:
            nums[l+1] = -1
            nums[l] = 0
            print l+1
            return 0
        elif m == 0 and n == 2:
            nums[l] = 0
            nums[l+1] = -2
            print l+1, l+1
            return 0
        else:
            sock.send("? %d %d\n" % (l, l+1))
            recv_str = sock.recv(1024)
            try:
                m = int(recv_str[:-1])
            except:
                print "Error"
                sys.exit(0)
            nums[l] = -1 * m
            sock.send("? %d %d\n" % (l+1, r))
            recv_str = sock.recv(1024)
            try:
                m = int(recv_str[:-1])
            except:
                print "Error"
                sys.exit(0)
            nums[l+1] = -1 * m
            return 0
    change(l, (l + r)/2, m, True)
    change((l + r) / 2, r, n-m, True)
    if m != 0:
        func2(l, (l+r)/2, m)
    if n-m != 0:
        func2((l+r)/2, r, n-m)


if __name__ == "__main__":
    sock = socket.socket()
    sock.connect(("47.89.18.224", 10011))
    #sock.connect(("127.0.0.1", 23333))

    while 1:
        while 1:
            text = sock.recv(1024)
            regex = re.compile(r"Level \d+ : n = (\d+)")
            try:
                n = int(regex.findall(text)[0])
                break
            except:
                if text:
                    print text
        ans = n
        print text, n

        cnt = 0
        nums = [0] * 1024
        for i in range(0, 16):
            sock.send("? %d %d\n" % (i * 64, i * 64 + 64))
            recv_str = sock.recv(1024)
            m = int(recv_str[:-1])
            print i, m
            if m != 0:
                change(i * 64, i * 64 + 64, m, True)
                func2(i * 64, i * 64 + 64, m)

        #change(0, 1024, n, True)
        #func(0, 1024, n)

        s = "!"
        for i in range(0, 1024):
            if nums[i] < 0:
                for j in range(0, abs(nums[i])):
                    s+= " " + str(i)
        s += "\n"
        print s
        sock.send(s)