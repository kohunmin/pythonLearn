__author__ = 'Administrator'
from ydsocket import YDSocket, JobThread

acceptor = YDSocket()
acceptor.Bind(8080)
while 1:
    conn = acceptor.Accept()
    myJob = JobThread(conn)
    myJob.run()