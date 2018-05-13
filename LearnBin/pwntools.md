pwntools使用

p64(0x12345678)
u64(0x12345677)
enhex(p64(0x12345678))


send 发送一个字符串 sendline
rece 接收字符  recvuntil 接收字符串直到遇到recvuntil为止
recvrepeat

cyclic 100 生成一百个字符

查询是哪个libc  
libcdb.com  and    libc-database//github.com

objdump -R xxxx查看程序的构造表 
