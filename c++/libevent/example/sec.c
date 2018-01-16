/* For sockaddr_in */
#include <netinet/in.h>
/* For socket functions */
#include <sys/socket.h>
/* For gethostbyname */
#include <netdb.h>
#include <unistd.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>


int post_file()
{
    const char query[] = 
  "POST /upload  HTTP/1.1\r\n"
  "User-Agent: curl/7.35.0\r\n"
  "Host: www.baidu.com\r\n"
  "Accept: */*\r\n"
  "\r\n"
  "Expect: 100-continue\r\n"
  "Content-Type: multipart/form-data;filename=test.cab; boundary=------------------------215fa5025e58e0c4\r\n"
  "\r\n";
  
  struct sockaddr_in server;
  int client_fd;
  client_fd = socket(AF_INET, SOCK_STREAM, 0);
  if(client_fd <= 0)
      perror("create client socket failed");
  
  const char server_addr[] = "127.0.0.1";
  const int port = 5000;
  //memset(&server, 0, sizeof(server));
  memset(&server, 0, sizeof(server));
  server.sin_family = AF_INET;
  server.sin_port = htons(port);
  inet_pton(AF_INET, server_addr, &server.sin_addr);
  //server.sin_addr = inet_addr(server_addr);
  if (connect(client_fd, (struct sockaddr*) &server, sizeof(server))) {
        perror("connect");
        close(client_fd);
        return 1;
    }
   char *buffer;
   //memset(buffer, 0, 1024);
   char header[1024];
   FILE*fp;
   fp = fopen("first.c", "r");
   fseek(fp,0L,SEEK_END); 
   int fsize=ftell(fp);
   fseek(fp, 0, 0);
   buffer = (char*)malloc(fsize*sizeof(char));
   fread(buffer, 1, fsize, fp);
   printf("%d", fsize);
   printf("%d",(int)send(client_fd, query, strlen(query), 0));
   int remaining = fsize;
   int nwritten = 0;
   while (remaining > 0)
   {
      nwritten -= send(client_fd, buffer, remaining, 0);
      remaining -= nwritten;
   }
   
   
   
}

void post_args()
{
  struct sockaddr_in server;
  int client_fd;
  client_fd = socket(AF_INET, SOCK_STREAM, 0);
  if(client_fd <= 0)
      perror("create client socket failed");
  
  const char server_addr[] = "127.0.0.1";
  const int port = 5000;
  //memset(&server, 0, sizeof(server));
  memset(&server, 0, sizeof(server));
  server.sin_family = AF_INET;
  server.sin_port = htons(port);
  inet_pton(AF_INET, server_addr, &server.sin_addr);
  //server.sin_addr = inet_addr(server_addr);
  if (connect(client_fd, (struct sockaddr*) &server, sizeof(server))) {
        perror("connect");
        close(client_fd);
        return 1;
    }
    char *pHttpPost = "POST %s HTTP/1.1\r\n"  
    "Host: %s:%d\r\n"  
    "Content-Type: application/x-www-form-urlencoded\r\n"  
    "Content-Length: %d\r\n\r\n"  
    "%s";  
  
    char* addr = "/login";  
    char* host = "127.0.0.1";  
    char* msg = "aaa=1&bbb=2";  
      
    char strHttpPost[1024] = {0};  
    sprintf(strHttpPost, pHttpPost, addr, host, port, strlen(msg), msg);  
      
    //这里忽略掉了socket连接代码  
      
    send(client_fd, strHttpPost, strlen(strHttpPost), 0);  
}


int main(int c, char **v)
{
    post_args();
    const char query[] =
        "GET / HTTP/1.0\r\n"
        "Host: www.baidu.com\r\n"
        "\r\n";
    const char hostname[] = "www.baidu.com";
    struct sockaddr_in sin;
    struct hostent *h;
    const char *cp;
    int fd;
    ssize_t n_written, remaining;
    char buf[1024];

    /* Look up the IP address for the hostname.   Watch out; this isn't
       threadsafe on most platforms. */
    h = gethostbyname(hostname);
    if (!h) {
        fprintf(stderr, "Couldn't lookup %s: %s", hostname, hstrerror(h_errno));
        return 1;
    }
    if (h->h_addrtype != AF_INET) {
        fprintf(stderr, "No ipv6 support, sorry.");
        return 1;
    }

    /* Allocate a new socket */
    fd = socket(AF_INET, SOCK_STREAM, 0);
    if (fd < 0) {
        perror("socket");
        return 1;
    }

    /* Connect to the remote host. */
    sin.sin_family = AF_INET;
    sin.sin_port = htons(80);
    sin.sin_addr = *(struct in_addr*)h->h_addr;
    if (connect(fd, (struct sockaddr*) &sin, sizeof(sin))) {
        perror("connect");
        close(fd);
        return 1;
    }

    /* Write the query. */
    /* XXX Can send succeed partially? */
    cp = query;
    remaining = strlen(query);
    while (remaining) {
      n_written = send(fd, cp, remaining, 0);
      if (n_written <= 0) {
        perror("send");
        return 1;
      }
      remaining -= n_written;
      cp += n_written;
    }

    /* Get an answer back. */
    while (1) {
        ssize_t result = recv(fd, buf, sizeof(buf), 0);
        if (result == 0) {
            break;
        } else if (result < 0) {
            perror("recv");
            close(fd);
            return 1;
        }
        fwrite(buf, 1, result, stdout);
    }

    close(fd);
    return 0;
}