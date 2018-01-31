#include <netinet/in.h>
#include <sys/socket.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <sys/epoll.h>
#include <time.h>
#include <unistd.h>
#include <sys/types.h>
#include <arpa/inet.h>

#define MAXSIZE     1024
#define IPADDRESS   "127.0.0.1"
#define SERV_PORT   8787
#define FDSIZE        1024
#define EPOLLEVENTS 20

static void handle_connection(int sockfd);
static void
handle_events(int epollfd,struct epoll_event *events,int num);
//static void do_read(int epollfd,int fd,int sockfd,char *buf);
static void do_read(int fd, char *buf);
static void do_write(int epollfd,int fd,int sockfd,char *buf);
static void add_event(int epollfd,int fd,int state);
static void delete_event(int epollfd,int fd,int state);
static void modify_event(int epollfd,int fd,int state);
static void do_epoll(int epollfd);
int count = 0;

int main(int argc,char *argv[])
{
    int epollfd = epoll_create(EPOLLEVENTS);
    add_event(epollfd, STDIN_FILENO, EPOLLIN|EPOLLET);
    struct epoll_event events[EPOLLEVENTS];
    int ret;
    for (; ;)
    {
        ret = epoll_wait(epollfd, events, EPOLLEVENTS, -1);
        handle_events(epollfd, events, ret);
    }
    
    return 0;
}

static void add_event(int epollfd, int fd, int listen_event)
{
    struct  epoll_event ev;
    ev.events = listen_event;
    ev.data.fd = fd;
    epoll_ctl(epollfd, EPOLL_CTL_ADD, fd, &ev);    
}



static void handle_events(int epollfd,struct epoll_event *events,int num){
    int i, fd;
    int tmp_fd;
    char buf[MAXSIZE];
    printf("enter handle_events");
    for (i = 0; i < num; i++)
    {
        printf("events_num:%d \n", num);
        fd = events[i].data.fd;
        if (fd == STDIN_FILENO && events[i].events & EPOLLIN)
        {    //do_read(fd, buf);
            printf("trigger:%d \n", count++);
            if (0 == count%2)
                do_read(fd, buf);
            sleep(1);
            
        }  
    }
}

static void do_read(int fd, char* buf)
{
    int nread;
    nread = read(fd, buf, MAXSIZE);
    if (nread > 0)
        buf[nread] = '\0';
        printf("read:%s", buf);
}