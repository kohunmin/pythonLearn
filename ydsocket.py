# -*- coding: utf-8 -*-
__author__ = 'Administrator'

import socket
import sys
import os
import time
from threading import Thread

BACKLOG = 5

# Socket 클래스
class YDSocket:
    def __init__(self):
        self.listensock = 0
    # Bind 함수
    def Bind(self,port):
        #socket이 이름을 붙는다는 것을 제외하고는
        #BSD Socket 함수와 동일하게 사용할 수 있습니다.
        self.listensock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.listensock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.listensock.bind(('127.0.0.1',port))
        self.listensock.listen(BACKLOG)
    # Accept 함수
    def Accept(self):
        conn, addr = self.listensock.accept();
        print "Accept OK : ", addr
        return conn

# 스레드 클래스
class JobThread(Thread):
    def __init__(self, conn):
        Thread.__init__(self)
        self.conn = conn
        self.method = {"quit": self.func_quit}
    def run(self):
        while 1:
            read = self.conn.recv(1024)
            if read == '':
                print "Client Close"
                self.conn.close();
                return
            else :
                stripstr = read.rstrip('\r\n')
                if stripstr in self.method:
                    rtv = self.method.get(stripstr)()
                    if rtv == 0:
                        return
                else :
                    self.conn.send(read)
    # 유저가 quit 를 입력했을 경우 종료한다.
    def func_quit(self):
        print "Client Close func"
        self.conn.close();
        return 0;
