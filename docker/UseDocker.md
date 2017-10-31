如何在mac上使用docker
step1:从docker官网上下载docker for mac
step2:国内访问国外镜像源时速度很感人，所以我们要在docker上配置加速器，这里我们选择用阿里云的加速器
具体步骤：待续

docker 使用总结

docker ps -a #列出所有docker容器，包括正在运行的和未运行的
docker run -it ubuntu /bin/bash
-i -t：想要创建一个可以和我们进行交互的shell，此参数不可少

容器命名
docker run --name TestDocker -i -t ubuntu /bin/bash

重启停止的容器
docker start TestDocker

附着到正在运行的容器
docker attach TestDocker

创建守护容器
docker run --name TestDocker -d ubuntu /bin/sh -c "while true; do echo hello world; sleep 1; done"
-d：让docker在后台运行
在要运行的命令中使用while循环

获取守护容器的日志
docker logs TestDocker

跟踪守护容器日志
docker logs -f TestDocker

跟踪守护容器最新日志
docker logs -ft TestDocker

统计信息
docker stats name
显示一个或多个容器的统计信息

在容器中运行后台任务
docker exec -d TestDocker touch /etc/new_config_file
-d：需要运行一个后台进程

停止正在运行的容器
docker stop TestDocker

自动重启容器
docker run --restart = always --name TestDocker -d ubuntu /bin/sh -c "while true; do echo hello world; sleep 1; done"
指定重启次数
docker run --restart = on-failure:5(当容器退出代码味非0时，docker会尝试自动重启容器，最多5次) --name TestDocker -d ubuntu /bin/sh -c "while true; do echo hello world; sleep 1; done"

查看容器，除了可以通过docker ps命令获取容器信息，还可以使用docker inspect来获得更多的容器信息
docker inspect TestDocker

返回容器的运行状态
docker inspect --format = '{{ .State.Running }}' TestDocker

查看容器的ip地址
docker inspect --format = '{{ .NetworkSettings.IPAddress }}'

查看多个容器
docekr inspect --format = '{{.name}} {{.State.Running}}' \ TestDocker TestDocker0

删除容器
docker rm TestDocker 
docker rm TestDocker TestDocker0

删除所有容器
docker rm 'sudo docker ps -a -q'
docker ps列出现在所有的容器 -a列出所有容器 -q 返回容器的id而不会返回其他信息，这样我们就得到了容器id的列别，传给docker rm命令，从而删除所有的容器

列出docker 镜像
docker images

拉取ubuntu镜像
docker pull ubuntu:12.04

运行一个带标签的docker镜像
docker run -i -t --name TestDocker ubuntu:12.04 /bin/bash
从镜像ubuntu:12.04启动一个容器，这个镜像的操作系统是ubuntu:12.04

运行dockerfile
docker build -t = "test/test_web" .
从当前目录读取dockerfile并新建一个名为test的仓库，镜像名为test_web
也可以在构建镜像的过程中为镜像设置一个标签，其使用方法为"镜像名:标签"
docker build -t = "test/test_web:a1" .

docker build -t "test/test_web" -f path/to/file
文件名可以不必命名为Dockerfile，但是必须要位于构建上下文之中

将构建上下文上传到docker守护进程
sending builed context to docker daemon 