#### Cookie技术

HTTP协议无状态

某些网站为了辨别用户身份、进行session跟踪而储存在本地终端的数据

RFC265

#### 缓存和Web代理服务器技术

在不访问服务器的前提下满足客户端的请求

优点：

- 缩短客户请求的响应时间
- 节省企业，机构开支

#### P2P架构和C/S架构

文件分发时，C/S架构线性增长

而P2P架构则具有一定的极限值，有很好的稳定性

#### Socket

进程间通信：在客户进程和服务器进程的通信中，使用服务器主机ip地址标识服务器，再利用端口号（16位整数）查找。

故Socket对外标识通信端点：IP地址+端口号

操作系统/进程管理套接字（对内）：套接字描述符-小整数

WinSock：

WSAStartup：初始化socket库

WSACleanup：清除/中止socket库

socket：创建套接字

connect：连接远端服务器（客户端）

closesocket:释放套接字

bind:绑定本地IP地址和端口号（通常客户端不需要）

listen: 置（服务器）端TCP套接字为监听模式，并设置队列大小

accept：接受连接请求，仅用于TCP

recv：

recvfrom：接受非连接模式的数据报（UDP）

send：调用的connect函数的套接字

sendto：传输非连接模式的套接字



#### TCP/IP定义了网络字节顺序

htons：本地字节顺序——网络字节顺序16bits

ntons：网络——本地

htonl：本地字节顺序——网络字节顺序32bits

ntohl：网络——本地

##### 解析服务器IP地址



