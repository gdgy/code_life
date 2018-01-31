### 查看打开文件的程序 ###
    lsof
	sudo lsof myapp.log      
	COMMAND   PID USER   FD   TYPE DEVICE SIZE/OFF    NODE NAME
	python3 26195 root    4w   REG 202,16   394579 1310724 myapp.log
### curl ###
http上传文件

    curl -F "file=@shell.c" -XPOST http://127.0.0.1:5000/upload

### 请求头和响应头 ###
    curl -v http://www.baidu.com

### grep ###
    or 关键词
	grep 'key1\|key2'
	二进制
	grep -a  'key'
### 编译 ###
	 g++ -std=c++11
	
