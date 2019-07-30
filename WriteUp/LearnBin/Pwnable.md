gcc -fno-stack-protector -z execstack bof.c -o bof
关闭两个保护

sudo echo "set disassembly-flavor intel"> ~/.gdbintit
将gdb的语法由ATIT语法转换为Inter语法

真实漏洞的抽象
cpu和内存之间交换数据和指令
漏洞产生的根本的原因 数据和指令并不能完全的分开
输入了数据，被当成指令执行

pwn 漏洞----->控制流劫持

pwn的伪代码一般都很简洁，关注目标函数饥渴

关注一些目标函数
例如没有做长度校验的
gets(&buf),scanf,strcpy,strcat

查看文件格式，看多少位
32 和 64位
寄存器位数不同
动态链接和动态链接
























